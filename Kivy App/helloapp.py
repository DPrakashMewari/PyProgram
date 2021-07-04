import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        # Add coloumns
        self.window.cols = 1
        # Resize margin padding or size pos
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {'center_x':0.5,"center_y":0.5}
        # Add Image
        self.window.add_widget(Image(source="one.png"))
        # Add one label
        self.greeting = Label(text="What is Your Name?",font_size=19,color="#FF2F02")
        self.window.add_widget(self.greeting)
        # text input widget
        self.user = TextInput(multiline=False,padding_y=(21,21),size_hint=(1,0.5))
        self.window.add_widget(self.user)
        # Add button
        self.button = Button(text="Greet",size_hint=(1,0.5),bold=True,background_color="#FF2F02")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        return self.window

    def callback(self,instance):
        self.greeting.text = "Hello" +" "+ self.user.text + "!"

if __name__ == "__main__":
    SayHello().run()

