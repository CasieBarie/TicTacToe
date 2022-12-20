class Player:
    name = ""
    score = 0
    character = ""
    
    def ask_input(self):
        pos = input("Where does " + self.name + "[" + self.character + "] wants to put his character? \033[1;34m")
        return pos