# Vasallius

# Asking for user inputs
print("Enter an adjective:")
adj = input()
print("Enter an noun:")
noun = input()
print("Enter an verb:")
verb = input()
print("Enter an noun:")
noun2 = input()

new_file = open('newfile.txt', 'w')

# Substituting variables to placeholders
string = f"""The {adj} panda walked to the {noun} and then {verb}. A nearby {noun2} 
was unaffected by these events."""

new_file.write(string)
new_file.close()
