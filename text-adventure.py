name = input(
    "Hello! what is your name?\nplease type your name and then hit 'enter'\n")

# note, choices are defined by the naming convention "choice_[first choice]_[second choice]..." so if the player chooses 1, 2, and then 1, that function will be named "choice_1_2_1"


def choice_1_invalid():
    choice_1()


def choice_1_3_2_i():
    choice_1_3_2()


def choice_1_3_i():  # for some god-foresaken reason, any other choice_n_invalid doesn't work, I have to use i instead of invalid
    choice_1_3()


def choice_1_3_4():  # for some god-foresaken reason, any other choice_n_invalid doesn't work, I have to use i instead of invalid
    choice_1_4_i()


def start_the_game():
    begin_the_game = input("Great to meet you, " + name +
                           "! Are you ready to begin?\nplease hit 'y' or 'n' and then hit enter\n")
    if begin_the_game == "y":
        print("Great!\nOnce upon a Tuesday, you're walking down a nice forest path when-\nOH NO! It's the reanimated corpse of William Shakespeare coming towards you!\nWhat do you do?")
        choice_1()
    elif begin_the_game == "n":
        print("Well...bye then I guess?")
    else:
        print("invalid response")
        repeat = input("press 'r' to go retry\nany other key will exit game\n")
        if repeat == "r":
            start_the_game()
        else:
            exit()


def start_over():  # function to start from the "Great to meet you, name..." part
    start_over = input(
        "If you would like to try again, please hit 'r' and then 'enter', hit any other key and 'enter' to end the program\n")
    if start_over == "r":
        start_the_game()
    else:
        exit()


def choice_1_3_2():
    choice_1_3_2 = input(
        "Bill isn't scared of your blade, and charges at you!\nWhat do you do?\n1.Swing low with your katana\n2.Swing high with your katana\n3.Charge at him\n4.Run away screaming\nYou know the drill when it comes to the buttons\n")
    if choice_1_3_2 == "1":
        print("He jumps over your blade and literally kicks your head off your body\n")
        start_over()
    elif choice_1_3_2 == "2":
        print("He combat rolls under your blade and delivers a swift uppercut, knocking your head off your body\n")
        start_over()
    elif choice_1_3_2 == "3":
        print("When you two meet, your blade crumples against his iron-clad pecs and he crashes into you with the force of a thousand suns. You never had a chance.\n")
        start_over()
    elif choice_1_3_2 == "4":
        print("You trip over a branch and fall on your face. Your katana goes flying through the air and somehow lands blade-first on Shakespeare's bald spot, his one weakness!\nHe cries out in anguish 'Aaah, if only I used Regain Extra Strength Foam available for £40.99!\nHe's dead.\nYou win!")
        start_over()
    else:
        print("invalid response")
        choice_1_3_2_invalid = input(
            "press 'r' and then 'enter' to retry\nany other key will exit game\n")
        if choice_1_3_2_invalid == "r":
            choice_1_3_2_i()
        else:
            exit()


def choice_1_3_3():
    print(
        "Shakespeare halts.\n'y-you can't be serious?' he asks.\nYou are.\n'Kaaa...'\n'...meeeh.\nkaaaa\nmeeeeh.\nAAAAAAH\nShakespeare is obliterated.")
    start_over()


def choice_1_3():
    choice_1_3 = input("Shakespeare breaths in deep and flexes his biceps, which grow to at least 24\", bruh I need his routine.\nWhat will you do?\n1.Run away screaming\n2.Pull out your katana that does +2 against any undead foes\n3.Plant your feet, and start charging up a kamehameha wave\nPress '1', '2', or '3', and then hit 'enter'\n")
    if choice_1_3 == "1":
        print("You trip over a branch and fall on your face. He effortlessly picks you up, says 'I was wondering what would break first, you spirit, or your body!' and snaps your spine over his knee. Before you die you have time to think 'Was that a Bane quote? How does Shakespeare know that Bane quote. Mad'")
        start_over = input(
            "If you would like to try again, please hit 'r' and then 'enter', hit any other key and 'enter' to end the program\n")
        if start_over == "r":
            start_the_game()
        else:
            exit()
    if choice_1_3 == "2":
        choice_1_3_2()
    if choice_1_3 == "3":
        choice_1_3_3()
    else:
        print("invalid response")
        choice_1_3_invalid = input(
            "press 'r' and then 'enter' to retry\nany other key will exit game\n")
        if choice_1_3_invalid == "r":
            choice_1_3_i()
        else:
            exit()


def choice_1_4():
    choice_1_4 == input(
        "World-renowned authour and playwright William Shakespeare has tears and snot running down his face.\n'I-I'm way better then that hack author!'\nHow do you want to address the mess in front of you?\n1.Say 'Oh no, wait! You're the guy who wrote Harry Potter!'\n2.Laugh at him\n3.Back slowly away\n4.Say 'Sorry man, I didn't mean it, I love your work!\n")
    if choice_1_4 == "1":
        print("William's head explodes from stress\n")
        start_over()
    elif choice_1_4 == "2":
        print("'S-s-stop laughing at me!' he squeals. You laugh even more and walk away.")
        start_over()
    elif choice_1_4 == "3":
        print(
            "'You get back here right no-' and slips on his own tears. His neck snaps. F.")
        start_over()
    elif choice_1_4 == "4":
        print("He looks up with hope in his eyes. 'R-really?;\nYou smile down at him, lean in, and whisper, 'no'.\nYou walk away.s")
    else
     print("invalid response")
      choice_1_4_invalid = input(
           "press 'r' and then 'enter' to retry\nany other key will exit game\n")
       if choice_1_4_invalid == "r":
            choice_1_4_i()
        else:
            exit()


def choice_1():
    choice_1 = input("1.Run away screaming\n2.Walk up to him and give him a firm handshake\n3.Challenge him to a fight\n4.Say 'I loved your book, The Shining!'\npress '1', '2', '3', '4', and then hit 'enter'\n")
    if choice_1 == "1":
        print("You trip over a branch, fall onto your face, and are promptly devoured")
        start_over()
    elif choice_1 == "2":
        print("He's impressed by your 'can do!' attitude, and immediately offers you a job. Great work, champ!")
        start_over()
    elif choice_1 == "3":
        choice_1_3()
    elif choice_1 == "4":
        print("William... bursts into tears?")
        choice_1_4()
    else:
        print("invalid response")
        choice_1_invalid = input(
            "press 'r' and then 'enter' to retry\nany other key will exit game\n")
        if choice_1_invalid == "r":
            choice_1_invalid()
        else:
            exit()


start_the_game()
