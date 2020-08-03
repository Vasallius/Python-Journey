# Mad Libs

# Asking for user inputs
adj = input("Enter an adjective: ")
noun = input("Enter an noun: ")
verb = input("Enter an verb: ")
noun2 = input("Enter an noun: ")

output_file = open('sample.txt', 'w+')

# Substituting variables to placeholders
string = f"""The {adj} panda walked to the {noun} and then {verb}. A nearby {noun2} 
was unaffected by these events."""

output_file.write(string)
output_file.close()
