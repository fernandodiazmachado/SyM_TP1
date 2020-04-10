#!/usr/bin/python

from curses import wrapper
import time
from Proyecto_Fer import Malla

def main(stdscr):
	# Clear screen
	fila=3
	columna=3
	m = Malla.Malla(fila,columna)
	#m.celulaMuerta(1,1)
	m.celulaMuerta(2,2)
	#m.celulaMuerta(1,3)
	m.mostrarMallaCompleta()
	time.sleep(3)
	stdscr.clear()
	for i in range(1,fila+1):
		for j in range (1,columna+1):
			stdscr.addstr(i, j, m.valorCelula(i,j))

	stdscr.refresh()
	stdscr.getkey()

wrapper(main)
