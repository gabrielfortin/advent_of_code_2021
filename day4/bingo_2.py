from pprint import pprint

with open("data.txt", 'r') as f:
    lines = f.readlines()

drawn_numbers = lines[0].strip('\n').split(",")
drawn_numbers = [int(i) for i in drawn_numbers]

boards = list()

boards_data = lines[1:]

for index in range(0, len(boards_data)):
    if boards_data[index] == "\n":
        new_entry = list()
        for entry in boards_data[index+1:index+6]:
            mod_entry = entry.strip('\n')
            if mod_entry[0] == " ":
                mod_entry = mod_entry[1:]
            mod_entry = mod_entry.replace('  ', ',')
            mod_entry = mod_entry.replace(' ', ',')
            mod_entry = mod_entry.split(",")
            mod_entry = [int(i) for i in mod_entry]
            
            new_entry.append(mod_entry)

        boards.append(new_entry)

class Board():
    def __init__(self, board_data):
        self._board_data = board_data
        self._size = len(board_data)
        self._marked_matrix = [[] for i in range(0, self._size)]
        for i in range(0, self._size):
            self._marked_matrix[i] = [False for i in range(0, self._size)]
        self._steps_for_bingo = 0
        self._bingo = False
        self._last_called_number = None

    def play_bingo(self, numbers, pretty=True):
        for number in numbers:
            ret = self.input_number(number, pretty)
            if ret is not False:
                print(ret)
                return ret
                break

    def input_number(self, number, pretty=True):
        self._steps_for_bingo += 1
        for i in range(0, len(self._board_data)):
            for j in range(0, len(self._board_data[i])):
                if number == self._board_data[i][j]:
                    self._marked_matrix[i][j] = True
        self._check_for_bingo()

        if self._bingo and pretty:
            self._last_called_number = number
            return "Bingo with {0} steps".format(self._steps_for_bingo)
        elif self._bingo:
            self._last_called_number = number
            return self._steps_for_bingo
        else:
            return False

    def _check_for_bingo(self):
        self._bingo = False
        for i in range(0, self._size):
            if sum(self._marked_matrix[i]) == self._size:
                self._bingo = True

        for i in range(0, self._size):
            col = [row[i] for row in self._marked_matrix]
            if sum(col) == self._size:
                self._bingo = True

        return self._bingo

    def calculate_score(self):
        score_sum = 0
        for i in range(0, self._size):
            for j in range(0, self._size):
                if not self._marked_matrix[i][j]:
                    score_sum += self._board_data[i][j]
        final_score = score_sum * self._last_called_number
        return final_score

max_step = 0
max_board = None          
for board_data in boards:
    board_obj = Board(board_data)
    steps = board_obj.play_bingo(drawn_numbers, False)
    
    if (steps > max_step):
        max_step = steps
        max_board = board_obj

print(max_board.calculate_score())