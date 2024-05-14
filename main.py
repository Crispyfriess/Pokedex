import csv
import random as rd
import os

# Import the csv data to a variable
with open('Pokemon.csv', 'r') as file:
  pokemon = list(csv.reader(file))

# Extract the data from the pokemon csv, assign to a variable
name = [pokemon[i][1] for i in range(1, len(pokemon))]
type_1 = [pokemon[i][2] for i in range(1, len(pokemon))]
type_2 = [pokemon[i][3] for i in range(1, len(pokemon))]
total = [int(pokemon[i][4]) for i in range(1, len(pokemon))]
hp = [int(pokemon[i][5]) for i in range(1, len(pokemon))]
attack = [int(pokemon[i][6]) for i in range(1, len(pokemon))]
defense = [int(pokemon[i][7]) for i in range(1, len(pokemon))]
sp_atk = [int(pokemon[i][8]) for i in range(1, len(pokemon))]
sp_def = [int(pokemon[i][9]) for i in range(1, len(pokemon))]
speed = [int(pokemon[i][10]) for i in range(1, len(pokemon))]
generation = [pokemon[i][11] for i in range(1, len(pokemon))]
legendary = [pokemon[i][12] for i in range(1, len(pokemon))]

def displayMenu():
  """
  Displays the menu.

  Parameters
  ----------
  None

  Returns
  -------
  None
  """
  
  print('''
Pokemon Super Engine
  1. Display Pokemon with their types and statistics
  2. Display the first Pokemon of a Type of your choice
  3. Display all Pokemons with Total Base stat of your choice
  4. Display all Pokemons with a minimum set of stats
  5. Display all legendary Pokemons of Types of your choice
  6. Surprise me! (don't worry I'm not gonna zipbomb you :>)
  0. Quit
  ''')

def displayHeader():
  """
  Displays the header for the table.

  When called, the header is displayed. Formatted nicely using string formatting 

  Parameters
  ----------
  None

  Returns
  -------
  None
  """

  print(
    "{:^3} | {:26} | {:^9} | {:^9} | {:^6} | {:^4} | {:^7} | {:^8} | {:^7} | {:^7} | {:^6} | {:^11} |{:^10}".format('No.', 'Name', 'Type_1', 'Type_2', 'Total', 'HP', 'Attack', 'Defense','Sp. atk' ,'Sp. def', 'Speed', 'Generation', 'Legendary'))

def poke(n):
  """
  Displays the pokemon using it's index.

  Given the index of the pokemon, it will display the name, type, total,
  hp, attack, defense, sp. atk, sp.def, speed, generation and legendary 
  status of the pokemon.

  It will be formatted in a table using string formatting.

  Parameters
  ----------
  n  :  Int
        Index of the pokemon to display

  Returns
  -------
  None
  """
  print(
    "{:^3} | {:26} | {:^9} | {:^9} | {:^6} | {:^4} | {:^7} | {:^8} | {:^7} | {:^7} | {:^6} | {:^11} | {:^10}".format(n+1, name[n], type_1[n], type_2[n], total[n], hp[n], attack[n], defense[n],sp_atk[n] ,sp_def[n], speed[n], generation[n], legendary[n]))

