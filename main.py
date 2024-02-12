# imoprts
import tkinter as tk
from tkinter import ttk
import sympy as sp
from sympy import *
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import Limes

# funktion plotten
def plot(expr, x_range=(-10, 10), num_points=400):
   x = symbols('x')
   f = sp.lambdify(x, expr, 'numpy')
   x_v = np.linspace(x_range[0], x_range[1], num_points)
   y_v = f(x_v)
   figure = plt.figure(figsize=(6, 4))
   plot = figure.add_subplot(1, 1, 1)
   plot.clear()
   plot.plot(x_v, y_v,color='blue')
   plot.grid(True)
   plot.axhline(0, color='black',linewidth=0.5)
   plot.axvline(0, color='black', linewidth=0.5)
   return figure

def calc():
    expr = sp.sympify(formel.get())
    gegen = Limes.filter(geg.get())
    s_grenz = str(seite.get())
    if gegen == -math.inf:
        loesung.config(text="Der Grenzwert von {} fuer x gegen {} ist: -{}".format(expr, gegen, Limes.limes(Limes.func_return, gegen, s_grenz, expr)))
    else:
        loesung.config(text="Der Grenzwert von {} fuer x gegen {} ist: {}".format(expr, gegen, Limes.limes(Limes.func_return, gegen,s_grenz,expr)))
    

    #plot
    figure = plot(expr)
    canvas = FigureCanvasTkAgg(figure, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
# Mod for the window
root.title("Limes Rechner")
root.geometry("800x800")

#label1
label1 = ttk.Label(root, text="Bitte geben sie ihre formel f(x) an: f(x) =")
label1.pack()

# Entry fuer die forme
formel = ttk.Entry(root)
formel.pack()
formel.insert(0, "Bsp. 3*x^2")

# Label1
label2 = ttk.Label(root, text="Bitte geben sie den wert an gegen den die funktion laufen soll (-inf = -unendlich, inf = unendlich)")
label2.pack()

# Entry fuer gegen welchen wert die funktion laufen soll
geg = ttk.Entry(root)
geg.pack()

# label3
label3 = ttk.Label(root, text="geben sie die seite an von der der Grenzwert Berechnet werden soll (beide, rechts, links): ")
label3.pack()

# Entry fuer die seite
seite = ttk.Entry(root)
seite.pack()

# Button zum Berechen
btn_fomel = ttk.Button(root, text="submit", command=calc)
btn_fomel.pack()

# label solution
loesung = ttk.Label(root, text="")
loesung.pack()

root.mainloop()

