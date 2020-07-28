# Program for guess the number
n = 18
print("Hello There, This is number guessing game\nYou Have only 9 guesses")
guess = 1
while (guess <= 9):
    guess_inp = int(input())
    if guess_inp < 18:
        print("Try Large number")
    elif guess_inp > 18:
        print("Try Small number")
    else:
        print("Congratulations You won")
        print(guess, "no of guess you took")
        break
    print(9 - guess, "No. of guess are left")
    guess = guess + 1

if guess > 9:
    print("You Lost!")