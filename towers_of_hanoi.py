'''
def towers(discs):
	tower_1, tower_2, tower_3 = [], [], []
	for disc in range(discs, 0, -1):
		tower_1.append(disc)
	initial_tower_1 = tower_1
	print(tower_1, tower_2, tower_3)
	while tower_2 != initial_tower_1 and tower_3 != initial_tower_1:

print(towers(7))

move the highest value piece possible to a place that supports items
move all pieces to a different stack
move stacks that are n-1, etc as high as the original stack (n)
move all the discs from a to b using c

if one disc, move disc 
if two discs, move top disc to intermediate, then move second disc to destination, then intermediate to destination
if three discs, do two disc procedure, move bottom disc, then repeat two disc with using disc as dest
sublime text, atom, vs code
pycharm
'''

def towers(discs, orig, dest, using):
	statement = 'move {} to {}'
	if discs == 0:
		return
	if discs == 1:
		print(statement.format(orig, dest))
	if discs == 2:
		print(statement.format(orig, using))
		print(statement.format(orig, dest))
		print(statement.format(using, dest))
	if discs >= 3:
		towers(discs-1, orig, dest, using)
		print(statement.format(orig, dest))
		towers(discs-1, using, orig, dest)

towers(4, "A", "C", "B")