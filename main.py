from kivy.app import App
from kivy.uix.label import Label

class Tujisomee(App):
    def build(self):
        return Label(text="Hello, User!")

if __name__ == "__main__":
    Tujisomee().run()

"""
KIVY BOILERPLATE CODE

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        self.label = Label(text="Welcome!")
        self.add_widget(self.label)

        self.button = Button(text="Click Me")
        self.button.bind(on_press=self.on_button_click)
        self.add_widget(self.button)

    def on_button_click(self, instance):
        self.label.text = "Button Clicked!"

class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    MyApp().run()
"""
