import code
import readline
import atexit
import os
import rlcompleter
import re

historyPath = os.path.expanduser("~/.timecalc-history")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, historyPath

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
