#!/usr/bin/python3

def multiple_returns(sentence):
    # Check if the sentence is empty
    if sentence == "":
        return (0, None)
    
    # Return the length of the sentence and the first character
    return (len(sentence), sentence[0])

print(multiple_returns("Hello"))
print(multiple_returns(""))
print(multiple_returns("Python"))  
print(multiple_returns("A"))
