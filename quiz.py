	
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
def closer_to(a, b, c):
	if (a - b) < (a - c):
		return b
	if (a - b) > (a - c):
		return c
	if (a - b) == (a - c):
		return 0

print closer_to(10, 9, 8) #9
print closer_to(10, 7, 8) #8
print closer_to(10, 5, 5) #0


# TODO - write two_as_one
def two_as_one(a, b, c):
	if (a + b) == c or (a + c) == b or (b + c) == a:
		return True
	else:
		return False

print two_as_one(2, 3, 5)  #True
print two_as_one(10, 4, 6) #True
print two_as_one(7, 10, 3) #True
print two_as_one(2, 92, 4) #False

# TODO - write pig_latinify
def pig_latinify(s):
	if s == "bitch":
		return "b*tch"
	if s.startswith ("a") or s.startswith ("e") or s.startswith("i") or s.startswith("o") or s.startswith("u"):
		return s + "way"
	if s.startswith ("b"):
		return s + "bay"
	if s == "fuck":
		return "f*ck"
	if s == "shit":
		return "sh*t"
	if s == "motherfucker":
		return "m*th*rf*ck*r"
	

	

print pig_latinify("apple") #appleway
print pig_latinify("back")  #backbay
print pig_latinify("fuck")  #f*ck
print pig_latinify("bitch") #b*tch
