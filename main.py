from kivy import Config
from kivy import platform
if platform in ["android", "ios"]:
    Config.set('input', 'default', 'mtdev,/dev/input/event0,en-us')
    Config.set('input', 'mouse', 'mouse,disable_multitouch')
else:
    Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
from kivy.uix.screenmanager import Screen
import os
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import NumericProperty, ColorProperty, ObjectProperty, StringProperty
from navigation import NavigationScreenManager


class MainScreenManager(NavigationScreenManager):
    pass


class ScreenObjectProperty(Screen):
    layout = ObjectProperty(None)


class SheetViewerScreen(Screen):
    sheet_viewer = ObjectProperty(None)


class CatalogScreen(Screen):
    catalog_name = StringProperty("")
    back_color = ColorProperty()
    scroll = ObjectProperty(None)


class MindMapViewerScreen(Screen):
    scatter_mind_map = ObjectProperty(None)


class MedicsProtocols(App):
    spacing_padding = NumericProperty(dp(10))
    menu_background = ColorProperty((0.206, 0.238, 0.246, 1))
    main_screen_manager = ObjectProperty(None)
    speciality_selector_width = dp(175)
    app_folders = (os.path.join("choices", "cardiologie"),
                   os.path.join("choices", "pneumologie"),
                   os.path.join("choices", "echographie"),
                   os.path.join("choices", "geriatrie"),
                   os.path.join("choices", "hematologie"),
                   os.path.join("choices", "hepato_gastro"),
                   os.path.join("choices", "immunologie"),
                   os.path.join("choices", "medecine_interne"),
                   os.path.join("choices", "nephrologie"),
                   os.path.join("choices", "pediatrie"),
                   os.path.join("choices", "rhumatologie"),
                   os.path.join("choices", "urgences"),
                   os.path.join("choices", "neurologie"))

    def build(self):
        self.icon = "images/icon.png"
        self.main_screen_manager = MainScreenManager()
        return self.main_screen_manager

    def on_start(self):
        if not os.path.exists("choices"):
            os.mkdir("choices")
        for folder in self.app_folders:
            if not os.path.exists(folder):
                os.mkdir(folder)


MedicsProtocols().run()
