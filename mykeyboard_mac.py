import myosascript

TMPL = 'tell application "System Events" to %s'
TMPL_K = 'tell application "System Events" to key code %s'
TMPL_K_U = 'tell application "System Events" to key code %s using %s'
TMPL_KS = '''
tell application "System Events" to keystroke %s
'''

change_lang_ru = '''
    launch application "System Events"
	delay 0.1
	
	ignoring application responses
		tell application "System Events" to tell process "TextInputMenuAgent"
			click menu bar item 1 of menu bar 2
		end tell
	end ignoring
	do shell script "killall System\\\ Events"
	delay 0.1
	tell application "System Events"
		tell process "TextInputMenuAgent"
			tell menu bar item 1 of menu bar 2
				click menu item "Russian - PC" of menu 1
				delay 0.1
			end tell
		end tell
	end tell
	ignoring application responses
		tell application "System Events" to tell process "TextInputMenuAgent"
			click menu bar item 1 of menu bar 2
		end tell
	end ignoring
	do shell script "killall System\\\ Events"
	delay 0.1
    '''

change_lang_en = '''
    tell application "System Events" to tell process "TextInputMenuAgent"
		tell menu bar item 1 of menu bar 2
			click menu item "U.S." of menu 1
			delay 0.1
		end tell
	end tell
    '''


def press_delete(): myosascript.run(TMPL_K % '51')


def press_down(): myosascript.run(TMPL_K % '125')


def press_up(): myosascript.run(TMPL_K % '126')


def press_left(): myosascript.run(TMPL_K % '123')


def press_right(): myosascript.run(TMPL_K % '124')


def press_enter(): myosascript.run(TMPL_K % '76')


def press_return(): myosascript.run(TMPL_K % '36')


def keystroke(val): myosascript.run(TMPL_KS % '"' + val + '"')


def keystroke_return(): myosascript.run(TMPL_KS % 'return')


def brightness_up(): myosascript.run(TMPL_K_U % ('113', 'function down'))


def brightness_down(): myosascript.run(TMPL_K_U % ('107', 'function down'))


def press_esc(): myosascript.run(TMPL_K % '53')


def press_space(): myosascript.run(TMPL_K % '49')
