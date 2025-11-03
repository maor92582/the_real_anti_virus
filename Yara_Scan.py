import yara

# חוק לדוגמה — מזהה את המילה "malware" בכל קובץ
rule_source = '''
rule SimpleTest {
    strings:
        $a = "malware"
    condition:
        $a
}
'''

# מקמפלים את החוק
rules = yara.compile(filepath="C:\\Users\\555\\OneDrive\\Documents\\the_real_anti_virus\\rules\\rules\\crypto\\crypto_signatures.yar")

# סורקים קובץ לדוגמה
file_path = "readme.txt"  # תחליף לשם קובץ אמיתי
matches = rules.match(filepath=file_path)

if matches:
    print("🔴 נמצא חוק תואם:")
    for match in matches:
        print(f" - {match.rule}")
else:
    print("✅ אין התאמה — הקובץ כנראה נקי.")
