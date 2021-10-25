
print("Welcome to guess the number.")
print("I choose a four digit number (0 to 9999), and you guess it in 10 tries or less to win.  Each try is for a single digit!")

import numpy as np
x = np.random.randint(0,10000)
s = '{:4}'.format(x).replace(' ', '0')
x = list(map(int, list(s)))
found = [0, 0, 0, 0]
print(x)
count = 0
while True:
    count += 1
    display = ''
    for i in range(4):
        if found[i]:
            display += str(x[i])
        else:
            display += 'X'
    print("You currently have: ", display)


    loc = int(input("Which digit to guess? "))
    if found[loc]:
        print("You already got that one.!")
        continue

    val = int(input("Which value do you guess? "))
    if val == x[loc]:
        found[loc] = 1
        print("congrats!")

    if sum(found) == 4:
        print("You win!")
        break

    if count >= 10:
        print("You lose!")
        break 

     
