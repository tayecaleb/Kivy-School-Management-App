 
Main_KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import gch kivy.utils.get_color_from_hex
#:import MagicBehavior kivymd.uix.behaviors.MagicBehavior
#:import environ os.environ
#:import gch kivy.utils.get_color_from_hex
#:import IconRightWidget kivymd.uix.list.IconRightWidget
#:import colors kivymd.color_definitions.colors
#:import gch kivy.utils.get_color_from_hex
#:import Clock kivy.clock.Clock
#:import rgba kivy.utils.get_color_from_hex
#: import ew kivy.uix.effectwidget
#: import AKSwipeMenu kivymd_extensions.akivymd.uix.swipemenu



<StudentRow>:
    orientation: "horizontal"
    md_bg_color: rgba("#ffffff")
    padding: ["10dp", 0, "10dp", 0]
    canvas.before:
        Color:
            rgba: [0.95, 0.95, 0.97, 1]
        Line:
            points: [self.x, self.y, self.right, self.y]
            width: 1

    MDLabel:
        text: root.id_text
        size_hint_x: 0.1
        font_style: "Caption"
        theme_text_color: "Hint"

    MDBoxLayout:
        size_hint_x: 0.3
        spacing: "12dp"
        padding: ["5dp", "10dp"]
        MDBoxLayout:
            size_hint: None, None
            size: "40dp", "40dp"
            md_bg_color: root.avatar_color
            radius: [20, ]
            pos_hint: {"center_y": .5}
            MDLabel:
                text: root.initials
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "Caption"
                bold: True
        MDBoxLayout:
            orientation: "vertical"
            pos_hint: {"center_y": .5}
            MDLabel:
                text: root.name
                bold: True
                font_style: "Body2"
                adaptive_height: True
            MDLabel:
                text: root.email
                font_style: "Caption"
                theme_text_color: "Hint"
                adaptive_height: True

    MDLabel:
        text: root.dept
        size_hint_x: 0.2
        font_style: "Body2"

    MDLabel:
        text: root.year
        size_hint_x: 0.1
        font_style: "Body2"

    MDBoxLayout:
        size_hint_x: 0.1
        MDLabel:
            text: root.gpa
            theme_text_color: "Custom"
            text_color: 0.1, 0.7, 0.3, 1
            bold: True

    MDBoxLayout:
        size_hint_x: 0.1
        padding: [0, "20dp"]
        MDBoxLayout:
            md_bg_color: [0.1, 0.8, 0.4, 0.1] if root.status == "Active" else [1, 0.6, 0.1, 0.1]
            radius: [12, ]
            MDLabel:
                text: "• " + root.status
                theme_text_color: "Custom"
                text_color: [0.1, 0.7, 0.3, 1] if root.status == "Active" else [0.9, 0.5, 0, 1]
                font_style: "Caption"
                bold: True
                halign: "center"

    BoxLayout:
        orientation: "vertical"
        size_hint_x: 0.1
        Widget:
            size_hint_y: None
            height: 50
        MDBoxLayout:
            spacing: "4dp"
            MDIconButton:
                icon: "pencil-outline"
                theme_text_color: "Custom"
                text_color: 0.3, 0.4, 1, 1
            MDIconButton:
                icon: "trash-can-outline"
                theme_text_color: "Custom"
                text_color: 1, 0.3, 0.3, 1
        Widget:


