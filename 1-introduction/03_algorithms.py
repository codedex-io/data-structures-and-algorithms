# Algorithms Demo 🙂
# Codédex

def insertion_sort(arr):
  for i in range(1, len(arr)-1):  
    key = arr[i]  
    j = i - 1  
  
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
       
    arr[j + 1] = key  

  return arr

# Update the list below

input_list = [5, 3, 8, 4, 2, 10, 3]

output_list = insertion_sort(input_list)

print(output_list)
