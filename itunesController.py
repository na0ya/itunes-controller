# iTunes controlle for dictation.
import sublime, sublime_plugin
import sys
import Pywin32.setup

platform = sys.platform
if platform == "win32":
		import win32com.client
		iTunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")
else:
		from Foundation import *
		from ScriptingBridge import *
		iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")


class itunes_move_to_next(sublime_plugin.TextCommand):
	def run(self, edit):
		if platform == "win32":
			iTunes.NextTrack()
		else:
			iTunes.nextTrack()

class itunes_move_to_previous(sublime_plugin.TextCommand):
	def run(self, edit):
		if platform == "win32":
			iTunes.PreviousTrack()
		else:
			iTunes.previousTrack()

class itunes_pause(sublime_plugin.TextCommand):
	def run(self, edit):
		if platform == "win32":
			iTunes.Playpause()
		else:
			iTunes.playpause()

class itunes_back(sublime_plugin.TextCommand):
	def run(self, edit):
		if platform == "win32":
			iTunes.Rewind()
		else:
			iTunes.rewind()

class itunes_fastforward(sublime_plugin.TextCommand):
	def run(self, edit):
		if platform == "win32":
			iTunes.FastForward()
		else:
			iTunes.fastForward()

class itunes_info(sublime_plugin.TextCommand):
	def runt(self, edit):
		ls = dir(iTunes)
		self.view.insert(edit, 50, dir(iTunes))
