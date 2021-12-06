from datetime import datetime
date_start = datetime.now()

days = 80
incubation = 6
max_number_of_incubation = int(days / incubation)


with open("data.txt", 'r') as f:
	data = f.read()
fishes_init = [int(i) for i in data.split(',')]

fish_count = len(fishes_init)

def number_of_descendants(x, day):
	def day_born(i):
		return day + 1 + x + 7*i
		
	number_of_eggs = int(days/(x+max_number_of_incubation))
	if number_of_eggs > max_number_of_incubation:
		number_of_eggs = max_number_of_incubation
	
	new_fishes_born = [day_born(i) for i in range(0,number_of_eggs+1) if day_born(i) <= days]
	
	global fish_count
	fish_count += (len(new_fishes_born))
	
	for new_fish in new_fishes_born:
		number_of_descendants(8, new_fish)
		
	return fish_count

for fish in fishes_init:
	number_of_descendants(fish, 0)
print("Fish count {0}".format(fish_count))

print(datetime.now()-date_start)

