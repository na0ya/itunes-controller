# iTunes controlle for dictation.
import sublime, sublime_plugin
import sys
import Pywin32.setup

platform = sys.platform
if platform == "win32":
	import win32com.client
else:
	from Foundation import *
	from ScriptingBridge import *

class InitializeApps(object):
	def __init__(self):
		if platform == "win32":
			self.itunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
		else:
			self.itunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

	def get_connection(self):
		return self.itunes

class itunesMoveNextCommand(sublime_plugin.TextCommand):
	def run(view, edit):
		app = InitializeApps().get_connection()
		if platform == "win32":
			app.NextTrack()
		else:
			app.nextTrack()

class itunesMovePreviousCommand(sublime_plugin.TextCommand):
	def run(view, edit):
		app = InitializeApps().get_connection()
		if platform == "win32":
			app.PreviousTrack()
		else:
			app.previousTrack()

class itunesPauseCommand(sublime_plugin.TextCommand):
	def run(view, edit):
		app = InitializeApps().get_connection()
		if platform == "win32":
			app.Playpause()
		else:
			app.playpause()

class itunesRewindCommand(sublime_plugin.TextCommand):
	def run(view, edit):
		app = InitializeApps().get_connection()
		if platform == "win32":
			app.PlayerPosition = iTunes.PlayerPosition - 15;
		else:
			app.playerPosition = iTunes.playerPosition - 15;

class itunesFastforwardCommand(sublime_plugin.TextCommand):
	def run(view, edit):
		app = InitializeApps().get_connection()
		if platform == "win32":
			app.PlayerPosition = iTunes.PlayerPosition + 15;
		else:
			app.playerPosition = iTunes.playerPosition + 15;
