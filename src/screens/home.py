from kivy.uix.label import Label
from kivy.uix.widget import Widget


class HomeScreen(Widget):
    def say_hello(self):
        print('heyy')


# widgets
class ChooseFile(Widget):
    def on_touch_move(self, touch):
        print("Yeet")
        return super().on_touch_move(touch)
