# Prompts user to input data, to stop inputting user must enter "QUIT":

print("Please input data items. Enter QUIT to stop inputting.")

# Gather raw data:

data = []

# Add items to data list until the user enters QUIT

quit = False 
while not quit:
  item = input("Enter an item: ")
  if item == "QUIT":
    quit = True 
  else:
    data.append(item)

print("Raw data:", data)

# Process the data:

processed_data = {}
for item in data:
  # clean the item
  item = item.lower().strip()

  if item in processed_data.keys():
    # Increase the value at the item's key by 1 if item already in dictionary
    processed_data[item] += 1
  else:
    # Otherwise, add the item with a value of 1
    processed_data[item] = 1

print("Processed data: ", processed_data)
