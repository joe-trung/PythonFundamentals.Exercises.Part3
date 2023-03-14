def greet(name):
    print ("Hello " +name)
greet("Trung Tran")
greet("Darth Vader")
greet("Guido van Rossum")
def name_input():
    return(input("Please enter your name:"))
greet(name_input())

def language_input():
    chosen_language = input("Please choose your language (1 for English, 2 for Spainish, 3 for French)")
    if chosen_language == "1":
        print("Hello " + input("What's your name?"))
    elif chosen_language == "2":
        print("Hola " + input("Cómo te llamas?"))
    elif chosen_language == "3":
        print("Bonjour " + input("Comment vous-appelez vous?"))

language_input()