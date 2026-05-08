 
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
        
        
ScreenManager:
    transition: FadeTransition()
    id: screen_manager
    
'''
