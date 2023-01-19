from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

# Pong game made with python kivy
# Can be played on desktop and mobile 

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()
