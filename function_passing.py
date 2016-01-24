"""
Milestones:
1 
"""
def num_digits(x):
  return len(str(x))

def most_digits(L):
  L = sorted(L, key=num_digits)
  return L[-1]
  
def largest_two_digit_even(L):
  two_digit_numbers = [i for i in L if num_digits(i)==2]
  evens = [i for i in two_digit_numbers if i%2 == 0 ]
  evens.sort()
  return evens[-1]

def num_ones_in_binary(given_int): #input: single integer(base 10)
  binary_number = bin(given_int)[2:] #convert into binart, get rid of 0b
  count_one = binary_number.count('1') #count ones in the str
  return count_one
  
def most_ones_in_binary(L):
    L= sorted(L, key=num_ones_in_binary) #sort by count
    return L[-1] #return largest
  
def best(L, criteria):
    return criteria(L)
  
L = [1, 76, 1045693, 84, 95, 214, 1023, 511, 32]
print(best(L, min)) # Prints 1
print(best(L, largest_two_digit_even)) # Prints 84
print(best(L, most_digits)) # Prints 1045693
print(best(L,most_ones_in_binary)) #Print 1045693

  



