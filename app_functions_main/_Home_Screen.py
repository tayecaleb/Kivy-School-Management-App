from  app_imports import *


def toast_hello_world(self):   
    toast("Hello, World!")
    
def set_active(self, selected_item):
        # Reset all items in the layout to inactive
        for item in selected_item.parent.children:
            if isinstance(item, NavigationItem):
                item.active = False
        
        # Set the clicked item to active
        selected_item.active = True