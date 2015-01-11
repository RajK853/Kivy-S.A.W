from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class mainWidget(BoxLayout):

	Config.set("graphics", "height", "600")
	Config.set("graphics", "width", "600")
	Config.set("graphics",  "resizable", "1")
	Config.write()
	def __init__(self, **kwargs):
		super(mainWidget, self).__init__(**kwargs)
		self.add_widget(Label(text="Your graphical settings has been restored!", color=(0.2, 0.6, 0.2, 0.8), font_size=24))

class mainApp(App):
	def build(self):
		return mainWidget()

if __name__ == "__main__":
	mainApp().run()