import docker
import subprocess
import requests
import time
import os
def is_docker_installed():
    try:
        print(subprocess.run(["docker","--version"]))
        return True
    except FileNotFoundError:
        print("downloading")
        file=requests.get("https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=dd-smartbutton&utm_location=module&_gl=1*2t2mu1*_gcl_au*MjA4NTg3NDEwNy4xNzYzMzAxMzg1*_ga*NTEwMTAxNzQ2LjE3NjMyOTU5MDI.*_ga_XJWPQMJYHQ*czE3NjMzMDEzODUkbzIkZzEkdDE3NjMzMDE0MzgkajckbDAkaDA.")
        print(file)
        if(file.status_code==200):
            file=file.content
            with open("download.exe","wb") as f:
                f.write(file)
            subprocess.run(["download.exe","install","--quiet","--accept-license","--backend=wsl-2"])
            print("finish")
            subprocess.Popen(["C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"])
            return True          
    except Exception as e:
        print(e)

def run_bash_command(continer,command):
    output=continer.exec_run(command)
    return output

def is_docker_running():
    try:
        subprocess.run(
            ["docker", "info"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        print("bbb")
        return True
    except Exception as e:
        print(e)
        return False

def create_continer(timeout=45):
    d=False
    for i in range(timeout):
        time.sleep(1)
        print(i)
        if(is_docker_running()):
            print("hi docker is running")
            d=True
            break
    if(d==True):
        print("111")
        client=docker.from_env()
        
        try:
            client.images.get("my-linux-sandbox:latest")
            print("Image exists.")
        except docker.errors.ImageNotFound:
            print("Image NOT found.")
            try:
                image,build_logs=client.images.build(path=os.getcwd(),tag="my-linux-sandbox:latest",rm=True)
                print("hh")
            except Exception as e: 
                print(e)
                return
        while True:
            try:
                continer=client.containers.run("my-linux-sandbox:latest","sleep infinity","ls",name="linux_test",detach=True,volumes={(os.getcwd()+r"\mybe_virus"): {"bind": "/samples","mode":"rw"}})
                break
            except docker.errors.APIError as e:
                if "conflict" in str(e):
                    print("Container with the same name already exists. Removing existing container.")
                existing_container=client.containers.get("linux_test")
                existing_container.stop()
                existing_container.remove()
        print("קונטיינר נוצר. ID:", continer)
        print("לוגים ראשוניים:")
        print(continer.logs().decode(errors="ignore"))
        return continer       
               
def run_continer(continer):
    #print(run_bash_command(continer,"-w /samples ls").output.decode())
    viruses=continer.exec_run("ls -1",workdir="/samples").output.decode()
    print(viruses)

    print(run_bash_command(continer,"ls -1").output.decode())
    continer.exec_run("Xvfb :500 -screen 0 1280x1024x24", detach=True)
    for virus in viruses.splitlines():
        continer.exec_run("wine " + str(virus),detach=True,workdir="/samples")
        print(f"הרצת {virus} בוצעה.")
    output=run_bash_command(continer,"ps -eo comm,pid,pcpu,pmem,args --no-headers")
    text=str(output.output.decode())
    lines=text.splitlines()
    parsed = [line.split() for line in lines]
    print(parsed)
    print(run_bash_command(continer,"ls -1"))
    system_dict={
        "sleep":1,
        "ps":1,
        "Xvfb":1

    }
    for process in parsed:
       if process[0] not in system_dict:
           if(float(process[2])>10.0 or float(process[3])>10.0):
               print(f"תהליך חשוד זוהה: {process}")
    run_bash_command(continer,"stats --no-stream --all").output.decode()
       

    
    continer.stop()
    continer.remove()
    
#is_docker_installed()
continer=create_continer()
run_continer(continer)
 