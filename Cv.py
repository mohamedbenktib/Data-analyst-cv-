"""
سيرة ذاتية لمحلل بيانات باستخدام Python
"""

class CV:
    def __init__(self):
        self.personal_info = {
            "الاسم": "أحمد عبدالله",
            "العنوان": "جدة، المملكة العربية السعودية",
            "البريد الإلكتروني": "ahmed.data@example.com",
            "الهاتف": "+966501112233",
            "LinkedIn": "linkedin.com/in/ahmed-data-analyst",
            "GitHub": "github.com/ahmed-python-projects"
        }
        
        self.summary = """
        محلل بيانات متخصص في Python مع 4 سنوات خبرة في تحليل البيانات،
        تعلم الآلة، وتحويل البيانات إلى رؤى قابلة للتنفيذ.
        """
        
        self.skills = {
            "Python": ["Pandas", "NumPy", "Matplotlib", "Scikit-learn"],
            "قواعد البيانات": ["SQL", "MongoDB"],
            "تصور البيانات": ["Tableau", "Power BI"]
        }
        
        self.experience = [
            {
                "المنصب": "محلل بيانات",
                "الشركة": "شركة التقنية",
                "الفترة": "2020-الآن",
                "المهام": [
                    "تحليل البيانات باستخدام Python",
                    "بناء نماذج تنبؤية",
                    "إنشاء لوحات تحكم تفاعلية"
                ]
            }
        ]

if __name__ == "__main__":
    my_cv = CV()
    print("=== السيرة الذاتية ===")
    print(my_cv.personal_info)
    print(my_cv.summary)
    print("المهارات:", my_cv.skills)
