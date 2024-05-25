 #!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the name
    print(f"My name is {first_name} {last_name}")

# Examples
say_my_name("John", "Doe")  # Output: My name is John Doe
say_my_name("Jane")         # Output: My name is Jane 

