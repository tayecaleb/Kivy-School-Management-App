from  app_imports import *


def loadTeacherPage(self):
    
    self.root.ids.side_bar_teacher.clear_widgets(self.root.ids.side_bar_teacher.children[:])
    self.root.ids.side_bar_teacher.add_widget(
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
            ussserschoolname = self.ussserschoolname,
            active = [False, False, True, False, False, False, False, False],
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
            "on_release": lambda x=dept: self.set_item_teacher(x),
        } for dept in departments
    ]
    
    # 3. Initialize the menu object
    self.menu_teacher = MDDropdownMenu(
        caller=self.root.ids.dept_button_teacher, # This links menu to the button
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
            "on_release": lambda x=grade: self.set_grade_item_teacher(x),
        } for grade in grades
    ]
    
    # 3. Initialize the menu object
    self.grade_menu_teacher = MDDropdownMenu(
        caller=self.root.ids.grade_button_teacher, # This links menu to the button
        items=menu_items,
        width_mult=4,
    )

    self.all_teachers = [
        {
            "id_text": f"STU-{str(i).zfill(3)}",
            "names": f"Paul Tunde {i}",
            "email": f"paultunde@gmail.com",
            "initials": "J",
            "avatar_color": [0.3, 0.4, 1, 1],
            "date_joined": "12-05-2024",
            # "attendance": "3.85",
            # "status": "Active"
        } for i in range(1, 51)
    ]
    self.update_table_Teacher()
    
def update_table_Teacher(self):
    # Calculate start and end index
    start = self.current_page_teacher * self.items_per_page_teacher
    end = start + self.items_per_page_teacher
    
    # Slice the data and update RecycleView
    self.root.ids.rv_teacher.data = self.all_teachers[start:end]
    
    # Update page label
    total_pages = len(self.all_teachers) // self.items_per_page_teacher
    self.root.ids.page_num_teacher.text = f"Page {self.current_page_teacher + 1} of {total_pages}"
    self.root.ids.cur_page_num_teacher.text = str(self.current_page_teacher + 1)

def next_page_Teacher(self):
    if (self.current_page_teacher + 1) * self.items_per_page_teacher < len(self.all_teachers):
        self.current_page_teacher += 1
        self.update_table_Teacher()

def prev_page_Teacher(self):
    if self.current_page_teacher > 0:
        self.current_page_teacher -= 1
        self.update_table_Teacher()

def set_grade_item_Teacher(self, text_item):
    # Update the button text to show the selection
    self.root.ids.grade_button_teacher.text = text_item
    self.grade_menu_teacher.dismiss()
    

def set_item_Teacher(self, text_item):
    # Update the button text to show the selection
    self.root.ids.dept_button_teacher.text = text_item
    self.menu_teacher.dismiss()