def collecting_system(pokemons) :
  '''
  Pokemon collecting system.
  
  Generate a random pokemon index and check if pokemon is legendary. 
  If pokemon is a legendary, then it will ask the user to guess a number from 0-100. 
  If the user guesses the number correctly, then the user will get a legendary pokemon. 
  
  If the pokemon is not a legendary, then it will ask the user to guess a number from 0-10. 
  If the user guesses the number correctly, then the user will get a normal pokemon.
  
  User will only get 5 tries to guess the number.

  Parameters
  ----------
  None

  Returns
  -------
  None
  '''
  guessed = False
  
  number = rd.randint(1,800)

  #if Pokemon is legendary
  if legendary[number] == "TRUE" :
    gacha = rd.randint(1,100)   
    counter = 0
    
    while not guessed:
      #Check for input validity
      try :
        guess = int(input("A wild LEGENDARY pokemon has appeared! Guess a number from 1-100: "))

        #Logic for guessing the number
        if guess == gacha: 
          print(f"Congratulations! You got {name[number]}!")
          pokemons.append(number)
          guessed = True
        elif guess > 100 or guess < 0 : 
          print('Invalid input! Please enter a number from 1-100\n')
          counter -= 1
        elif guess > gacha:
          print(f"Your guess is too high! You have {4-counter} tries left.\n")
        elif guess < gacha:
          print(f"Your guess is too low! You have {4-counter} tries left.\n")

        if counter == 4 : 
          guessed = True
          print(f'{name[number]} has run away...')

        counter += 1
        
      #Ensure value error is not raised.
      except ValueError:
        print("Invalid input. Please enter a number from 1-100.\n")
        counter -= 1

  #If pokemon is not a legendary, then it will ask the user to guess a number from 0-10.
  else : 
    gacha = rd.randint(1,10)
    counter = 0
    
    while not guessed:
      try :
        guess = int(input("A wild pokemon has appeared! Guess a number from 1-10: "))

        #Logic for guessing the number
        if guess == gacha: 
          print(f"Congratulations! You got {name[number]}!")
          pokemons.append(number)
          guessed = True
        elif guess > 10 or guess < 0: 
          counter -= 1
          print('Please enter a number from 1-10\n')
        elif guess > gacha:
          print(f"Your guess is too high! You have {4-counter} tries left.\n")
        elif guess < gacha:
          print(f"Your guess is too low! You have {4-counter} tries left.\n")

        if counter == 4 : 
          guessed = True
          print(f'{name[number]} has run away...\n')

        counter += 1
        
      #Ensure value error is not raised
      except ValueError:
        print("Invalid input. Please enter a number from 1-10.\n")
        counter -= 1

  return pokemons

def surpriseMe():
  """
  A pokemon collecting game.

  Generate a random number between 1 and 800 and access the different pokemon that is the indee

  Parameters
  ----------
  None

  Returns
  -------
  None
  """
  os.system('clear')
  
  pokemons = []
  
  if os.path.isfile('savedata.txt'):
    with open('savedata.txt', 'r') as file:
      savedata = file.readline()
      savedata = savedata.split(',')

      for i in savedata:
        if i != '':
          pokemons.append(int(i))
      
  
  con = True
  while con:
    try : 
      print("\nWelcome to the Pokemon Collector!\n"
        "What are you going to do today?\n"
        "1. Catch a pokemon!\n"
        "2. See my collection.\n"
        "3. Tutorial -- Help me!\n"
        "0. Return to Pokedex.\n")
      choice = int(input("Enter your choice: "))
  
      if choice == 1:
        #Play gacha
        pokemons = collecting_system(pokemons)

        with open('savedata.txt', 'w') as file:
          save_poke = ''
          for i in pokemons:
            save_poke += str(i) + ','
          file.write(save_poke)
      
      elif choice == 2:
        #Display collection
        if len(pokemons) == 0:
          print("You don't have any pokemon yet!")
        else:
          print("\nMy collection!")
          displayHeader()
          for pokemon in pokemons:
            poke(pokemon)
        
      elif choice == 3:
        print('\nWelcome to Tutorial for collecting pokemon!\n'
             'How to catch a pokemon?\n'
             '1. Press 1 to find a pokemon\n'
             '2. The system will show you whether the pokemon is legendary or not\n'
              '3. If the pokemon is legendary, you can obtain it by guessing a number from 1-100\n'
              '4. If the pokemon is common, you can obtain it by guessing a number from 1-10\n'
             'However, you are only given 5 tries to guess the number\n'
              'If you fail to guess the pokemon, the pokemon will run away.\n'
             'Press 2 to see your pokemon collection')
        #Display tutorial
      elif choice == 0:
        #Return to pokedex
        os.system('clear')
        return
      else:
        print("Invalid choice. Please try again.")
        
    except ValueError :
      print('Invalid input. Please enter a number from 0-3.\n')
    


def displayPokemon(n):
  """
  Displays N number of pokemon(s).

  Given the number of pokemon, it will
  display the name, type, and other stats.

  It will be formatted in a table using 
  string formatting.
  
  Parameters
  ----------
  n  :  Int
        Number of Pokemon to display

  Returns
  -------
  None
  """
  displayHeader()
  
  for number in range(0, n):
      poke(number)

def displayPokeType(type):
  """
  Displays all pokemon of a certain type.
  
  Parameters
  ----------
  type  : String
          Type of pokemon to display

  Returns
  -------
  None
  """
  myList = []
  
  #Searching for pokemon of same type.
  for index in range(1, len(pokemon)-1):
    if type_1[index].lower() == type.lower() or type_2[index].lower() == type.lower():
      myList.append(index)

  if len(myList) == 0:
    print("No pokemon of that type found!\n")
  else:
    displayHeader()  
    poke(myList[0])
     
