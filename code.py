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
    new_location = (location_of_character + shift_input) % 26 # divides by 26 and takes the module value
    # if new_location >= 26: # long-method
    #     new_location -= 26
    string_output += alpha[new_location] # adding '+' concatenate each character. if removed, i.e '=' then all previous characters are over-ridden.


print("Encrypted text is: ", string_output.lower())

print(3000 % 26)