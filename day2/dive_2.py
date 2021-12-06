
class Submarine():
    def __init__(self, file_name=None):
        self._depth = 0
        self._position = 0
        self._aim = 0
        self._file_name = file_name
        return

    def forward(self, increase):
        self._position += increase
        self._depth += ( self._aim * increase )

    def up(self, increase):
        self._aim -= increase
    
    def down(self, increase):
        self._aim += increase

    def navigate_from_data(self):
        with open(self._file_name, 'r') as f:
            instructions = f.readlines()

        for instruction in instructions:
            method_name = instruction.split(' ')[0]
            increase = instruction.split(' ')[1]
            method_to_call = getattr(self, method_name)
            method_to_call(int(increase))
    
    def calculate(self):
        return self._depth * self._position

    def part_one(self):
        self.navigate_from_data()
        return self.calculate()

submarine = Submarine(file_name="data.txt")
print(submarine.part_one())



