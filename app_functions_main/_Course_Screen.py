from  app_imports import *


def loadCoursePage(self):
    
    self.root.ids.side_bar_course.clear_widgets(self.root.ids.side_bar_course.children[:])
    self.root.ids.side_bar_course.add_widget(
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
            active = [False, False, False, False, True, False, False, False],
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
            "on_release": lambda x=dept: self.set_item_course(x),
        } for dept in departments
    ]
    
    # 3. Initialize the menu object
    self.menu_course = MDDropdownMenu(
        caller=self.root.ids.dept_button_course, # This links menu to the button
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
            "on_release": lambda x=grade: self.set_grade_item_course(x),
        } for grade in grades
    ]
    
    # 3. Initialize the menu object
    self.grade_menu_course = MDDropdownMenu(
        caller=self.root.ids.grade_button_course, # This links menu to the button
        items=menu_items,
        width_mult=4,
    )

    

    self.all_courses = [
        {
            "id_text": f"STU-{str(i).zfill(3)}",
            "course": f"Mathematics {i}",
            "departments": f"Science, General, ...",
            "grades": "JSS2, SS2, ...",
            "date_created": "12-05-2024",

        } for i in range(1, 51)
    ]
    self.update_table_Course()
    
def update_table_Course(self):
    # Calculate start and end index
    start = self.current_page_course * self.items_per_page_course
    end = start + self.items_per_page_course
    
    # Slice the data and update RecycleView
    self.root.ids.rv_course.data = self.all_courses[start:end]
    
    # Update page label
    total_pages = len(self.all_courses) // self.items_per_page_course
    self.root.ids.page_num_course.text = f"Page {self.current_page_course + 1} of {total_pages}"
    self.root.ids.cur_page_num_course.text = str(self.current_page_course + 1)

def next_page_Course(self):
    if (self.current_page_course + 1) * self.items_per_page_course < len(self.all_courses):
        self.current_page_course += 1
        self.update_table_Course()

def prev_page_Course(self):
    if self.current_page_course > 0:
        self.current_page_course -= 1
        self.update_table_Course()

def set_grade_item_Course(self, text_item):
    # Update the button text to show the selection
    self.root.ids.grade_button_course.text = text_item
    self.grade_menu_course.dismiss()
    

def set_item_Course(self, text_item):
    # Update the button text to show the selection
    self.root.ids.dept_button_course.text = text_item
    self.menu_course.dismiss()