	
# TODO - write has_teen
def has_teen(a, b, c):
	if a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >= 13 and c <= 19:
		return True
	else:
		return False
print has_teen(13, 14, 15) #True
print has_teen(12, 13, 20) #True
print has_teen(10, 20, 29) #False

# TODO - write not_string
def not_string(s):
	if s.startswith ("Good"):
		return "Not Good"
	if s.startswith ("Not Good"):
		return "Not Good Not"

print not_string("Good") #Not Good
print not_string("Not Good") #Not Good Not

# TODO - write icy_hot
def icy_hot(a, b):
	if a < 0 and b > 0:
		return True
	if a > 0 and b < 0:
		return True
	else:
		return False

print icy_hot(-1, 101) #True
print icy_hot(101, -1) #True
print icy_hot(50, 60)  #False

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
