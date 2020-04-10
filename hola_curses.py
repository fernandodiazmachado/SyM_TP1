#!/usr/bin/python

from curses import wrapper

def main(stdscr):
	# Clear screen
	stdscr.clear()
	
	s = "Hola curses"	
	for i in range(len(s)):
		stdscr.addstr(i, i, s[i])

	stdscr.refresh()
	stdscr.getkey()

wrapper(main)
