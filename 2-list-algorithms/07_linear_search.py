# Linear Search 📧
# Codédex

def linear_search(input_list, target_value):
  for item in input_list:
    if item == target_value:
      return True
  return False

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
