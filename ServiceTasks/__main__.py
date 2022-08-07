from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello World", halign="center")


def main():
    MainApp().run()


if __name__ == "__main__":
    main()
