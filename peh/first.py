#!/bin/python3

print('\n')
#STRINGS
print("Hello World")
print('Hello World')
print("""This string runs
multiple lines!""")
print("This string is " + "awesome") #we can also concatenate
print('\n') #new line
print('test the new line')

print('\n')
#MATH
print(50 + 50) #add
print(50 - 50) #abstract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 50) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 // 6) #no remainder

print('\n')
#VARIABLES AND METHODS

quote = 'All is fair in love and war.'
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Heath"
age = 33 #int
gpa = 3.7 #float
print(int(age))
print(int(30.1))
print(float(30.1))

print("My name is " + name + " and i am " + str(age) + " years old")

age += 1
print(age)

birthday = 1
age += birthday
print(age)

print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
    name = "heath" #local variable
    age = 30
    print("My name is " + name + " and i am " + str(age) + " years old")

who_am_i()

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #new line
    print('\n')

nl()
#CONDITONAL STATEMENTS - if/else

def drink(money):
    if money >= 2:
        return "You got yourself a drink"
    else:
        return "No drink for you"

print(drink(3))
print(drink(1))

def alcohol(age,money):
    if (age >= 21) and (money >= 5):
        return "were getting a drink"
    elif (age >= 21) and (money < 5):
        return "Come back with more money"
    elif (age < 21) and (money >= 5):
        return "Nice try kid"
    else:
        return "your too young and too poor."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()
#LISTS - have brackets []
movies = ["When harry met sally", "The hangover", "the Perks of Being a Wallflower", "The Exorcist"]
print(movies[1]) #returns the second number in the list
print(movies[0]) #returns the first number in the list
print(movies[1:3]) #returns the first index number given right until the last number, but not include the last number.
print(movies[0:]) #print entire list

print(len(movies))
movies.append('JAWS')
print(movies)

movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes last item
print(movies)
movies.pop(0) #removes first item

amber_movies = ["just go with it", "50 first dates"]
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["bob", 82],["Alice", 90],["Jeff", 73]]
bobs_grade = grades[0][1]
alice_grade = grades[1][1]
grades[0][1] = 83
print(grades)
print(bobs_grade)
print(alice_grade)

nl()
#Tuples - Do not change, (), not mutable (imutable)
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
#Looping

#for loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)

#while looks - execute as long as true
i = 1

while i < 10:
    print(i)
    i += 1

nl()
#advanced strings

my_name = "heath"
print(my_name[0])  #first letter
print(my_name[-1]) #last letter

sentence = "this is a sentence"
print(sentence[:4])
print(sentence.split()) #delimeter - default is space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "he said, give me all your money"
print(quote)

too_much_space = "              hello        "
print(too_much_space.strip())

print("A" in "Apple") #true
print("a" in "Apple") #false

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("my favorite movie is {}.".format(movie))
print("my favorite movie is %s" %movie)
print(f"My favorite movie is {movie}.")



nl()
#DICTIONARIES - key/value pairs {}

drinks = {"White Russian": 7, "Old Fasioned": 10, "Lemon Drop": 8} #drink is the key, price is the value
print(drinks)

employees = {"Finance" : ["bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"]}
print(employees)

employees['legal'] = ["Mr. Frond"] #adds new key value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key value pair
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get('White Russian'))

nl()
