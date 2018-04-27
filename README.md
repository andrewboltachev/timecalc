timecalc
========

Simple time calculator in Python

Usage example (standard mode):
`````
[andrey@archer ~]$ python2 timecalc.py
>>> 10:10+11:11
21:21
>>> 12:00+10:15-5:05
17:10
>>> 12:00+10:15
22:15
>>> 
`````

"Real calculation" mode (useful to calculate timezone shifts):
`````
➜  timecalc git:(master) python timecalc.py --real
"Real calculation" mode: would "shift" negative values and ones more than 24h
>>> 15:00+17:00
8:00
>>> 00:00-23:00
1:00
>>> 
`````
