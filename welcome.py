from player import Player

class Welcome:
    #logo
    def logo(self):
        print("\033[1;33m _____ _     _____         _____ \n|_   _(_) __|_   _|_ _  __|_   _|__   ___ \n  | | | |/ __|| |/ _` |/ __|| |/ _ \ / _ \ \n  | | | | (__ | | (_| | (__ | | (_) |  __/ \n  |_| |_|\___||_|\__,_|\___||_|\___/ \___|")
        #wachten op enter
        input("\n\033[0;37mPress Enter to start.. ")
    
    #informatie
    def info(self):
        print("To win, of course, you have to get 3 in a row. To put your character in a box you have to enter the coordinate of the box. You do this as follows: X,Y where X is horizontal and Y vertical.\nYou can only enter 0, 1 or 2. This means that with, for example, 1,2 your character will be in the bottom center.")
        #wachten op Enter
        input("\nPress Enter to continue..")