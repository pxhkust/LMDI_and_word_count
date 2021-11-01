# spam_amount = 0
# print(spam_amount)
#
# spam_amount = spam_amount + 4
# if spam_amount > 0:
#     print("But I don't know Any spam")
#
# viking_song = "Spam" * spam_amount
# print(viking_song)
#
# print(type(spam_amount))
# print(type(19.95))
#
# print(5 // 2)
# print(6 // 2)
#
# hat_height_cm = 25
# my_height_cm = 190
# total_height_meters = (hat_height_cm + my_height_cm) / 100
# print("Height in meters", total_height_meters)
#
# print(min(1, 2, 3))
# print(max(1, 2, 3))
#
# print(abs(32))
# print(abs(-32))
#
# print(float(10))
# print(int(3.33))
# print(int("807") + 1)
#
# def least_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return min(diff1, diff2, diff3)
#
# print(least_difference(1, 10, 100),
#       least_difference(1, 10, 10),
#       least_difference(5, 6, 7))
#
# print(1, 2, 3, sep="<")
#
# def greet(who="Colin"):
#     print("hello", who)
#
# greet(who = "Kaggle")
#
# greet("world")
#
# def mult_by_five(x):
#     return 5 * x
#
# def call(fn, arg):
#     return fn(arg)
#
# def squared_call(fn, arg):
#     return fn(fn(arg))
#
# print(
#     call(mult_by_five, 1),
#     squared_call(mult_by_five, 1),
#     sep='\n',
# )
#
# def mod_5(x):
#     return x % 5
#
# print(
#     "which number is biggest?",
#     max(100, 51, 14),
#     "which number is the biggest modulo 5",
#     max(100, 51, 14, key=mod_5),
#     sep = '\n'
# )
#
# def round_to_two_places(num):
#     round_to_two_places = round(num, 2)
#     return round_to_two_places
# print(round_to_two_places(3.14159))
#
# x = True
# print(x)
# print(type(x))
#
# def can_run_for_president(age):
#     return age >= 35
#
# print("Can a 19_year_old run for president?", can_run_for_president(19))
# print("Can a 19_year_old run for president?", can_run_for_president(45))
#
# def is_odd(n):
#     return (n % 2) ==1
# print("Is 100 odd?", is_odd(100))
# print("Is 100 odd?", is_odd(-1))
#
#
#
#
#
# def inspect(x):
#     if x ==0 :
#         print(x, "is zero")
#     elif x > 0 :
#         print(x, "is positive")
#     elif x < 0 :
#         print(x, "is negative")
#     else:
#         print(x, "is unlike anything I have ever seen")
#
# inspect(0)
# inspect(-15)
#
#
# preimes = [2, 3, 5, 7]
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#
# hands = [
#     ["j", "Q", "K"],
#     ["2", "2", "2"],
#     ["6", "A", "K"]]
#
# print(planets[0])
# planets[3] = "Malacandra"
# print(planets)
# print(len(planets))
# print(sorted(planets))
# primes = [2, 3, 5, 7]
# print(max(primes))
#
# planets.append("pluto")
# print(planets)
# print(planets.pop())
# planets.index("Earth")
#
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# for planet in planets:
#     print(planet, end = " ")
#
# multiplicands = (2, 2, 2, 3, 3, 5)
# product = 1
# for mult in multiplicands:
#     product = product * mult
# print(product)
#
# for i in range(5):
#     print("Doing important work. i =", i)
#
# i = 0
# while i <10:
#     print(i, end="")
#     i += 1
#
# squares = [n**2 for n in range(10)]
#
# print(squares)
#
# squares1 = []
# for n in range(10):
#     squares1.append(n**2)
#
# short_planets = [planet for planet in planets if len(planet) < 6]
# print(short_planets)
# loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
# loud_short_planets
#
# def count_negatives(nums):
#     n_negative = 0
#     for num in mums:
#         if num < 0:
#             n_negative = n_negative+1
#     return n_negative
#
# x = 'Pluto is a planet'
# y = "Pluto is a planet"
# print(x == y)
#
# hello = "hello\nworld"
# print(hello)
#
# numbers = {"one": 1, "two": 2, "three": 3}
# print(numbers["one"])
#
# numbers["eleven"] = 11
# print(numbers)
#
# numbers["one"] = "pluto"
# print(numbers)
#
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
#
# planet_to_initial = {planet: planet[0] for planet in planets}
# print(planet_to_initial)
#
# for k in numbers:
#     print("{} = {}".format(k, numbers[k]))
#
# print(" ".join(sorted(planet_to_initial.values())))
#
# for planet, initial in planet_to_initial.items():
#     print("{} begins with \"{}\"".format(planet.rjust(10), initial))

def word_search(documents, keyword):
    indices = []
    for i, doc in enumerate(documents):
        tokens = doc.split()
        normalized = [token.rstrip('.,') for token in tokens]
        if keyword in normalized:
            indices.append(i)
    return indices


def multi_word_search_dic(documents, keywords):
    multi_word_search_dic = {}
    for _keywords in keywords:
        multi_word_search_dic[_keywords] = word_search(documents, keywords)
    return multi_word_search_dic


doc_list1 = ["The Learn Python Challenge casino.", "they bought a car and a casino", "casinoville"]
keywords1 = ["casino", "they"]
result2 = multi_word_search_dic(doc_list1, keywords1)
print("result", result2)