<StatCard>:
    orientation: "vertical"
    padding: "16dp"
    # size_hint: None, None
    # size: "200dp", "140dp"
    size_hint_y: None
    height: "140dp"
    radius: [12, ]
    elevation: 1
    shadow_softness: 4
    md_bg_color: 1, 1, 1, 1
    
    # Icon and Background Container
    MDBoxLayout:
        size_hint: None, None
        size: "36dp", "36dp"
        md_bg_color: root.icon_bg_color
        radius: [8, ]
        padding: ["6dp", "0dp", "0dp", "0dp"]
        
        MDIcon:
            icon: root.icon
            pos_hint: {"center_x": .5, "center_y": .5}
            font_size: "20sp"
            theme_text_color: "Custom"
            text_color: 0.3, 0.4, 1, 1

    # Title Label
    MDLabel:
        text: root.title
        font_style: "Button"
        theme_text_color: "Hint"
        adaptive_height: True
        padding_y: "8dp"

    # Main Value Label
    MDLabel:
        text: root.value
        font_style: "H5"
        bold: True
        adaptive_height: True

    # Subtitle Label
    MDLabel:
        text: root.subtitle
        font_style: "Caption"
        theme_text_color: "Secondary"
        adaptive_height: True

<NavbarTop>:
    size_hint_y: None
    height: "63dp"
    padding: ["16dp", "8dp", "16dp", "8dp"]
    spacing: "12dp"
    md_bg_color: rgba("#ffffff")
    radius: [0, 0, 0, 0]
    canvas.before:
        Color:
            rgba: [0.9, 0.9, 0.9, 1]
        Line:
            # [start_x, start_y, end_x, end_y]
            points: [self.x, self.y, self.right, self.y]
            width: 1.1

    MDBoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: 38

        MDLabel:
            text: root.text
            theme_text_color: "Custom"
            # font_style: "Button"
            bold: True
            font_size: "18sp"
            valign: "center"

        MDLabel:
            text: root.bottomText
            theme_text_color: "Custom"
            # font_style: "Button"
            bold: True
            font_size: "15sp"
            color: rgba("#94a3b8")
            valign: "center"

    Widget:

    MDRectangleFlatIconButton:
        text: "Export CSV"
        icon: "file-export"
        theme_text_color: "Custom"
        text_color: "#4A5568"
        line_color: "#E2E8F0"
        md_bg_color: "#ffffff"
        icon_color: "#4A5568"
        radius: [8, ]

    Widget:
        size_hint_x: None
        width: 5

    MDRectangleFlatIconButton:
        text: "Add Student"
        icon: "plus"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        line_color: 0, 0, 0, 0  # Remove the border line
        md_bg_color: 0.3, 0.4, 1, 1
        icon_color: 1, 1, 1, 1
        radius: [8, ]
            

<NavigationItem>:
    size_hint_y: None
    height: "56dp"
    padding: ["16dp", "8dp", "16dp", "8dp"]
    spacing: "12dp"
    # Background color changes based on active state
    md_bg_color: [0.3, 0.4, 1, 0.1] if self.active else [0, 0, 0, 0]
    radius: [12, ]
    active: False

    canvas.before:
        Color:
            rgba: [0.3, 0.4, 1, 1] if self.active else [0, 0, 0, 0]
        RoundedRectangle:
            # Vertical line on the far left
            pos: self.x, self.y + dp(14)
            size: dp(4), self.height - dp(28)
            radius: [2, ]

    # Icon Container
    MDBoxLayout:
        size_hint: None, None
        size: "36dp", "36dp"
        md_bg_color: [0.3, 0.4, 1, 0.15] if root.active else [0, 0, 0, 0.05]
        radius: [8, ]
        pos_hint: {"center_y": .5}
        padding: ["6dp", "0dp", "0dp", "0dp"]
        
        MDIcon:
            icon: root.icon
            pos_hint: {"center_x": .5, "center_y": .5}
            theme_text_color: "Custom"
            text_color: [0.3, 0.4, 1, 1] if root.active else [0.4, 0.4, 0.4, 1]

    # Menu Text
    MDLabel:
        text: root.text
        theme_text_color: "Custom"
        text_color: [0.3, 0.4, 1, 1] if root.active else [0.2, 0.2, 0.2, 1]
        # font_style: "Button"
        bold: True
        font_size: "13sp"
        valign: "center"

    # Badge/Counter
    MDBoxLayout:
        size_hint: None, None
        size: "24dp", "20dp"
        md_bg_color: [0.3, 0.4, 1, 1]
        radius: [10, ]
        pos_hint: {"center_y": .5}
        opacity: 1 if root.badge_text else 0
        
        MDLabel:
            text: root.badge_text
            halign: "center"
            font_size: "11sp"
            theme_text_color: "Custom"
            text_color: [1, 1, 1, 1]


