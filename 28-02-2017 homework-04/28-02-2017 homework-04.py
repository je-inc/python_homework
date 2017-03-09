print("Hello world!")
number = 2017.38
str1 = "Hello"
str2 = 'world'
total = "{}, {} - {}!".format(str1, str2, int(number))
print(total)
print(str(str1) + ", " + str(str2) + " - " + str(int(number)) + "!")
print(str1, ", ", str2, " - ", int(number), "!", sep="")

my_list = [
    29,
    True,
    "my string one",
    [
        30,
        False,
        "my string two"
    ],
    {
        'number': 31,
        'boolem': True,
        'string': "my string three"
    }
]
print(my_list[1], my_list[3][:2], my_list[4]['string'], sep=", ")

str_turn = "123.456"
str_turn_int = int(float(str_turn))
str_turn_float = float(str_turn_int)
print(str_turn_float, type(str_turn_float))

num_turn = 93735
num_turn_float = float(num_turn)
num_turn_str = str(num_turn_float)
print(num_turn_str, type(num_turn_str))