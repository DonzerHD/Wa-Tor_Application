import random as rd

class Fish:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape = None # Ajout de l'attribut shape
        self.nombre_reproduction = 4
        
    def move(self, world):
        old_x = self.x
        old_y = self.y
        # Génère une liste de positions possibles pour le poisson de se déplacer
        possible_positions = self.verification_move(world)
        #Si il y a des positions possibles pour le poisson de se déplacer
        if len(possible_positions) > 0:
            # Choisit aléatoirement une position de la liste possible_positions
            new_pos = rd.choice(possible_positions)
            # Met à jour la grille en enlevant le poisson de sa position actuelle
            # Met à jour les coordonnées du poisson
            self.x = new_pos[0]
            self.y = new_pos[1]
            # Met à jour la grille en ajoutant le poisson à sa nouvelle position
        return old_x , old_y
    
    def verification_move(self, world):
        # Initialise une liste de positions possibles pour le poisson de se déplacer
        possible_positions = []
        #Boucle à travers les déplacements possibles pour le poisson (dx et dy peuvent prendre les valeurs -1, 0, 1)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Calcul les nouvelles coordonnées du poisson en utilisant l'opérateur modulo pour s'assurer 
                # qu'elles restent dans les limites de la grille en bouclant sur les bords
                x = (self.x + dx) % world.rows
                y = (self.y + dy) % world.cols 
                # Vérifie si la case cible ne contient pas un requin ou un autre poisson
                if world.is_empty(x, y):
                    # Ajoute les coordonnées de la case cible à la liste de positions possibles
                    possible_positions.append((x, y))
        # Retourne la liste de positions possibles
        return possible_positions
           
    def reproduction(self, world, old_x , old_y,day):
        if world.is_empty(old_x, old_y):
            if day % self.nombre_reproduction == 0:
                new_fish = Fish(old_x, old_y)
                world.add_fish(new_fish)