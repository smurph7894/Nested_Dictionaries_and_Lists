from dataclasses import replace


x = [ [5,2,3], [10,8,9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20}]


#1.a.
x[1][0] = 15

print(x[1])

#b. 
def replace_last_name (old_last_name, new_last_name):
    for person in students:
        if person['last_name'] == old_last_name:
            person['last_name'] = new_last_name
            
            
replace_last_name('Jordan', 'Bryant')
print (students)

#c.
def change_sports_player (old_name, new_name):
    for sport_players in sports_directory.values():
        # print("sport_players: " + str(sport_players))
        for player_name in sport_players:
            # print("player_name: " + str(player_name))
            if player_name == old_name:
                # print("Name Match")
                player_location = sport_players.index(player_name)
                # print(player_location)
                sport_players[player_location] = new_name

change_sports_player("Messi", "Andres")

print(sports_directory)

#d.
def change_num_value(original_value, new_value):
    for letter_needed in z:
        if letter_needed['y'] == original_value:
            letter_needed['y'] = new_value

change_num_value(20, 30)

print(z)


#2. 

def iterate_Dictionatry(some_list):
    for dictionaries_given in some_list:
        # print("dictionary_given: " + str(dictionaries_given) )
        i = 0
        for dictionary_key, dictionary_value in dictionaries_given.items():
            print (dictionary_key, "-", dictionary_value, end ="" )
            i = i + 1
            if i == len(dictionaries_given)-1:
                print( ", ", end="")
        print("")
iterate_Dictionatry(students)

#3
def iterateDictionary2(key_name, some_list):
    for dictionary_given in some_list:
        # print("dictionary_given:" + str(dictionary_given))
        # print("dictionary keys:" + str(dictionary_given.keys()))
        for dictionary_key, dictionary_value in dictionary_given.items():
            # print("key:" +str(dictionary_key))
            if dictionary_key == key_name:
                print(dictionary_value)

iterateDictionary2('last_name', students)
iterateDictionary2('first_name', students)


#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for dic_key, dic_value  in some_dict.items():
        print(len(dic_value), " ", end ="")
        print(dic_key)
        for dictionary_values in dic_value:
            print(dictionary_values)


printInfo(dojo)