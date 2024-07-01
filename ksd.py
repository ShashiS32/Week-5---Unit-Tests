import random

try:
    inp = input("Whats ur name? ")

except ValueError:
    print("Sorry, please write your name!")

alphabet = alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
common_symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', 
    '}', '~'
]

passord = []

for letters in range (0,4):
    passord.append(random.choice(alphabet))
    passord.append(random.choice(numbers ))


for letters in range (0,2):
    passord.append(random.choice(common_symbols))


random.shuffle(passord)

passord = ''.join(str(x) for x in passord)

print(passord)

userPass = {
    inp: passord
}

print(userPass)