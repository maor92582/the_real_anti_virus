import yara
import os


def run_yara(file_path):
    folderpath="C:\\Users\\555\\OneDrive\\Documents\\the_real_anti_virus\\rules"
    x=False
    for root,dir,files in os.walk(folderpath):
        for file in files:
            if not file.endswith(('.yar', '.yara')):
                continue
            rulepath=os.path.join(root,file)
            if (
                    "deprecated" in root or
                    "Android" in root or
                    "ELF" in file or
                    "webshells_index" in file or
                    "index_w_mobile" in file or
                    "index.yar" in file
                 ):
                    continue
            if "domain.yar" in file or "ip.yar" in file or "url.yar" in file:
                continue
            try:
                rules=yara.compile(filepath=rulepath)
                matches = rules.match(filepath=file_path)
            except yara.SyntaxError as e:
                print(f"⚠️ שגיאה בקובץ חוק: {rulepath}\n   ➜ {e}")
                continue
            except Exception as e:
                print(f"⚠️ בעיה אחרת בקובץ {rulepath}: {e}")
                continue
            if matches:
                print("🔴 נמצא חוק תואם:")
                for match in matches:
                    print(f" - {match.rule}")
                    x=True
                    return x
    return x
            

    # סורקים קובץ לדוגמה
x=run_yara("readme.txt")
if(x==False):
    print("this file not scary")