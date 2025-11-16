import docker
import subprocess
import requests
import time
def is_docker_installed():
    try:
        print(subprocess.run(["docker","--version"]))
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
            


    except Exception as e:
        print(e)
def is_docker_running():
    try:
        subprocess.run(
            ["docker", "info"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except:
        return False
def create_continer(timeout=45):
    d=False
    for i in range(timeout):
        time.sleep(1)
        if(is_docker_installed):
            d=True
            break
    if(d==True):
        client=docker.from_env()
        print(client.containers.run("mcr.microsoft.com/windows/servercore:ltsc2022",command="cmd.exe",name="win_test",detach=True))
#is_docker_installed()
create_continer()
