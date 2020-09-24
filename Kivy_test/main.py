from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton


class KivyApp(MDApp):

    def build(self):
        screen = Screen()
        drukknop = MDRectangleFlatButton(text='button', pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                         on_press=self.ingeduwd)
        screen.add_widget(drukknop)
        return screen

    def ingeduwd(self, instance):
        print("Ingeduwd")


if __name__ == '__main__':
    app = KivyApp()
    app.run()
