Past_Student_Screen = '''

# ScreenManager:
#     ## transition: FadeTransition()
#     id: screen_manager
    
    MDScreen:
        name: "Past Student Screen"
        EffectWidget:
            effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
            FitImage:
                source: "test.jpg"
                id: backimg99
                
                      
                
        MDBoxLayout:
            orientation: "horizontal"
            
            MDBoxLayout:
                size_hint_x: .2
                orientation: "vertical"
                id: side_bar_past_student
                

        
            MDBoxLayout:
                size_hint_x: .8
                orientation: "vertical"  
                NavbarTop:
                    text: "Students"
                    bottomText: "StudentOS › Students"
                    buttonText: "Add Student"

                MDBoxLayout:
                    orientation: "vertical"  
                    padding: ["20dp", "0dp", "20dp", "0dp"]   
                    MDBoxLayout:
                        orientation: "vertical"
                        
                        Widget:
                            size_hint_y: None
                            height: 15

                        # Container for the cards
                        MDBoxLayout:
                            adaptive_height: True
                            
                            spacing: "16dp"

                            StatCard:
                                icon: "school"
                                icon_bg_color: 0.9, 0.9, 1, 1
                                title: "Total Students"
                                value: "10"
                                subtitle: "Enrolled this term"

                            StatCard:
                                icon: "check-bold"
                                icon_bg_color: 0.9, 1, 0.9, 1
                                title: "Active"
                                value: "8"
                                subtitle: "Currently studying"

                            StatCard:
                                icon: "chart-line"
                                icon_bg_color: 1, 0.9, 1, 1
                                title: "Avg GPA"
                                value: "3.59"
                                subtitle: "Across all students"


                            StatCard:
                                icon: "town-hall"
                                icon_bg_color: 1, 0.9, 1, 0.8
                                title: "Departments"
                                value: "9"
                                subtitle: "Unique programs"

                        Widget:
                            size_hint_y: None
                            height: 25


                        # Row 3: Search and Filter Bar
                        MDBoxLayout:
                            adaptive_height: True
                            spacing: "16dp"
                            
                            MDBoxLayout:
                                md_bg_color: 1, 1, 1, 1
                                radius: [8, ]
                                padding: ["12dp", 0, "12dp", 0]
                                size_hint_x: None
                                width: "300dp"
                                height: "44dp"
                                MDIcon:
                                    icon: "magnify"
                                    pos_hint: {"center_y": .5}
                                    theme_text_color: "Hint"
                                BoxLayout:
                                    orientation: "vertical"
                                    Widget:
                                    MDTextField:
                                        hint_text: "Search students..."
                                        mode: "fill"
                                        fill_color_normal: 1, 1, 1, 0
                                        active_line: False
                                        line_color_normal: 0, 0, 0, 0
                                        pos_hint: {"center_y": .5}
                                    Widget:

                            MDRoundFlatIconButton:
                                id: grade_button  # Added ID
                                text: "All Grades"
                                icon: "chevron-down"
                                icon_position: "right"  # Moves arrow to the right side
                                line_color: 0.88, 0.91, 0.94, 1
                                md_bg_color: 1, 1, 1, 1
                                theme_text_color: "Custom"
                                text_color: 0.3, 0.3, 0.4, 1
                                on_release: app.grade_menu.open()  # Opens the menu

                            # Filters (Dropdown Placeholders)
                            MDRoundFlatIconButton:
                                id: dept_button  # Added ID
                                text: "All Departments"
                                icon: "chevron-down"
                                icon_position: "right"  # Moves arrow to the right side
                                line_color: 0.88, 0.91, 0.94, 1
                                md_bg_color: 1, 1, 1, 1
                                theme_text_color: "Custom"
                                text_color: 0.3, 0.3, 0.4, 1
                                on_release: app.menu.open()  # Opens the menu
                            
                            

                            Widget: # Spacer

                            # Sort Filters
                            MDRoundFlatIconButton:
                                text: "Name"
                                icon: "swap-vertical"
                                text_color: 0.3, 0.4, 1, 1
                                line_color: 0.9, 0.9, 1, 1
                            
                            MDRoundFlatIconButton:
                                text: "GPA"
                                icon: "swap-vertical"
                                text_color: 0.3, 0.4, 1, 1
                                line_color: 0.9, 0.9, 1, 1


                        Widget:
                            size_hint_y: None
                            height: 15 

                        # Table Card
                        MDCard:
                            orientation: "vertical"
                            adaptive_height: True
                            radius: [12, ]
                            md_bg_color: "#ffffff"
                            shadow_softness: 8  # Makes the shadow look modern/soft
                            # To add a border to a card:
                            line_color: 0.88, 0.91, 0.94, 1
                            line_width: 1
                            
                            # Header remains outside the RecycleView so it doesn't scroll
                            MDBoxLayout:
                                size_hint_y: None
                                height: "50dp"
                                md_bg_color: 0.98, 0.98, 1, 1
                                padding: ["10dp", 0]
                                MDLabel:
                                    text: "ID"
                                    size_hint_x: 0.1
                                    font_style: "Caption"
                                    bold: True
                                MDLabel:
                                    text: "STUDENT"
                                    size_hint_x: 0.3
                                    font_style: "Caption"
                                    bold: True
                                MDLabel:
                                    text: "DEPARTMENT"
                                    size_hint_x: 0.2
                                    font_style: "Caption"
                                    bold: True
                                MDLabel:
                                    text: "YEAR"
                                    size_hint_x: 0.1
                                    font_style: "Caption"
                                    bold: True
                                MDLabel:
                                    text: "GPA"
                                    size_hint_x: 0.1
                                    font_style: "Caption"
                                    bold: True
                                MDLabel:
                                    text: "STATUS"
                                    size_hint_x: 0.1
                                    font_style: "Caption"
                                    bold: True
                                MDLabel:
                                    text: "ACTIONS"
                                    size_hint_x: 0.1
                                    font_style: "Caption"
                                    bold: True
                            # The RecycleView
                            RecycleView:
                                id: rv
                                viewclass: 'StudentRow'
                                size_hint_y: None
                                height: dp(270)  # Use dp for consistency across devices
                                
                                # --- Scrollbar Settings ---
                                bar_width: dp(6)                # Width of the scrollbar
                                bar_color: 0.3, 0.4, 1, 0.8     # The color of the bar (Matches your blue theme)
                                bar_inactive_color: 0.3, 0.4, 1, 0.2  # Color when not scrolling
                                scroll_type: ['bars', 'content'] # Allows scrolling via bar or dragging content
                                
                                RecycleBoxLayout:
                                    default_size: None, dp(70)
                                    default_size_hint: 1, None
                                    size_hint_y: None
                                    height: self.minimum_height
                                    orientation: 'vertical'

                            
                            # Inside the MDCard where your RecycleView lives:
                            MDBoxLayout:
                                size_hint_y: None
                                height: "56dp"
                                padding: ["20dp", 0]
                                spacing: "12dp"
                                canvas.before:
                                    Color:
                                        rgba: 0.95, 0.95, 0.97, 1
                                    Line:
                                        points: [self.x, self.top, self.right, self.top]
                                        width: 1

                                MDLabel:
                                    id: page_num
                                    text: "Page 1 of 5"
                                    font_style: "Caption"
                                    theme_text_color: "Secondary"

                                Widget: # Spacer

                                
                                MDIconButton:
                                    icon: "chevron-left"
                                    on_release: app.prev_page()
                                
                              
                                # Optional: Page Numbers (simplified)
                                BoxLayout:
                                    orientation: "vertical"
                                    size_hint_x: None
                                    width: 40
                                        
                                    Widget:
                                        
                                    MDBoxLayout:
                                        orientation: "vertical"
                                        size_hint: None, None
                                        width: 40
                                        height: 30
                                        md_bg_color: 0.3, 0.4, 1, 0.1
                                        Widget:
                                        MDLabel:
                                            id: cur_page_num
                                            text: "1"
                                            font_style: "Caption"
                                            theme_text_color: "Secondary"
                                            halign: "center"
                                        Widget:
                                    Widget:
                                        size_hint_y: None
                                        height: 10

                                # MDFlatButton:
                                    
                                #     id: cur_page_num
                                #     text: "1"
                                    
                                #     text_color: 0.3, 0.4, 1, 1

                            
                                MDIconButton:
                                    icon: "chevron-right"
                                    on_release: app.next_page()

                        Widget:

                

          

'''