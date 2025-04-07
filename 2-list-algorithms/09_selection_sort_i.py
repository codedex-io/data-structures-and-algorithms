# Selection Sort 📶
# Codédex

my_list = [8, 15, 4, 2]

# Step 1: Write Swap and test it!

def swap(input_list, index_1, index_2):
  temp = input_list[index_1] # Using temp so we don't lose the original value at index_1
  input_list[index_1] = input_list[index_2]
  input_list[index_2] = temp
  return input_list # Make sure to return the swapped list

# The lowest index before we begin the for loop is 0

lowest_index = 0

# Step 2: Write the for loop that finds the lowest index in the list

for i in range(len(my_list)):
  if my_list[i] < my_list[lowest_index]:
    lowest_index = i

# Step 3: After finding the lowest index, use swap() to put the lowest value at the start of the list

my_list = swap(my_list, lowest_index, 0)
print(my_list)
