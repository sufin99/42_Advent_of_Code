import time
import tkinter as tk
from PIL import Image, ImageTk

with open('acertijo6.txt', 'r') as file:
	mapa = [list(line.strip()) for line in file.readlines()]

for y, fila in enumerate(mapa):
	for x, celda in enumerate(fila):
		if (celda == '^'):
			pos_x, pos_y = x, y
			break

"""root = tk.Tk()
root.title("Cueva Celeste")

img_fondo = ImageTk.PhotoImage(Image.open("img/fondo.PNG"))
img_personaje_up = ImageTk.PhotoImage(Image.open("img/personaje_up.PNG"))
img_personaje_down = ImageTk.PhotoImage(Image.open("img/personaje_down.PNG"))
img_personaje_left = ImageTk.PhotoImage(Image.open("img/personaje_left.PNG"))
img_personaje_right = ImageTk.PhotoImage(Image.open("img/personaje_right.PNG"))
img_obstaculo = ImageTk.PhotoImage(Image.open("img/obstaculo.PNG"))
img_pintado = ImageTk.PhotoImage(Image.open("img/pintado.PNG"))

canvas = tk.Canvas(root, width=len(mapa[0]) * 32, height=len(mapa) * 32)
canvas.pack()"""

def imprimir_mapa(mapa, pos_x, pos_y):
	"""canvas.delete("all")"""
	for y, fila in enumerate(mapa):
		for x, celda in enumerate(fila):
			if (x == pos_x and y == pos_y):
				print('^', end='')
			else:
				print(celda, end='')
		print()
	print()
	"""if (celda == '#'):
				canvas.create_image(x * 32, y * 32, image=img_obstaculo, anchor=tk.NW)
			elif (celda == 'X'):
				canvas.create_image(x * 32, y * 32, image=img_pintado, anchor=tk.NW)
			else:
				canvas.create_image(x * 32, y * 32, image=img_fondo, anchor=tk.NW)
	if (direccion == 'U'):
		img_personaje = img_personaje_up
	elif (direccion == 'D'):
		img_personaje = img_personaje_down
	elif (direccion == 'L'):
		img_personaje = img_personaje_left
	elif (direccion == 'R'):
		img_personaje = img_personaje_right
	canvas.create_image(pos_x * 32, pos_y * 32, image=img_personaje, anchor=tk.NW)
	root.update()"""

def mover_personaje(mapa, pos_x, pos_y, direccion):
	if (mapa[pos_y][pos_x] == '.' or mapa[pos_y][pos_x] == '^'):
		mapa[pos_y][pos_x] = 'X'
		return (True, pos_x, pos_y, direccion)
	if (direccion == 'U'):
		if (pos_y > 0 and mapa[pos_y - 1][pos_x] in ['.', 'X']):
			pos_y -=1
		else:
			direccion = 'R'
	elif (direccion == 'R'):
		if (pos_x < len(mapa[0]) - 1 and mapa[pos_y][pos_x + 1] in ['.', 'X']):
			pos_x += 1
		else:
			direccion = 'D'
	elif (direccion == 'D'):
		if (pos_y < len(mapa) - 1 and mapa[pos_y + 1][pos_x] in ['.', 'X']):
			pos_y += 1
		else:
			direccion = 'L'
	elif (direccion == 'L'):
		if (pos_x > 0 and mapa[pos_y][pos_x - 1] in ['.', 'X']):
			pos_x -= 1
		else:
			direccion = 'U'
	return (False, pos_x, pos_y, direccion)

direccion = 'U'
count_X = 0

while (True):
	"""imprimir_mapa(mapa, pos_x, pos_y)"""
	pintado, pos_x, pos_y, direccion = mover_personaje(mapa, pos_x, pos_y, direccion)
	if (pintado):
		count_X += 1
	"""time.sleep(0.5)"""

	if (pos_x == 0 or pos_x == len(mapa[0]) - 1 or pos_y == 0 or pos_y == len(mapa) - 1):
		mapa[pos_y][pos_x] = 'X'
		count_X += 1
		imprimir_mapa(mapa, pos_x, pos_y)
		print("Saliste de la Cueva Celeste")
		print(f"Has pintado {count_X} veces")
		break

"""root.mainloop()"""