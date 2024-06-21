from kivy.uix.screenmanager import ScreenManager


class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push_screen(self, screen_name):
        self.screen_stack.append(self.current)
        self.transition.direction = "left"
        self.current = screen_name

    def pop_screen(self):
        screen_name = self.screen_stack[-1]
        del self.screen_stack[-1]
        self.transition.direction = "right"
        self.current = screen_name
