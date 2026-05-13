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
        self.root.ids.side_bar_box.clear_widgets(self.root.ids.side_bar_box.children[:])
        self.root.ids.side_bar_box.add_widget(
            SidebarLeft(
                dashboard = "#ffffff",
                dashboard2 = "#FF0000",
                courses = "#ffffff",
                students = "#ffffff",
                studentsg = "#ffffff",
                teachers = "#ffffff",
                pastteachers = "#ffffff",
                departments = "#ffffff",
                terms = "#ffffff",
                courses2 = "#176477",
                students2 = "#176477",
                studentsg2 = "#176477",
                teachers2 = "#176477",
                departments2 = "#176477",
                terms2 = "#176477",
                pastteachers2 = "#176477",
                ussserimage = self.ussserimage,
                ussserfirstname = self.ussserfirstname,
                ussserschoolname = self.ussserschoolname
            )
        )

        # 1. Define the items you want in the dropdown
        departments = ["All Departments", "Science", "Commerce", "Art"]
        
        # 2. Create the menu items list
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": dept,
                "height": dp(54),
                "on_release": lambda x=dept: self.set_item(x),
            } for dept in departments
        ]
        
        # 3. Initialize the menu object
        self.menu = MDDropdownMenu(
            caller=self.root.ids.dept_button, # This links menu to the button
            items=menu_items,
            width_mult=4,
        )

        # 1. Define the items you want in the dropdown
        grades = ["All Grades", "JSS 1", "JSS 2", "JSS 3", "SSS 1", "SSS 2", "SSS 3"]
        
        # 2. Create the menu items list
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": grade,
                "height": dp(54),
                "on_release": lambda x=grade: self.set_grade_item(x),
            } for grade in grades
        ]
        
        # 3. Initialize the menu object
        self.grade_menu = MDDropdownMenu(
            caller=self.root.ids.grade_button, # This links menu to the button
            items=menu_items,
            width_mult=4,
        )

        self.all_students = [
            {
                "id_text": f"STU-{str(i).zfill(3)}",
                "name": f"Student {i}",
                "email": f"student{i}@uni.edu",
                "initials": "S",
                "avatar_color": [0.3, 0.4, 1, 1],
                "dept": "Computer Science",
                "year": "Year 3",
                "gpa": "3.85",
                "status": "Active"
            } for i in range(1, 51)
        ]
        self.update_table()
        

    def update_table(self):
        # Calculate start and end index
        start = self.current_page * self.items_per_page
        end = start + self.items_per_page
        
        # Slice the data and update RecycleView
        self.root.ids.rv.data = self.all_students[start:end]
        
        # Update page label
        total_pages = len(self.all_students) // self.items_per_page
        self.root.ids.page_num.text = f"Page {self.current_page + 1} of {total_pages}"
        self.root.ids.cur_page_num.text = str(self.current_page + 1)

    def next_page(self):
        if (self.current_page + 1) * self.items_per_page < len(self.all_students):
            self.current_page += 1
            self.update_table()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_table()

    def set_grade_item(self, text_item):
        # Update the button text to show the selection
        self.root.ids.grade_button.text = text_item
        self.grade_menu.dismiss()
        

    def set_item(self, text_item):
        # Update the button text to show the selection
        self.root.ids.dept_button.text = text_item
        self.menu.dismiss()
        
    
    
    from app_functions_main._Home_Screen import toast_hello_world, set_active
    
if __name__ == '__main__':
    MainApp().run()
