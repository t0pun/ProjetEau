import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt, animation


root = tk.Tk()
root.title("La fontaine qui danse")
root.configure(background="#005FF9")


title = tk.Label(root, text="La fontaine qui danse", font=("Serif", 50, "bold"), bg="#005FF9", fg="white")
title.pack(pady=20)


frame = tk.Frame(root, bg="#005FF9")
frame.pack()


values = []
current_values = [0] * 16

def set_value(index, value):
    current_values[index] = value
    print("Value {} set to {}".format(index, current_values[index]))

for i in range(4):
    for j in range(4):
        index = i * 4 + j
        slider = ttk.Scale(frame, from_=0, to=150, orient="horizontal", command=lambda value, index=index: set_value(index, float(value)))
        slider.set(0)
        slider.grid(row=i, column=j, padx=10, pady=10)


def next_step():
    global current_values
    values.append(current_values[:])
    current_values = [0] * 16
    print("Passant au step suivant, current valeurs: {}".format(values))

next_button = tk.Button(root, text="Passer à la prochaine étape", command=next_step)
next_button.pack(pady=10)

fig, ax = plt.subplots()
plt.ylim(0,160)
ax.set_ylim(0, 160)
plt.xlim(0,17)


def update(frame):
    ax.clear()
    ax.set_ylim(0, 160)
    ax.bar(range(16), values[frame])


def show_values():
    print("Tableau final : {}".format(values))
    ani = animation.FuncAnimation(fig, update, frames=len(values), repeat=True,interval=1000)
    plt.show()

show_button = tk.Button(root, text="Simuler", command=show_values)
show_button.pack(pady=10)

root.mainloop()