<SidebarLeft>:
    orientation: "vertical"
    md_bg_color: rgba("#ffffff")
    canvas.before:
        Color:
            rgba: [0.9, 0.9, 0.9, 1]  # Light grey border color
        Line:
            # points: [x_start, y_start, x_end, y_end]
            # We use self.right to anchor it to the far right edge
            points: [self.right, self.y, self.right, self.top]
            width: 1.1  # Subtle thin line

            
    Widget:
        size_hint_y: None
        height: 15

    MDBoxLayout:
        size_hint_y: None
        height: 60
        Widget:
            size_hint_x: None
            width: 15
        BoxLayout:     
            orientation: "vertical"
            size_hint_x: None
            width: 45
            MDBoxLayout:
                size_hint: None, None
                width: 45
                height: 45
                radius: [10, 10, 10, 10]
                md_bg_color: rgba("#7c3aed")
                MDIconButton:
                    icon: "school"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    icon_color: rgba("#ffffff")
                    theme_text_color: 'Custom'

            Widget:
                

        MDBoxLayout:
            orientation: "vertical"
            padding: ['10dp', '10dp', '10dp', '10dp']
            MDLabel:
                text: "StudentOS"
                bold: True
                font_size: "25sp"

            Widget:
                size_hint_y: None
                height: 10

            MDLabel:
                text: "ACADEMIC PORTAL"
                color: rgba("#94a3b8")
                font_size: "13sp"
                bold: True
    
    Widget:
        size_hint_y: None
        height: 14
    
    MDSeparator:
        height: "1dp"
   
    
    Widget:
        size_hint_y: None
        height: 10


        
    # MDLabel:
    #     size_hint_y: None
    #     height: 25
    #     text: "Welcome, " + app.ussserfirstname[0:13]
    #     halign: "center"
    #     color: "#ffffff"
    
    MDLabel:
        text: "Main Menu"
        color: rgba("#94a3b8")
        font_size: "14sp"
        size_hint_y: None
        height: 25
        bold: True
        padding: ['20dp', '0dp', '0dp', '0dp']

    Widget:
        size_hint_y: None
        height: 15

    MDBoxLayout:
        id: nav_container
        orientation: 'vertical'
        size_hint_y: None
        height: 520
        padding: "20dp"
        spacing: "10dp"

        NavigationItem:
            id: item_students
            text: "Students"
            icon: "school"
            badge_text: "10"
            active: root.active[0]
            on_release: app.navigateToStudent("Student Screen")
        
        NavigationItem:
            id: item_past_students
            text: "Past Students"
            icon: "school"
            badge_text: "30"
            active: root.active[1]
            on_release: app.navigateToStudent("Past Student Screen")

        NavigationItem:
            id: item_teachers
            text: "Teachers"
            icon: "account-supervisor"
            badge_text: "20"
            active: root.active[2]

        NavigationItem:
            id: item_past_teachers
            text: "Past Teachers"
            icon: "account-supervisor"
            badge_text: "10"
            active: root.active[3]

        NavigationItem:
            id: item_courses
            text: "Courses"
            icon: "book-open-variant"
            active: root.active[4]

        NavigationItem:
            id: item_courses
            text: "Grades & Departments"
            icon: "bank"
            active: root.active[5]

        NavigationItem:
            id: item_departments
            text: "Settings"
            icon: "cog"
            active: root.active[6]

        NavigationItem:
            id: item_logout
            text: "Logout"
            icon: "logout"
            on_release: app.set_active(self)
            
       
    Widget:    
                
    Widget:
        size_hint_y: None
        height: 15
        
        


ScreenManager:
    transition: FadeTransition()
    id: screen_manager
    
'''
