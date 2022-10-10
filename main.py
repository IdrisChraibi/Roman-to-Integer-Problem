s = input("") # Input variable containing the Roman numerals to be translated
        
roman = { "I" : 1,     # Assign a value to each roman integer using a hashmap
          "V" : 5, 
          "X" : 10, 
          "L" : 50, 
          "C" : 100, 
          "D" : 500, 
          "M" : 1000 }      

result = 0 #  The result after converting the Roman integer to whole numbers
        
for i in range (len(s)): # iterate through the string
    if i + 1 < len(s) & roman[s[i]] < roman[s[i + 1]]: # "i + 1 < len(s)" is needed so the string index doesnt go out of range, "roman[s[i]] < roman[s[i + 1]]" if the value is decreasing 
        result = result - roman[s[i]]                          # subtract the value from the result
    else:
        result = result + roman[s[i]] # add the value to the result
                
print(result) # print the result
