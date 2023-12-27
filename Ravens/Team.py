class Player:
    def __init__(self, name, jersey, size, pos):
        self.name = name
        self.jersey = jersey
        self.size = size
        self.pos = pos
    
Varun = Player("Varun", 10, "M", "F")
Aaryan = Player("Aaryan", 7, "M", "M")
Ayush = Player("Ayush", 22, "XXL", "D")
Arush = Player("Arush", 24, "XXL", "M")



players = [Varun, Aaryan, Ayush, Arush]

for player in players:
    # print(f"{player.name} {player.jersey} {player.size}")
    if (player.pos == 'M'):
        print(player.name)