def smallest_lexicographical_string (P, S):
    
      order_dict = {P[i]: i for i in range(26)}
# Sort string S using the order specified in P
      sorted_S = sorted(S, key=lambda char: order_dict[char])
# Convert the sorted list back to a string
      result = ''.join(sorted_S)
      return result
# number of test cases
T = int(input("Enter Number of Test Cases: "))
results = []
for i in range(T):
    P = input("Enter String P: ")
    S = input("Enter String S: ")
    result = smallest_lexicographical_string (P, S)
    

results.append(result)
for result in results:
   print (result)
