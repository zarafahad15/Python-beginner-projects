secret = 3

def guess_num():
    for attempt in range(3):
        guess = int(input("🔢 Enter your guessed number: "))
        
        if guess > secret:
            print("📈 Too High!")
        elif guess < secret:
            print("📉 Too Low!")

        else:          
            print("🎉 YOU GUESSED RIGHT!")
            break
    else:
        print("😢 Out of guesses!")

guess_num()

 