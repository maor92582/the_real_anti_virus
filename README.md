# 🛡️ The Real Anti-Virus
**Advanced Malware Analysis & Threat Detection System**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker)
![YARA](https://img.shields.io/badge/YARA-Scanning-red?style=for-the-badge)

מערכת אנטי-וירוס שפיתחתי לניתוח וחשיפת תוכנות זדוניות, האנטי וירוס ישלב בדיקות סטטיות ובדיקות דינמיות שיהיו בסביבה מבודדת.

## 📋 אודות הפרויקט
המערכת נועדה לניתוח קבצים\תוכנות חשודות באמצעות שלוש שכבות בדיקה עיקריות:

1.  **🔍 בדיקת חתימות (Hash Check):** השוואה מהירה של חתימות קבצים (SHA256) מול מאגרי hash קיימים.
2.  **🧪 סריקה סטטית (Yara Scanning):** שימוש בחוקי YARA לזיהוי דפוסים, מחרוזות ומשפחות נוזקה בתוך הקוד מבלי להריץ אותו.
3.  **🛡️ ניתוח דינמי (Sandbox):** הרצת קבצי EXE בסביבת **Docker** מבודדת המבוססת על Linux & Wine לניטור התנהגות  (**בפיתוח**)-> (נעשה בלינוקס כדי לבודד את הקרנל של המערכת הרגילה להורדת הסיכונים).

.

