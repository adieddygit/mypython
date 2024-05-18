str = "The quick brown fox jumps over the lazy dog"
print(str)

str = "The quick brown fox jumps over the lazy dog"
print(len(str))

str = "The quick brown fox jumps over the lazy dog"
print(str.upper())

str = "The quick brown fox jumps over the lazy dog"
print(str.lower())

str = "The quick brown fox jumps over the lazy dog"
print(str.title())

str = "The quick brown fox jumps over the lazy dog"
split_str = str.split()
split_str.reverse()
new_str = ' '.join(split_str)
print(new_str)

print(new_str.title())

str = "The quick brown fox jumps over the lazy dog"
number_of_a_in_str = str.count("a")
print(number_of_a_in_str)

str = "The quick brown fox jumps over the lazy dog"
number_of_the_in_str = str.count("the")
print(number_of_the_in_str)

str = "The quick brown fox jumps over the lazy dog"
str = str.replace("the", "a")
print(str)

str = "The quick brown fox jumps over the lazy dog"
dict = {}

for i in str:
    if i.isalpha():
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

print(dict)


people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

for people, sex, age in zip(people, sex, age):
    print(f'{people} the {sex} is {age} years old')