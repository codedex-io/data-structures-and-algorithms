# Selection Sort II 📶
# Codédex

my_list = [8, 15, 4, 2]

def swap(input_list, index_1, index_2):
  temp = input_list[index_1] #Using temp so we don't lose the original value at index_1
  input_list[index_1] = input_list[index_2]
  input_list[index_2] = temp
  return input_list # Make sure to return the swapped list

for j in range(len(my_list)):
  lowest_index = j # Lowest index now starts at j
  for i in range(j, len(my_list)): #i now starts at j rather than 0
    if my_list[i] < my_list[lowest_index]:
      lowest_index = i
  my_list = swap(my_list, lowest_index, j) # Swapping with position j rather than 0

print(my_list)
