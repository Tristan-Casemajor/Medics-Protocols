import os
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import NumericProperty, ColorProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy import platform
from navigation import NavigationScreenManager


class MainScreenManager(NavigationScreenManager):
    pass


class MedicsProtocols(App):
    spacing_padding = NumericProperty(dp(10))
    menu_background = ColorProperty((0.206, 0.238, 0.246, 1))
    main_screen_manager = ObjectProperty(None)
    def build(self):
        self.icon = "images/icon.png"
        self.main_screen_manager = MainScreenManager()
        return self.main_screen_manager

    def on_start(self):
        if not os.path.exists("choices"):
            os.mkdir("choices")
        if not os.path.exists("choices/cardiologie"):
            os.mkdir("choices/cardiologie")

MedicsProtocols().run()
