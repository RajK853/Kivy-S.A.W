#:kivy 1.8.0
from kivy.app import App                # for main App loop
#from kivy.core.audio import SoundLoader
from kivy.clock import Clock            # for updating the app contents in given intervals
from kivy.properties import NumericProperty, ObjectProperty, StringProperty # for making kivy Numbers and Objects
from kivy.uix.widget import Widget      # for making a custom widget
from kivy.config import Config          # for changing the Kivy's default settings
from kivy.base import EventLoop         # to prevent "Fatal Python error: (pygame parachute) Segmentation Fault"
from random import randint              # for generating a random integer with which the blade will be slowed


class gameWidget(Widget):           # Root Widget
	HEIGHT = 600         # height of the window
	WIDTH = 400         # width of the window

	# Connect objects between Python and Kivy language i.e Main.py and SAW.kv
	blade = ObjectProperty(None)
	victim = ObjectProperty(None)
	progressBar = ObjectProperty(None)

	# change the window's default height, width and resizable options
	Config.set("graphics", "width", str(WIDTH))
	Config.set("graphics", "height", str(HEIGHT))
	if Config.getint("graphics", "resizable") == 1:
		Config.set("graphics", "resizable", "0")
	Config.write()
	EventLoop.ensure_window()

class SAWApp(App):      # main App
	EventLoop.ensure_window()
	slowBlade = NumericProperty(0)      # value to slow down the blade
	progress = NumericProperty(0)       # value for progress bar
	progress_label = StringProperty()   # string to display as the pprogress bar fills
	bladePos = NumericProperty(0)       # blade position
	victimPos = NumericProperty(0)        # victim position
	gameOverAlpha = NumericProperty(0)  # alpha value for game over screen
	winAlpha = NumericProperty(0)       # alpha value for win screen
	width = NumericProperty(gameWidget().WIDTH) # width of window
	height = NumericProperty(gameWidget().HEIGHT)   # height of window

	def update(self, dt):               # update victimPos, bladePos and checks is victim is dead or alive
		# set the slowBlade to random
		self.slowBlade = randint(8, 30)/10
		# change progress bar value at different rate
		if self.progress < 100:
			self.progress_label = "%s %%" % round(self.progress, 2)
			if self.progress <= 10:
				self.progress += 0.2
			else:
				self.progress += 10
		else:
			self.progress_label = "Let's Play the Game"
		# change victim's position at different rate at different positions
		if self.victimPos < 2*self.width/5:
			self.victimPos += 0.5
		elif self.victimPos < self.width:
			self.victimPos += 1.6
		# change blade's position at different rate at different positions
		if self.bladePos < self.height/2:
			self.bladePos += 3
		elif self.bladePos < self.height:
			self.bladePos += 3.6
		# check if the user has won
		if self.victimPos > self.width and self.gameOverAlpha == 0:
			self.winAlpha = 0.3
		# check if the victim died
		if gameWidget().victim.victimDead(gameWidget().blade.center_x, gameWidget().blade.y+50):
			self.gameOverAlpha = 0.3

	def build(self):                        #main app loop
		Clock.schedule_interval(self.update, 1/40)      # update
		return gameWidget()                                 # run root widget

class homePage(Widget):         # make a homepage widget with image, button, label and progressbar widgets
	pass

class Blade(Widget):                # make a widget for blade
	pass

class Victim(Widget):               # make a widget for victim
	# function to check if victim dead
	def victimDead(self, x, y):
		# check if any point around the bottom_mid point of the blade collides with victim
		if self.collide_point(x, y) or self.collide_point(x-10, y+5) or self.collide_point(x+10, y+5) \
				or self.collide_point(x-15, y+10) or self.collide_point(x+15, y+10):
			return True
		return False
	pass

class GameOverScreen(Widget):       # make a canvas widget for game over screen
	pass

class Congratulation(Widget):           # make a canvas widget for win screen
	pass

if __name__ == "__main__":
	SAWApp().run()
