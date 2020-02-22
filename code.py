alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter a string: ")
# print(string_input)
shift_input = int(input("Enter in a value to shift by: "))

input_length = len(string_input)
print(input_length)

string_output = ""

for i in range(input_length):
    character = string_input[i].upper()
    location_of_character = alpha.find(character) # returns character index location
    new_location = location_of_character + shift_input
    string_output += alpha[new_location]


print("Encrypted text is: ", string_output.lower())

