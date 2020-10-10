import myosascript

TMPL = 'tell application "System Events" to %s'
TMPL_K = 'tell application "System Events" to key code %s'
TMPL_KS = 'tell application "System Events" to keystroke %s'


def unlock():
    myosascript.run(TMPL % 'click at {0, 0}')
    myosascript.run(TMPL_KS % '2002')
    myosascript.run(TMPL_K % '76')


def set_input_volume(val):
    myosascript.run('set volume input volume %s' % val)
