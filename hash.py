import hashlib
def file_hashing(filepath): #ממיר את הקובץ לsha256
    with open(filepath,'rb') as f:
        file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()
def get_hash_set(filepath):
    hashes=set()
    with open(filepath,'r') as f:
        for line in f:
            line = line.strip()
            if not line or len(line) != 64:
                continue  
            hashes.add(line)
    return hashes
def check_if_sus(hashes,hash):
    if hash in hashes:
        return True
    return False
filepath="readme.txt"
file_hash  = file_hashing(filepath)
print(file_hash )
hashset=get_hash_set("data\\full_sha256.txt")
print(check_if_sus(hashset,file_hash))
          



