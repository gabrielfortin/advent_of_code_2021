class Line():
	def __init__(self, line_data):
		def parse_coord(data, i, j):
			return int(data[i].split(',')[j].strip(' '))
		
		coords = line_data.split('->')
		self.x0 = parse_coord(coords, 0, 0)
		self.y0 = parse_coord(coords, 0, 1)

		self.xf = parse_coord(coords, 1, 0)
		self.yf = parse_coord(coords, 1, 1)
	
	def touched_points(self):
		def get_touched_points(init, final, checkX=True):
			touched = list()
			if init < final:
				touched = list(range(init, final+1))
			elif init > final:
				touched = list(range(final, init+1))
				touched.reverse()
			elif init == final:
				end = abs(self.yf-self.y0)+1 if checkX else abs(self.xf-self.x0)+1
				touched = [init for i in range(0, end)]

			return touched
		
		touched_xs = get_touched_points(self.x0, self.xf)
		touched_ys = get_touched_points(self.y0, self.yf, False)

		return [(touched_xs[i], touched_ys[i]) for i in range(0, len(touched_xs))]
	
class Field():
	def __init__(self, file_name):
		with open(file_name, "r") as f:
			data = f.readlines()
		self._lines = [Line(entry) for entry in [i.strip("\n") for i in data]]
		self._touched_points = dict()
	
	def touched_points(self):
		self._touched_points = dict()
		for line in self._lines:
			for touched_point in line.touched_points():
				if touched_point not in self._touched_points:
					self._touched_points[touched_point] = 0
				self._touched_points[touched_point] += 1

		return self._touched_points

	def points_that_overlap(self):
		return sum([touched_count > 1 for point, touched_count in self.touched_points().items()])

field = Field("data.txt")
print(field.points_that_overlap())