brands = ["Hermes", "Gucci", "Chanel", "Gucci",
           "Louis Vuitton", "Hermes", "Chanel","hugo boss", 
           "Guess", "Gucci", "Louis Vuitton"]

dict = {}

unique_values = (set(brands))

for i in unique_values:
        if i in dict:
            dict[i] = unique_values
        else:
            dict[i] = i[0]

print(dict)

original_dict = dict
reversed_dict = {}

for key, value in original_dict.items():
    if value not in reversed_dict:
        reversed_dict[value] = key

print(reversed_dict)
           
             

