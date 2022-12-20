from box import Box

class Field:
    board = []
    winPossibilities = [
        #vertical
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        #horizontal
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        #diagonal
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]],
    ]

    sizeX = 3
    sizeY = 3
    
    def __init__(self):
        self.board = []
        for x in range(0,self.sizeX):
            for y in range(0, self.sizeY):
                self.board.append(Box(x, y, " "))
    
    def print_board(self):
        #X
        for x in range(0, self.sizeX):
            #setup line
            line = ""
            #Y
            for y in range(0, self.sizeY):
                #Add value to our line
                line += "[" + self.op_coord(x, y).value + "]"
            #Print line
            print(line)

    def use_input(self, pos, char):
        #Split position by ','
        raw = pos.split(",")
        #Get field with x and y and give value
        self.op_coord(raw[1], raw[0]).value = char

    def validate_input(self, pos):
        if pos == "0,0" or pos == "0,1" or pos == "0,2" or pos == "1,0" or pos == "1,1" or pos == "1,2" or pos == "2,0" or pos == "2,1" or pos == "2,2":
            coord = pos.split(",")
            field = self.op_coord(coord[1], coord[0]).value
            #Check if it equals “ “
            return False if field != " " or field == None else True
        else:
            return False

    def op_coord(self, x, y):
        try:
            for i in range(0, len(self.board)):
                if int(self.board[i].posX) == int(x) and int(self.board[i].posY) == int(y):
                    return self.board[i]
            return Box(-1, -1, None)
        except:
            return Box(-1, -1, None)

    def get_winner(self):
        for i in range(0, len(self.winPossibilities)):
            pos1 = self.op_coord(self.winPossibilities[i][0][0], self.winPossibilities[i][0][1]).value
            pos2 = self.op_coord(self.winPossibilities[i][1][0], self.winPossibilities[i][1][1]).value
            pos3 = self.op_coord(self.winPossibilities[i][2][0], self.winPossibilities[i][2][1]).value
            if pos1 == pos2 and pos2 == pos3 and pos3 == pos1:
                return pos1
        return None

    def get_draw(self):
        amount = 0
        for i in range(0, len(self.board)):
            if self.op_coord(self.board[i].posX, self.board[i].posY).value != " ":
                amount = amount + 1
        if amount == 9:
            return "draw"