class Fish():
	def __init__(self, internal_timer_value):
		self._timer = internal_timer_value

	def next_day(self):
		ret = self._timer == 0
		self._timer = self._timer-1 if self._timer != 0 else 6
		return ret

class FishPopulation():
	def __init__(self, file_name):
		with open(file_name, 'r') as f:
			data = f.read()

		self._initial_timers = [int(i) for i in data.split(',')]

		self._fishes = list()
		self.create_fishes()

	def create_fishes(self):
		self._fishes = [Fish(timer_value) for timer_value in self._initial_timers]

	def increment_days(self, number_of_days):
		for i in range(0, number_of_days):
			for fish in self._fishes:
				create_new_fish = fish.next_day()		
				if create_new_fish:
					self._fishes.append(Fish(9))
		return

	def fish_count(self):
		return len(self._fishes)
					


fishes = FishPopulation("data.txt")
fishes.increment_days(256)
print(fishes.fish_count())