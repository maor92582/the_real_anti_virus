import hashlib
import requests
import zipfile
import io

def get_new_hashlist():
    url="https://bazaar.abuse.ch/export/txt/sha256/full/"
    x=requests.get(url)
    print(x)
    if(x.status_code==200):
        with zipfile.ZipFile(io.BytesIO(x.content)) as z:
            print(z.filelist)
            return get_hash_set(z.extract("full_sha256.txt"))


def file_hashing(filepath): #ממיר את הקובץ לsha256
    with open(filepath,'rb') as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()
def get_hash_set(file):#מוצא hash חדש
    hashes=set()
    with open(file,'r') as f:
        for line in f:
            line = line.strip()
            if not line or len(line) != 64:
                continue  
            hashes.add(line)
    return hashes
def check_if_sus(hashes,hash):#משווא בין המאגר לhash
    if hash in hashes:
        return True
    return False
def run_check(filepath):
    file_hash=file_hashing(filepath)
    hashset  = get_new_hashlist()
    print(check_if_sus(hashset,file_hash))
            
run_check("readme.txt")


