#!/usr/bin/python

from curses import wrapper
import time
import Malla
import archivo_noe




def graficar(stdscr):
	fila=5
	columna=5
	m = Malla.Malla(fila,columna)
	m.celulaViva(2,2)
	m.celulaViva(2,4)
	m.celulaViva(3,3)
	# Clear screen
	interacciones=2
	while interacciones>0:
		stdscr.clear()
		for i in range(1,fila+1):
			for j in range (1,columna+1):
				stdscr.addstr(i, j, m.valorCelula(i,j))
		#time.sleep(2)
		m=archivo_noe.NuevaMatriz(m.mallaCompleta())
		interacciones=interacciones-1
		stdscr.refresh()
		stdscr.getkey()

wrapper(graficar)


