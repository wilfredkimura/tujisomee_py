from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from playsound import playsound

class Tujisomee(App):
    def build(self):
        self.label = Label(text="Hello, User!")
    
        btn = Button(text="Play Sound")
        btn.bind(on_press=self.on_button_click)

        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(self.label)
        layout.add_widget(btn)

        return layout

    def on_button_click(self, instance):
        playsound("./mp3/a.mp3")   
    
    
    





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
