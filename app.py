from  app_imports import *


try:
    import pyi_splash
    pyi_splash.update_text("UI Loaded ...")
    pyi_splash.close()
except:
    pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print ("working")
        self.title = 'My Kivy App'
        self.icon = 'assets/App_Logo.png'
    
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        return Builder.load_string(kv)
    
    
    from app_functions_main._Home_Screen import toast_hello_world
    
if __name__ == '__main__':
    MainApp().run()
