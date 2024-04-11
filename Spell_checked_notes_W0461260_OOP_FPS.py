import random

#define weapons
class Weapon:
    def __init__(self,name, damage, ammo):
        self.name = name
        self.damage = damage
        self.ammo = ammo
        self.ammo_remain = ammo

    def shoot(self):
        if self.ammo_remain > 0:
            print(f"{self.name} fired - {self.damage}!")
        else:
            print("Out of ammo!")

#define player
class Player:
    def __init__(self, name,health):
        self.name = name
        self.health = health
        self.weapon = None

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage! Current health: {self.health}")

    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} became equiped with {weapon.name}!")

    def attack(self):
        if self.weapon:
            self.weapon.shoot()
        else:
            print(f"{self.name} has no weapon!")
        

#define the game
class FPS:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def play_round(self):
        print("Open the game!")
        self.player1.attack()
        self.player2.take_damage(shotgun.damage)

        self.player2.attack()
        self.player1.take_damage(assault_rifle.damage)

if __name__ == "__main__":
#Make weapons
    assault_rifle = Weapon("Assault rifle", damage = 10 ,ammo = 30)
    shotgun = Weapon("Shotgun", damage = 30, ammo = 8)
    weapon_list = [assault_rifle, shotgun]    
#create players
    player1= Player("Player 1", health=100)
    player2 = Player("Player 2", health=100)
#equip the players
    player1.equip(assault_rifle)
    player2.equip(shotgun)

    game = FPS(player1, player2)
    game.play_round()



"""
Notes

I got it working after 2 months.
The reason why the program didn't work was because there were too many variables given to the attack and take_damage functions
As well as the attack function itself was using the weapons.shoot function that also had an extra variable given that wasn't needed
"""