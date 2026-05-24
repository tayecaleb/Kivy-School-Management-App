from  app_imports import *


try:
    import pyi_splash
    pyi_splash.update_text("UI Loaded ...")
    pyi_splash.close()
except:
    pass

class MainApp(MDApp):
    ## Active Student
    all_students = []  # Store your full database here
    items_per_page = 10
    current_page = 0

    ## Past Student
    all_students_past_student = []  # Store your full database here
    items_per_page_past_student = 10
    current_page_past_student = 0

    ## Active Teachers
    all_teachers = []  # Store your full database here
    items_per_page_teacher = 10
    current_page_teacher = 0

    ## Past Teachers
    all_past_teachers = []  # Store your full database here
    items_per_page_past_teacher = 10
    current_page_past_teacher = 0

    ## Courses
    all_courses = []  # Store your full database here
    items_per_page_course = 10
    current_page_course = 0

    ## Grades
    all_grades = []  # Store your full database here
    items_per_page_grade = 10
    current_page_grade = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print ("working")
        self.title = 'My Kivy App'
        self.icon = 'assets/App_Logo.png'
        
    
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(kv)
    
    def on_start(self):
        self.ussserimage = "assets/avatars.jfif"
        self.ussserfirstname = "caleb"
        self.ussserschoolname = "St. Mary's School"
        self.navigateToStudent("Student Screen")

        
    # def navigateToStudent(self, screen, page):
    #     self.root.current = screen
        
    #     # 1. Run your page loading logic first
    #     if screen == "Student Screen":
    #         self.loadStudentPage()
    #     elif screen == "Past Student Screen":
    #         self.loadPastStudentPage()
            
    #     # 2. Call set_active LAST, after the UI/Screen changes are finalized
    #     self.set_active(page)

    def navigateToStudent(self, screen):
        self.root.current = screen
        
        # 1. Run your page loading logic first
        if screen == "Student Screen":
            self.loadStudentPage()
        elif screen == "Past Student Screen":
            self.loadPastStudentPage()
        elif screen == "Teacher Screen":
            self.loadTeacherPage()
        elif screen == "Past Teacher Screen":
            self.loadPastTeacherPage()
        elif screen == "Course Screen":
            self.loadCoursePage()
        elif screen == "Grade Screen":
            self.loadGradePage()
        
    
    from app_functions_main._Student_Screen import toast_hello_world, loadStudentPage, \
            update_table_Student, next_page_Student,  prev_page_Student, set_grade_item_Student, set_item_Student
    from app_functions_main._Past_Student_Screen import loadPastStudentPage, \
            update_table_Past_Student, next_page_Past_Student,  prev_page_Past_Student, set_grade_item_Past_Student, set_item_Past_Student
    from app_functions_main._Teacher_Screen import loadTeacherPage, \
            update_table_Teacher, next_page_Teacher,  prev_page_Teacher, set_grade_item_Teacher, set_item_Teacher
    from app_functions_main._Past_Teacher_Screen import loadPastTeacherPage, \
            update_table_Past_Teacher, next_page_Past_Teacher,  prev_page_Past_Teacher, set_grade_item_Past_Teacher, set_item_Past_Teacher
    from app_functions_main._Course_Screen import loadCoursePage, \
            update_table_Course, next_page_Course,  prev_page_Course, set_grade_item_Course, set_item_Course
    from app_functions_main._Grade_Screen import loadGradePage, \
            update_table_grade, next_page_grade,  prev_page_grade, set_grade_item_grade, set_item_grade
    
if __name__ == '__main__':
    MainApp().run()
