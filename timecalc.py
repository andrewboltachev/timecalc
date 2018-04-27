import code
import readline
import atexit
import os
import rlcompleter
import re
import argparse

parser = argparse.ArgumentParser(description='Simple time calculator.')
parser.add_argument('--real', action='store_true')
real = parser.parse_args()

historyPath = os.path.expanduser("~/.timecalc-history")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, historyPath

if real:
    print '"Real calculation" mode: would "shift" negative values and ones more than 24h'

x = ''
while x not in ['q']:
    try:
        x = raw_input(">>> ")
    except EOFError:
        print ''
        break
    if x != '':
        matchobj = re.match(r'^([-]?[0-9]+:[0-9][0-9])([-+][0-9]+:[0-9][0-9])*$', x)
        if matchobj:
            a = re.findall(r'[+-]?[-]?[0-9]+:[0-9][0-9]', x)
            s = 0
            for t in a:
                neg = -1 if t.find('-') != -1 else 1
                t = t.replace('+', '').replace('-', '')
                t = t.split(':')
                h = int(t[0])
                m = int(t[1])
                s += neg * (m + h * 60)
            MINUTES_IN_DAY = 24 * 60
            if real:
                while s >= MINUTES_IN_DAY:
                    s -= MINUTES_IN_DAY
                while s < 0:
                    s += MINUTES_IN_DAY
            r = ''
            r += '-' if s < 0 else ''
            s = abs(s)
            h, m = divmod(s, 60)
            h = '%d' % h
            r += h
            r += ':'
            m = '%d' % m
            m = ('0' if len(m) < 2 else '') + m
            r += m
            print r
        else:
            print 'Err'
