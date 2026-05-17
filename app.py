from  app_imports import *


try:
    import pyi_splash
    pyi_splash.update_text("UI Loaded ...")
    pyi_splash.close()
except:
    pass

class MainApp(MDApp):
    all_students = []  # Store your full database here
    items_per_page = 10
    current_page = 0
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
    
    from app_functions_main._Student_Screen import toast_hello_world, loadStudentPage, \
            update_table_Student, next_page_Student,  prev_page_Student, set_grade_item_Student, set_item_Student
    from app_functions_main._Past_Student_Screen import loadPastStudentPage
    
    
if __name__ == '__main__':
    MainApp().run()
