# 🛡️ The Real Anti-Virus
**Advanced Malware Analysis & Threat Detection System**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker)
![YARA](https://img.shields.io/badge/YARA-Scanning-red?style=for-the-badge)

מערכת אנטי-וירוס מתקדמת לניתוח וחשיפת איומים (Malware Analysis), המשלבת בדיקות סטטיות ודינמיות בסביבה מבודדת לחלוטין. המערכת מתוכננת לספק מעטפת הגנה רב-שכבתית לזיהוי קבצים זדוניים בזמן אמת.

---

## 📋 אודות הפרויקט
המערכת נועדה לספק מעטפת הגנה וניתוח קבצים חשודים באמצעות שלוש שכבות הגנה עיקריות:

1.  **🔍 בדיקת חתימות (Hash Check):** השוואה מהירה של חתימות קבצים (SHA256) מול מאגרי מודיעין איומים (כמו Abuse.ch).
2.  **🧪 סריקה סטטית (Yara Scanning):** שימוש בחוקי YARA לזיהוי דפוסים, מחרוזות ומשפחות נוזקה בתוך הקוד מבלי להריץ אותו.
3.  **🛡️ ניתוח דינמי (Sandbox):** הרצת קבצי EXE בסביבת **Docker** מבודדת המבוססת על Linux & Wine לניטור התנהגות אקטיבית (**בפיתוח**)-> (נעשה בלינוקס כדי לבודד את הקרנל של המערכת הרגילה להורדת הסיכונים).

---

## ✨ תכונות מרכזיות (Key Features)

* **Isolated Sandbox Container:** הקמה אוטומטית של Container ייעודי לכל בדיקה. השימוש בלינוקס כ-Host מבטיח הפרדה ברמת הקרנל מהמערכת המארחת והגנה מקסימלית.
* **Windows Emulation:** תמיכה בהרצת קבצי Windows Executables בתוך סביבת הלינוקס של הדוקר באמצעות **Wine** ו-**Xvfb**.
* **Behavioral Monitoring:** ניטור צריכת משאבים (CPU/RAM) וזיהוי תהליכים עוינים בזמן ההרצה (בפיתוח).
* **Automated Intelligence:**  מאגרי חתימות וחוקי YARA מוכרים.

---

## 🛠️ טכנולוגיות בשימוש
* **Language:** Python
* **Virtualization:** Docker (Isolated Environment)
* **Compatibility:** Wine (Running Windows apps on Linux)
* **Analysis Tools:** YARA Engine, Hash Verification API,sandbox


