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
    self.update_table_Student()
    
