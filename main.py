# Get the last Key or Value in a dictionary in Python

my_dict = {
    'id': 1,
    'name': 'Bobby Hadz',
    'country': 'Belgium'
}

last_key = list(my_dict)[-1]
print(last_key)  # 👉️ country

print(my_dict[last_key]) # 👉️ Belgium

first_key = list(my_dict)[0]
print(first_key)  # 👉️ id