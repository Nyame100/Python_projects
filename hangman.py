import random
# This is a hangman game.

logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ '''

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# Print logo
print(logo)
# Generate a random word.
words = ('''apple, bread, chair, dream, eagle, flame, grape, house, index, joker, knife, lemon, mango, night, ocean, piano, queen, river, stone, tiger, unity, voice, water, youth, zebra, actor, badge, cable, dance, earth, faith, giant, heart, ideal, judge, karma, laser, magic, noble, olive, panel, quick, radio, sugar, table, urban, vivid, wheat, xenia, yield, zoned, alert, blaze, craft, drill, entry, frost, glide, humor, input, jewel, kneel, layer, meter, never, orbit, phase, quite, rough, scale, train, upper, value, world, xenon, young, zesty, adopt, brick, crane, depth, elite, frame, grand, honor, irony, logic, model, novel, ounce, pride, quest, realm, solid, trace, usage, vital, worth, yeast, zone, admit, boost, clamp, deter, eager, fiber, grasp, hover, issue, joint, knock, lucid, minor, nurse, optic, press, quota, rally, serve, tempo, abide, bison, coral, denim, evoke, flair, gauge, haste, inlet, jaunty, knead, lodge, medal, niche, onset, proxy, quirk, rider, satin, tonic, utter, vapor, widen, xylem, yacht, zippy, agile, blunt, cider, droid, ember, ferry, genre, hardy, ivory, jolly, kayak, linen, motto, nylon, omega, polar, quart, rover, shyly, token, ulcer, verge, weary, xylan, yodel, zonal, amass, bribe, civic, decor, envoy, fable, gloat, haunt, ingest, juror, lapse, manor, nasal, opine, patio, quail, repel, scoop, tease, unify, vigor, wiser, xenic, zappy, adapt, bloom, charm, drier, exalt, fling, gloom, hiker, jazzy, lunar, mixer, nudge, oxide, plead, quash, spice, thorn, waltz, xenial, yonder, zodiac, anchor, beacon, carpet, dagger, empire, forest, galaxy, harbor, island, jacket, kernel, legend, marble, nectar, orange, pebble, quorum, rocket, silver, temple, unique, velvet, window, yellow, zipper, absent, border, custom, driver, effect, fabric, gentle, hazard, intent, jungle, kettle, ladder, market, native, object, parent, random, safety, talent, useful, vision, wealth, yearly, zenith, artist, battle, circle, demand, energy, factor, growth, height, impact, junior, kingdom, launch, memory, notion, option, people, result, secret, travel, urgent, vacant, wander, accept, bright, clever, depart, evolve, finish, global, honest, income, justify, kindly, luxury, master, narrow, online, prefer, reward, simple, target, update, volume, worker, across, barely, costly, decent, expand, formal, gather, handle, immune, keeper, lesson, manage, notice, output, proper, refuse, scheme, theory, unlike, valley, writer, admire, broken, client, differ, effort, future, golden, humble, inform, jester, lawful, modern, normal, oppose, period, quiet, remote, stable, timely, upward, versus, weekly, youthful, zephyr, thrive, afraid, breeze, castle, doctor, editor, farmer, hunter, leader, mother, nature, office, painter, reader, singer, teacher, vendor, banker, caller, dancer, helper, carbon, deluxe, estate, fossil, hardly, insert, kidney, margin, origin, pillar, quester, rugged, summit, tunnel, uphold, victor, winter, xenons, amber, cobalt, daring, fertile, glacier''').split(", ")
random_word = random.choice(words)
#print(random_word)
#print(words)
game_over = False
life_lost = 0
lives = 6
stage = ""
all_guessed_letters = []

# Generate blanks matching each word.
word_length = len(random_word)
blanks = list("_"*word_length)
print("".join(blanks))
#print(blanks)

# Asking user to guess a word.
while not game_over:
    guessed_letter = input("Guess a letter\n").lower()
    
# Checking if a guess is repeated.
    if guessed_letter not in all_guessed_letters:

# What happens if guessed letter is in word.
        for i in range(len(random_word)):
            if random_word[i] == guessed_letter:
                blanks[i] = guessed_letter
                all_guessed_letters += guessed_letter
                #print(blanks)
        print("".join(blanks))
        if "".join(blanks) == random_word:
            game_over = True
            print("You win")

# What happens if guessed letter is not in word
        if guessed_letter not in random_word:
            life_lost += 1
            all_guessed_letters += guessed_letter
# Because the 1st item in list is indexed at 0, we sub 1 from life_lost.        
            stage = stages[life_lost-1]
            print(stage)
            print(f"You guessed ({guessed_letter.upper()}), that's not in the word. You lose a life.")
            #print(f"{life_lost} life lost")
            if life_lost > lives:
                game_over = True
                print("You lose!\nGAME OVER")
                print(f"The word is: {random_word.upper()}")
    else:
        print(f"You already guessed the letter: {guessed_letter.upper()}")
