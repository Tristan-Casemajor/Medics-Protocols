from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

Builder.load_file("navigation.kv")


class NavigationScreenManager(ScreenManager):
    screen_stack = []
    current_app = ObjectProperty(None)

    def push_screen(self, screen_name, catalog_name="", dir_name="", back_color=(), path_to_file="", extension=""):
        self.screen_stack.append(self.current)
        self.transition.direction = "left"
        self.current = screen_name
        if catalog_name and dir_name:
            self.current_app.main_screen_manager.get_screen("Catalog").catalog_name = catalog_name
            self.current_app.main_screen_manager.get_screen("Catalog").back_color = back_color
            self.current_app.main_screen_manager.get_screen("Catalog").scroll.catalog_layout.update_widgets(dir_name)

        elif path_to_file and extension == ".txt":
            self.current_app.main_screen_manager.get_screen("SheetViewer").sheet_viewer.viewer_label.update_text(path_to_file)

        elif path_to_file and extension in [".jpg", ".gif", ".jpeg", ".ico", ".png"]:
            self.current_app.main_screen_manager.get_screen("MindMapViewer")


    def pop_screen(self):
        if self.screen_stack:  # Check if the stack is not empty
            screen_name = self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name
            self.screen_stack.pop()

        else:
            print("Screen stack is empty. Cannot pop.")
