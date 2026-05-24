from  app_imports import *

def loadPastStudentPage(self):
    
    self.root.ids.side_bar_past_student.clear_widgets(self.root.ids.side_bar_past_student.children[:])
    self.root.ids.side_bar_past_student.add_widget(
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
            active = [False, True, False, False, False, False, False, False],
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
            "on_release": lambda x=dept: self.set_item_past_student(x),
        } for dept in departments
    ]
    
    # 3. Initialize the menu object
    self.menu_past_student = MDDropdownMenu(
        caller=self.root.ids.dept_button_past_student, # This links menu to the button
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
            "on_release": lambda x=grade: self.set_grade_item_past_student(x),
        } for grade in grades
    ]
    
    # 3. Initialize the menu object
    self.grade_menu_past_student = MDDropdownMenu(
        caller=self.root.ids.grade_button_past_student, # This links menu to the button
        items=menu_items,
        width_mult=4,
    )

    self.all_students_past_student = [
        {
            "id_text": f"STU-{str(i).zfill(3)}",
            "names": f"Jack Ola {i}",
            "grade": f"SSS2",
            "initials": "J",
            "avatar_color": [0.3, 0.4, 1, 1],
            "dept": "Art",
            "date_joined": "12-05-2024",
            # "attendance": "3.85",
            # "status": "Active"
        } for i in range(1, 51)
    ]
    self.update_table_Past_Student()
    


def update_table_Past_Student(self):
    # Calculate start and end index
    start = self.current_page_past_student * self.items_per_page_past_student
    end = start + self.items_per_page_past_student
    
    # Slice the data and update RecycleView
    self.root.ids.rv_past_student.data = self.all_students_past_student[start:end]
    
    # Update page label
    total_pages = len(self.all_students_past_student) // self.items_per_page_past_student
    self.root.ids.page_num_past_student.text = f"Page {self.current_page_past_student + 1} of {total_pages}"
    self.root.ids.cur_page_num_past_student.text = str(self.current_page_past_student + 1)

def next_page_Past_Student(self):
    if (self.current_page_past_student + 1) * self.items_per_page_past_student < len(self.all_students_past_student):
        self.current_page_past_student += 1
        self.update_table_Past_Student()

def prev_page_Past_Student(self):
    if self.current_page_past_student > 0:
        self.current_page_past_student -= 1
        self.update_table_Past_Student()

def set_grade_item_Past_Student(self, text_item):
    # Update the button text to show the selection
    self.root.ids.grade_button_past_student.text = text_item
    self.grade_menu_past_student.dismiss()
    

def set_item_Past_Student(self, text_item):
    # Update the button text to show the selection
    self.root.ids.dept_button_past_student.text = text_item
    self.menu_past_student.dismiss()
