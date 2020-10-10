from subprocess import Popen, PIPE


def run(scr):
    try:
        command = ['osascript', '-e %s' % scr]
        lines = []
        with Popen(command, stdout=PIPE, universal_newlines=True) as process:
            for line in process.stdout:
                lines.append(line)
        return lines

    except Exception as e:
        return e
