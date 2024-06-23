from kivy.uix.screenmanager import ScreenManager


class NavigationScreenManager(ScreenManager):
    screen_stack = []

    def push_screen(self, screen_name):
        self.screen_stack.append(self.current)
        self.transition.direction = "left"
        self.current = screen_name
        print(self.screen_stack)

    def pop_screen(self):
        print(self.screen_stack)
        if self.screen_stack:  # Check if the stack is not empty
            screen_name = self.screen_stack[-1]
            self.transition.direction = "right"
            self.current = screen_name
            self.screen_stack.pop()

        else:
            print("Screen stack is empty. Cannot pop.")
        print(self.screen_stack)