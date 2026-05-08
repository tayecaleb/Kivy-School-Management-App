Home_Screen = '''

# ScreenManager:
#     ## transition: FadeTransition()
#     id: screen_manager
    
    MDScreen:
        name: "Home Screen"
        EffectWidget:
            effects: [ew.VerticalBlurEffect(size=10), ew.HorizontalBlurEffect(size=10)]
            FitImage:
                source: "test.jpg"
                id: backimg99
                
                      
                
        MDBoxLayout:
            orientation: "vertical"
            padding: ['10dp', '10dp', '10dp', '50dp']
            Widget:

            BoxLayout:
                size_hint_y: None
                height: self.minimum_height
                orientation: "vertical"
                spacing: "20dp"

                FitImage:
                    source: "assets/App_Logo.png"
                    size_hint: None, None
                    size: "150dp", "150dp"
                    pos_hint: {"center_x": .5}

                MDLabel:
                    text: "Welcome to the Home Screen"
                    font_style: "H4"
                    halign: "center"
                    size_hint_y: None
                    height: 40
                    

                MDFillRoundFlatButton:
                    text: "Say Hello"
                    pos_hint: {"center_x": .5}
                    md_bg_color: app.theme_cls.primary_color
                    on_release: app.toast_hello_world()

            Widget:


'''