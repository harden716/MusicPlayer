"""
1/15/2023 Program: musicPlayerGUI2.py

GUI-based version of the python music player application

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

ALSO NOTE: you MUST install the pygame package by running: pip install pygame
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
from pygame import mixer
from tkinter import PhotoImage
import tkinter.filedialog


class MusicPlayer(EasyFrame):

	# Definition of the __init__() method which is our class constructor
	def __init__(self):
		# Call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Music Player GUI", background = "black", resizable = True)
		# create the heading label 
		self.addLabel(text = "Python Music Player", row = 0, column = 0, columnspan = 3, background = "black", foreground = "#ff7900", sticky = "NESW", font = Font(family = "Impact", size = 28))
		# create a variable and add a label for our image
		self.imageLabel = self.addLabel(text = "", row = 2, column = 0, columnspan = 3, sticky = "NESW", background = "black")
		# load the image into the image label object
		self.image = PhotoImage(file = "music_player.png")
		self.imageLabel["image"] = self.image
		# label, text field, and button to load the music file
		self.addLabel(text = "File :", row = 3, column = 0, background = "black", foreground = "#ff7900", sticky = "W", font = Font(family = "Courier", size = 12, weight = "bold"))
		self.musicFile = self.addTextField(text = "", row = 3, column = 1, width = 50, sticky = "NESW", state = "disabled")
		self.loadButton = self.addButton(text = "Select File", row = 4, column = 1, command = self.loadFile)
		self.loadButton["bg"] = "white"
		self.loadButton["fg"] = "black"
		self.loadButton["bd"] = 12
		self.loadButton["width"] = 18

		# create three buttons for the music player functions
		self.playButton = self.addButton(text = "", row = 5, column = 0, state = "disabled", command = self.playMusic)
		self.playIcon = PhotoImage(file = "start.png")
		self.playButton["image"] = self.playIcon
		self.playButton["bg"] = "white"
		self.playButton["bd"] = 18
		self.playButton["width"] = 90
		
		self.pauseButton = self.addButton(text = "Pause", row = 5, column = 1, state = "disabled", command = self.pauseMusic)
		self.pauseIcon = PhotoImage(file = "pause.png")
		self.pauseButton["image"] = self.pauseIcon
		self.pauseButton["bg"] = "white"
		self.pauseButton["bd"] = 18
		self.pauseButton["width"] = 90
		
		self.resumeButton = self.addButton(text = "Resume", row = 5, column = 2, state = "disabled", command = self.resumeMusic)
		self.resumeButton["bg"] = "white"
		self.resumeIcon = PhotoImage(file = "play.png")
		self.resumeButton["image"] = self.resumeIcon
		self.resumeButton["bd"] = 18
		self.resumeButton["width"] = 90

	# event handling functions for the command buttons

	def loadFile(self):
		# initialize pygame mixer, file dialog window pops up to select a file, filename is displayed in the text field when selected

		fList = [("MP3", "*.mp3")]
		songFile = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
		mixer.init()
		mixer.music.load(songFile)
		self.playButton["state"] = "normal"
		mixer.music.play()
		self.musicFile["state"] = "normal"
		self.pauseButton["state"] = "normal"
		self.musicFile.setText(songFile)

	def playMusic(self):
		# play the loaded music file
		mixer.music.play()
		self.pauseButton["state"] = "normal"
		self.resumeButton["state"] = "disabled"


	def pauseMusic(self):
		# pause the current music file
		mixer.music.pause()
		self.resumeButton["state"] = "normal"
		self.pauseButton["state"] = "disabled"

	def resumeMusic(self):
		# resumes the current music file
		mixer.music.unpause()
		self.resumeButton["state"] = "disabled"
		self.pauseButton["state"] = "normal"

# Definition of the main() method which will establish class objects
def main():
	# Instantiate an object from the class into mainloop()
	MusicPlayer().mainloop()

# Global call to the main() method
main()