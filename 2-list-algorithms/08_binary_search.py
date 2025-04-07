# Binary Search 📧
# Codédex

def binary_search(input_list, target):
  if not input_list:
    return False  
 
  mid = len(input_list) // 2
 
  if input_list[mid] == target:
    return True
  elif  target < input_list[mid]:
    return binary_search(input_list[:mid], target)
  elif  target > input_list[mid]:
    return binary_search(input_list[mid + 1:], target)

# ------------- TESTING YOUR ALGORITHM -----------------

email_list = [
  'dwight.schrute@dundermifflin.com', 
  'michael.scott@dundermifflin.com',
  'mgoodyear@lumonindustries.com',
  'walter.white@jpwynnehigh.edu',
  'hank@dea.gov',
  'kimberly.finkle@essexu.edu',
  'sheldon@caltech.edu',
  'elliot@allsafe.com',
  'mr.robot@fsociety.com',
  'mulder@fbi.gov',
  'carrie@sexandthecity.tvs',
  'pleasecallmebarney@yahoo.com',
  'buffy@sunnydale.edu'
]

print(linear_search(email_list, 'mgoodyear@lumonindustries.com'))   # Output: True
print(linear_search(email_list, 'mark.scout@lumonindustries.com'))  # Output: False

# Checking an edge case - what if our input list is empty?

empty_list = []
print(linear_search(empty_list, 'dwight@dundermifflin.com'))        # Output: False