def displayPokeBaseStat(stat):
  """
  Displays all pokemon with a certain base stat.

  Prints all pokemon with a certain base stat in
  a table using string formatting.

  Parameters
  ----------
  stat  : Int
          Value of base stat of pokemon

  Returns
  -------
  None
  """
  myList = []
  
  #Searching for pokemon of same total base stat.
  for index in range(1, len(pokemon)-1):
    if stat == total[index]:
      myList.append(index)

  if len(myList) == 0:
    print("No pokemon of that minimum base stat found!\n")
  else:
    displayHeader()  
    for index in myList:
      poke(index)

def displayPokeMinStat(min_atk, min_def, min_speed):
  """
  Displays all pokemon with a certain 
  minimum stat.

  Prints all pokemon with a certain minimum 
  stat of special attack, defense, and speed 
  of pokemon using string formatting.

  Parameters
  ----------
  min_atk  :  Int
              Minimum value of special attack

  min_def  :  Int
              Minimum value of special defense

  min_speed:  Int
              Minimum value of speed

  Returns
  -------
  None
  """
  myList = []
  
  for index in range(1, len(pokemon)-1):
    if sp_atk[index] >= min_atk and \
    sp_def[index] >= min_def and \
    speed[index] >= min_speed:
      myList.append(index)

  if len(myList) == 0:
    print("No pokemon of that minimum stats found!\n")
  else:
    displayHeader()  
    for index in myList:
      poke(index)

def displayLegendary(t1, t2):
  """
  Displays all legendary pokemon of a 
  certain types.

  Prints all legendary pokemon of a certain 
  type 1 and type 2.

  Parameters
  ----------
  t1  :  String
         Type 1 of pokemon
  t2  :  String
         Type 2 of pokemon

  Returns
  -------
  None
  """
  

  myList = []
  
  for index in range(1, len(pokemon)-1):
    if legendary[index] == "TRUE" and \
     t1.lower() == type_1[index].lower() and \
     t2.lower() == type_2[index].lower():
        myList.append(index)
      
  if len(myList) == 0:
    print("No legendary pokemon of that type found!\n")
  else:
    displayHeader()  
    for index in myList:
      poke(index)
    
    
    
  
  

#Main
cont = True
      
while cont: 

  # Display menu and input choice
  displayMenu()
  
  invalid_input = True
  while invalid_input:
    try:
      option = int(input("Enter option: "))
      invalid_input = False
    except ValueError: 
       print("\nInvalid input. Please enter a number.\n")
      

  # Display N pokemon
  if option == 1:
    invalid_input = True
    while invalid_input:
      try:
        displayed_pokemon = int(input("Enter number of Pokemon you want to display: "))
        invalid_input = False
      except ValueError:
        print("\nInvalid input. Please enter a number.\n")
    
    displayPokemon(displayed_pokemon)
    
  #Display type pokemons
  elif option == 2 : 
    type_poke = input('Enter pokemon\'s type: ')

        
    displayPokeType(type_poke)
  
  #Display pokemons with total base stat      
  elif option == 3:
    invalid_input = True
    while invalid_input:
      try:
        stat_poke = int(input('Enter pokemon\'s base stat: '))
        invalid_input = False
      except ValueError:
        print("\nInvalid input. Please enter a number.\n")
    
    displayPokeBaseStat(stat_poke)

  #Display pokemons with min set of stats
  elif option == 4:
    invalid_input = True
    while invalid_input:
      try:
        min_atk = int(input("Enter pokemon\'s minimum special attack: "))
        min_def = int(input("Enter pokemon\'s minimum special defense: "))
        min_speed = int(input("Enter pokemon's minimum speed: "))
        invalid_input = False
      except ValueError:
        print("\nInvalid input. Please enter a number.\n")

    displayPokeMinStat(min_atk, min_def, min_speed) 

  #Display legendary pokemons of type
  elif option == 5:
    type_1_poke = input('Enter pokemon\'s 1st type: ')
    type_2_poke = input("Enter pokemon\'s 2nd type: ")
    

    displayLegendary(type_1_poke, type_2_poke)

  #Surprise me!
  elif option == 6:
    surpriseMe()

  #Quit
  elif option == 0:
    print("Goodbye!")
    cont = False
      