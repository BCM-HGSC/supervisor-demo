#!/usr/bin/env python3

from os import getpid
from signal import pause, signal, SIGABRT, SIGALRM, SIGINT, SIGTERM
from sys import argv, stdout
from time import sleep

SLEEP_TIME = 3

name = argv[1]
running = True

def out(*args, **kwds):
    print(*args, **kwds)
    stdout.flush()

out(name)
out(getpid())

def start_shutdown(signum, frame):
    global running
    out(f'signal {signum}, halting')
    running = False

def print_signal(signum, frame):
    out(f'signal {signum}')

signal(SIGABRT, start_shutdown)
signal(SIGINT, start_shutdown)
signal(SIGTERM, start_shutdown)

signal(SIGALRM, print_signal)

if name.endswith('_p'):
    out('paused')
    pause()

while running:
    out(f'job {name}')
    sleep(SLEEP_TIME)

out('done')
