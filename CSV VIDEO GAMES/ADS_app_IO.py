import csv
import os

class championRecord:
    def __init__(self, nombre, vida, damage, tipo):
        self.name = nombre
        self.life = vida
        self.damage = damage
        self.type = tipo

class DynamicArray:
    def __init__(self):
        self.Champs = []
        self.size = 0

    def tank(self,nombre):
        for i in range(self.size):
            if self.Champs[i].name == nombre:
                if self.Champs[i].life > 3999:
                    return print(f"The camp: {nombre} IS a tank")
                else:
                    return print(f"The camp: {nombre} IS NOT a tank")
                
    def fighter(self,nombre):
        for i in range(self.size):
            if self.Champs[i].name == nombre:
                if self.Champs[i].life > 1900 and self.Champs[i].life <=2500:
                    return print(f"The camp: {nombre} IS a fighter")
                else:
                    return print(f"The camp: {nombre} IS NOT a fighter")
                
    def assassin(self,nombre):
        for i in range(self.size):
            if self.Champs[i].name == nombre:
                if self.Champs[i].damage >= 700:
                    return print(f"The camp: {nombre} IS an assassin")
                else:
                    return print(f"The camp: {nombre} IS NOT an assassin")
                     
    def contains(self, nombre):
        for champ in self.Champs:
            if champ.name == nombre:
                return True
        return False    

    def add_champ(self, nombre, vida, damage, tipo):
        if self.contains(nombre):
            print(f"{nombre} ya esta en la lista.")
            return
        factor = championRecord(nombre, vida, damage, tipo)
        self.Champs.append(factor)
        self.size += 1

    def get_champ(self, index):
        if 0 <= index < self.size:
            champ = self.Champs[index]
            return champ.name, champ.life, champ.damage, champ.type
        else:
            raise IndexError("Index out of range")

    def remove_champ(self, index):
        if 0 <= index < self.size:
            self.Champs.pop(index-1)
            self.size -= 1
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return self.size

    def __str__(self):
        return '\n'.join([f"{champ.name}: {champ.life}, {champ.damage}, {champ.type}" for champ in self.Champs])

def read_csv():
    champsList = DynamicArray()
    path = os.path.dirname(__file__)    
    file_path = os.path.join(path, 'League_of_graphs.csv')

    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            # next(csv_reader)  
            for row in csv_reader:
                if len(row) >= 4:
                    try:
                        vida = int(row[1])
                        damage = int(row[2])
                        champsList.add_champ(row[0], vida, damage, row[3])
                    except ValueError:
                        print(f"Invalid data in row: {row}")
    else:
        print("File not found")

    return champsList

# Hora de las cosas RICAS
my_champs = read_csv()
my_champs.add_champ("Lulu", 500, 1200, "SP")
my_champs.add_champ("Ashe", 600, 1500, "AD")
my_champs.tank("Arhi")
#my_champs.fighter("Irelia")
#my_champs.assassin("Shaco")
# my_champs.remove_champ(4)

print("\nLista actual de campeones:")
print(my_champs)

