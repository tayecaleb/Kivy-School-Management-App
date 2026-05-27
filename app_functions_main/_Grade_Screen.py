from  app_imports import *
## new


def loadGradePage(self):
    
    self.root.ids.side_bar_grade.clear_widgets(self.root.ids.side_bar_grade.children[:])
    self.root.ids.side_bar_grade.add_widget(
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
            active = [False, False, False, False, False, True, False, False],
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
            "on_release": lambda x=dept: self.set_item_grade(x),
        } for dept in departments
    ]
    
    # 3. Initialize the menu object
    self.menu_grade = MDDropdownMenu(
        caller=self.root.ids.dept_button_grade, # This links menu to the button
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
            "on_release": lambda x=grade: self.set_grade_item_grade(x),
        } for grade in grades
    ]
    
    # 3. Initialize the menu object
    self.grade_menu_grade = MDDropdownMenu(
        caller=self.root.ids.grade_button_grade, # This links menu to the button
        items=menu_items,
        width_mult=4,
    )

    

    self.all_grades = [
        {
            "id_text": f"STU-{str(i).zfill(3)}",
            "grade": f"JSS2 {i}",
            "departments": f"Science, General, ...",
            "date_created": "12-05-2024",

        } for i in range(1, 51)
    ]
    self.update_table_grade()
    
def update_table_grade(self):
    # Calculate start and end index
    start = self.current_page_grade * self.items_per_page_grade
    end = start + self.items_per_page_grade
    
    # Slice the data and update RecycleView
    self.root.ids.rv_grade.data = self.all_grades[start:end]
    
    # Update page label
    total_pages = len(self.all_grades) // self.items_per_page_grade
    self.root.ids.page_num_grade.text = f"Page {self.current_page_grade + 1} of {total_pages}"
    self.root.ids.cur_page_num_grade.text = str(self.current_page_grade + 1)

def next_page_grade(self):
    if (self.current_page_grade + 1) * self.items_per_page_grade < len(self.all_grades):
        self.current_page_grade += 1
        self.update_table_grade()

def prev_page_grade(self):
    if self.current_page_grade > 0:
        self.current_page_grade -= 1
        self.update_table_grade()

def set_grade_item_grade(self, text_item):
    # Update the button text to show the selection
    self.root.ids.grade_button_grade.text = text_item
    self.grade_menu_grade.dismiss()
    

def set_item_grade(self, text_item):
    # Update the button text to show the selection
    self.root.ids.dept_button_grade.text = text_item
    self.menu_grade.dismiss()