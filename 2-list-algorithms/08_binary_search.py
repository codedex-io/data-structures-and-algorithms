# Binary Search 📧
# Codédex

def binary_search(input_list, target):
  left = 0
  right = len(input_list) - 1
    
  while left <= right:
    mid = (left + right) // 2   # Finds the middle index
        
    if input_list[mid] == target:
      return True               # Target found
    elif target < input_list[mid]:
      right = mid - 1           # Search the left half
    else:
      left = mid + 1            # Search the right half
    
  return False                  # Target not found

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

print(binary_search(email_list, 'mgoodyear@lumonindustries.com'))   # Output: True
print(binary_search(email_list, 'mark.scout@lumonindustries.com'))  # Output: False

# Checking an edge case - what if our input list is empty?

empty_list = []
print(binary_search(empty_list, 'dwight@dundermifflin.com'))        # Output: False
