from  app_modules_widget_imports import *


class StudentRow(RecycleDataViewBehavior, MDBoxLayout):
    id_text = StringProperty()
    names = StringProperty()
    grade = StringProperty()
    initials = StringProperty()
    avatar_color = ColorProperty()
    dept = StringProperty()
    date_joined = StringProperty()
    # gpa = StringProperty()
    # status = StringProperty()

    def refresh_view_attrs(self, rv, index, data):
        # This handles the data updates when scrolling
        return super().refresh_view_attrs(rv, index, data)

class TeacherRow(RecycleDataViewBehavior, MDBoxLayout):
    id_text = StringProperty()
    names = StringProperty()
    email = StringProperty()
    initials = StringProperty()
    avatar_color = ColorProperty()
    date_joined = StringProperty()
    # gpa = StringProperty()
    # status = StringProperty()

    def refresh_view_attrs(self, rv, index, data):
        # This handles the data updates when scrolling
        return super().refresh_view_attrs(rv, index, data)

class GradeRow(RecycleDataViewBehavior, MDBoxLayout):
    id_text = StringProperty()
    grade = StringProperty()
    departments = StringProperty()
    date_created = StringProperty()

    def refresh_view_attrs(self, rv, index, data):
        # This handles the data updates when scrolling
        return super().refresh_view_attrs(rv, index, data)

class CourseRow(RecycleDataViewBehavior, MDBoxLayout):
    id_text = StringProperty()
    course = StringProperty()
    departments = StringProperty()
    grades = StringProperty()
    date_created = StringProperty()

    def refresh_view_attrs(self, rv, index, data):
        # This handles the data updates when scrolling
        return super().refresh_view_attrs(rv, index, data)

class StatCard(MDCard):
    # Defining these as properties allows the KV code to "see" them
    icon = StringProperty("alert")
    icon_bg_color = ColorProperty([0.9, 0.9, 0.9, 1])
    title = StringProperty("Title")
    value = StringProperty("0")
    subtitle = StringProperty("Subtitle")

class NavbarTop(MDBoxLayout):
    text = StringProperty("")
    buttonText = StringProperty("")
    bottomText = StringProperty("")



class SidebarLeft(MDBoxLayout):
    dashboard = StringProperty()
    students = StringProperty()
    studentsg = StringProperty()
    courses = StringProperty()
    teachers = StringProperty()
    # fees = StringProperty()
    departments = StringProperty()
    terms = StringProperty()
    pastteachers = StringProperty()
    
    dashboard2 = StringProperty()
    students2 = StringProperty()
    studentsg2 = StringProperty()
    courses2 = StringProperty()
    teachers2 = StringProperty()
    # fees2 = StringProperty()
    departments2 = StringProperty()
    terms2 = StringProperty()
    pastteachers2 = StringProperty()

    ussserimage = StringProperty("assets/avatars.jfif")
    ussserfirstname = StringProperty()
    ussserschoolname = StringProperty()
    active = ListProperty([False, False, False, False, False, False, False])


class NavigationItem(ButtonBehavior, MDBoxLayout):
    active = BooleanProperty(False)
    text = StringProperty("")
    icon = StringProperty("")
    badge_text = StringProperty("")
    

