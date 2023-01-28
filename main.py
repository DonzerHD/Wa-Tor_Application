import tkinter as tk
import random as rd
import time

from World import World
from Shark import Shark
from Fish import Fish


cols = 50
rows = 50

def start_simulation():
    # Initialisation de la simulation
    world = World(cols, rows)
    # ajout du jour et son affichage 
    day = 1
    world.day_label = tk.Label(world.root, text="Jour : "+str(day))
    world.day_label.pack()
    for i in range(10):
        world.add_fish(Fish(rd.randint(1, rows - 1), rd.randint(1, cols - 1)))

    # Boucle de mise à jour de la simulation
    while True:
        for fish in world.fishes.copy():
            # Suppression de l'objet graphique actuel du poisson
            world.canvas.delete(fish.shape)
            # Déplacement du poisson
            old_x, old_y = fish.move(world)
            fish.reproduction(world,old_x,old_y,day)
            # Création d'un nouvel objet graphique pour le poisson à sa nouvelle position
            fish.shape = world.canvas.create_rectangle(fish.x*10, fish.y*10, (fish.x*10)+10, (fish.y*10)+10, fill="yellow")
            world.day_label.config(text="Jour : "+str(day) + "Poissons : "+ str(len(world.fishes)))
        day += 1
        world.root.update()
        time.sleep(0.6)

start_simulation()