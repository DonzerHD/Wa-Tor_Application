import tkinter as tk
import random as rd
import time
from Shark import Shark

from World import World
from Fish import Fish


cols = 30
rows = 30

def start_simulation():
    # Initialisation de la simulation
    world = World(cols, rows)
    # ajout du jour et son affichage 
    day = 1
    world.day_label = tk.Label(world.root, text="Jour : "+str(day))
    world.day_label.pack()
    world.root.geometry(str(cols*10) + "x" + str(rows*10))
    for i in range(50):
        world.add_fish(Fish(rd.randint(1, rows - 1), rd.randint(1, cols - 1)))
    for i in range(10):
        world.add_shark(Shark(rd.randint(1, rows - 1), rd.randint(1, cols - 1)))

    # Boucle de mise à jour de la simulation
    while True:
        for shark in world.sharks.copy():
            # Suppression de l'objet graphique actuel du poisson
            world.canvas.delete(shark.shape)
            # Déplacement du poisson
            old_x, old_y = shark.move(world)
            shark.reproduction(world,old_x,old_y,day)
            # Création d'un nouvel objet graphique pour le poisson à sa nouvelle position
            shark.shape = world.canvas.create_rectangle(shark.x*10, shark.y*10, (shark.x*10)+10, (shark.y*10)+10, fill="red")
        for fish in world.fishes.copy():
            # Suppression de l'objet graphique actuel du poisson
             world.canvas.delete(fish.shape)
             # Déplacement du poisson
             old_x, old_y = fish.move(world)
             fish.reproduction(world,old_x,old_y,day)
             # Création d'un nouvel objet graphique pour le poisson à sa nouvelle position
             fish.shape = world.canvas.create_rectangle(fish.x*10, fish.y*10, (fish.x*10)+10, (fish.y*10)+10, fill="yellow")
        world.day_label.config(text="Jour : "+str(day) + "Poissons : "+ str(len(world.fishes)) + "Requins : "+ str(len(world.sharks)))
        day += 1
        world.root.update()
        time.sleep(0.2)

start_simulation()