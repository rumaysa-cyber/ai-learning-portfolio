# Prompts user to choose an animal type:

print("Please choose an animal from the types: mammal, bird, or fish")

# Three categories to distinguish between animal types: can_swim, has_feathers, and has_hair
# Knowledge-gathering for can_swim, has_feathers, and has_hair starts here:

q0 = input("Can your animal swim? yes/no: ")

if q0 == "yes":
  can_swim = True
else:
  can_swim = False

q1 = input("Does your animal have feathers? yes/no: ")

if q1 == "yes":
  has_feathers = True
else:
  has_feathers = False

q2 = input("Does your animal have hair? yes/no: ")

if q2 == "yes":
  has_hair = True
else:
  has_hair = False


# Reasoning code starts here:

if can_swim and not has_hair and not has_feathers:
  print("Your animal is a fish!")
elif has_feathers and not has_hair:
  print("Your animal is a bird!")
elif has_hair and not has_feathers:
  print("Your animal is a mammal!")
else:
  print("Sorry, I don't know your animal type!")
