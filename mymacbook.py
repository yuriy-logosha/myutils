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


def get_current_volume(type='output'):
    cmd = 'get volume settings'
    settings = myosascript.run(cmd)
    # assert len(settings) == 1, "Wrong output: %s" % cmd
    # assert type(settings[0]) == str, "Wrong type of: %s" % settings[0]
    # assert len(settings[0].split(', ')) == 4, "Wrong format of: %s" % settings[0].split(', ')
    # assert len(settings[0].split(', ')[0].split(':')) == 2, "Wrong format of: %s" % settings[0].split(', ')[0]
    # assert type(settings[0].split(', ')[0].split(':')[1]) == str, "Wrong type of: %s" % settings[0].split(', ')[0].split(':')[1]
    return int(settings[0].split(', ')[0].split(':')[1]) if type == 'output' else int(
        settings[0].split(', ')[1].split(':')[1]) if type == 'input' else 0
