# Programmer: Lucas Podowski
# Course:  CS151, Zelalem Yalew
# Due Date: 10/31/2024
# programming Assignment: 3
# Problem Statement: You are creating a program to display ASCII art and string decorations to the user.
# ASCII art is just a combination of characters that make a design or pattern.
# Data In: design choice, number of times to output the design, and if user will restart the program
# Data Out: design type

# Purpose: prompt user for design choice
# Parameter: none
# Return: choice
def design_choice():
    choice = input("\nEnter the design you want to output (line, circle, poop): ").strip().lower()

    while choice not in {'line','circle','poop'}:
        print('Invalid choice')
        choice = input("Enter the design you want to output (line, circle, poop): ").strip().lower()
    return choice

# Purpose: prompt user for the number of times they want to output the design
# Parameter: choice
# Return: output_num
def input_num(choice):
    # Allows for custom word choices for your choice
    if choice == 'poop':
        words = 'piles of poop'
    else:
        words = choice + 's'

    output_num = input(f'Enter how many {words} you want to display: ').strip()

    while not output_num.isdigit():
        print("Invalid! You must enter an integer!")
        output_num = input(f'How many times do you want to display {choice}: ').strip()
    return int(output_num)

# Purpose: Contains and selects one of three ASCII designs
# Parameter: choice
# Return: design
def designs(choice):
    if choice == 'line':
        # This line design was designed by me to be long
        design = '''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
    elif choice == 'circle':
        # Inspiration of this circle design is from https://ascii.co.uk/art/circle
        design = """
                   , - - - ,
               , '           ' ,   
             ,                   ,
           ,                       ,
          ,                         ,
         ,                           ,
         ,                           ,
         ,                           ,
          ,                         ,
           ,                       ,
             ,                  , '
               ' - , _ _ _ ,  '
        """
    else:
        # This poop design comes from Krogg98 from the website https://ascii.co.uk/art/shit
        design = r"""
             (   )
          (   ) (
           ) _   )
            ( \_
          _(_\ \)__
         (____\___))
         """
    return design

# Purpose: Contain code to run function
# Parameter: none
# Return: none
def main():
    print("This program will repeatedly ask you what design you would like to output.\n"
          "You can output lines, circles, or piles of poop.\n"
          "It will then ask you how many times you want to output that design.")
    restart = 'yes'
    while restart == 'yes':
        choice = design_choice()
        number = input_num(choice)
        design = designs(choice)
        print(design * number)
        restart = input('Enter "yes" to continue: ').lower()
main()