with open("data.txt", "r") as f:
	data = f.readlines()

data = [i.strip("\n") for i in data]


class Line():
	def __init__(self, line_data):
		def parse_coord(data, i, j):
			return int(data[i].split(',')[j].strip(' '))
		
		coords = line_data.split('->')
		self.x0 = parse_coord(coords, 0, 0)
		self.y0 = parse_coord(coords, 0, 1)

		self.xf = parse_coord(coords, 1, 0)
		self.yf = parse_coord(coords, 1, 1)

		self.p0 = (self.x0, self.y0)
		self.pf = (self.xf, self.yf)

	def touched_points(self):
		touched_points = list()
		if self.x0 == self.xf:
			if self.y0 < self.yf:
				touched_ys = list(range(self.y0, self.yf+1))
			else:
				touched_ys = list(range(self.yf, self.y0+1))

			touched_points = [(self.x0, touched_y) for touched_y in touched_ys]

		elif self.y0 == self.yf:
			if self.x0 < self.xf:
				touched_xs = list(range(self.x0, self.xf+1))
			else:
				touched_xs = list(range(self.xf, self.x0+1))
			
			touched_points = [(touched_x, self.y0) for touched_x in touched_xs]

		else:
			pass
				
		return touched_points

class Field():
	def __init__(self, data):
		self._touched_points = dict()
		self._lines = list()
		for entry in data:
			self._lines.append(Line(entry))
	
	def touched_points(self):
		self._touched_points = dict()
		for line in self._lines:
			for touched_point in line.touched_points():
				if touched_point not in self._touched_points:
					self._touched_points[touched_point] = 0
				self._touched_points[touched_point] += 1

		return self._touched_points

	def points_that_overlap(self):
		count = 0
		for point, touched_count in self.touched_points().items():
			if touched_count > 1:
				count += 1

		return count		

field = Field(data)
print(field.points_that_overlap())