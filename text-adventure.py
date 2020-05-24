name = input(
    "Hello! what is your name?\nplease type your name and then hit 'enter'\n")


def start_the_game():
    begin_the_game = input("Great to meet you, " + name +
                           ", are you ready to begin?\nplease hit 'y' or 'n' and then hit enter\n")
    if begin_the_game == "y":
        print("Great!\nOnce upon a Tuesday, you're walking down a nice forest path when-\nOH NO! It's the reanimated corpse of William Shakespeare comeong towards you!\nWhat do you do?")
    elif begin_the_game == "n":
        print("Well...bye then I guess?")
    else:
        print("invalid response")
        repeat = input("press 'r' to go back\nany other key will exit game\n")
        if repeat == "r":
            start_the_game()
        else:
            exit()


start_the_game()

