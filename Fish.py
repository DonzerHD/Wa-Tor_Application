import random as rd

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = None # Ajout de l'attribut shape
        
    def move(self, world):
        old_x = self.x
        old_y = self.y
        direction = rd.randint(0,3)
        if direction == 0:  # Haut
            self.y -= 1
        elif direction == 1:  # Droite
            self.x += 1
        elif direction == 2:  # Bas
            self.y += 1
        elif direction == 3:  # Gauche
            self.x -= 1
        
        # vérifications limite monde
        if self.x < 0:
            self.x = 0
        if self.x >= world.cols:
            self.x = world.cols - 1
        if self.y < 0:
            self.y = 0
        if self.y >= world.rows:
            self.y = world.rows - 1
            
        return old_x, old_y
            
    def reproduction(self, world, old_x , old_y,day):
        if world.is_empty(old_x, old_y):
            if day % 4 == 0:
                new_fish = Fish(old_x, old_y)
                world.add_fish(new_fish)