from deps.bot import bot_character, client
from deps.api import token as TOKEN # Create api.py file and add token

def main():
    '''The main program'''

    valid = False
    
    n = 0
    for i in bot_character.names_list:
        print(f"""{n + 1}. {i}""")
        n += 1
    
    while not valid:
        usr_input = input("Type the name of a character: ") 

        if usr_input not in bot_character.characters_list:
            print("Not a valid character. Try again.")
        else:
            bot_character.usr_select = usr_input
            valid = True
    
    client.run(TOKEN)
    

if __name__ == "__main__":
    main()