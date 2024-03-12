capitals = {
    'USA': 'Washington DC',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Ukraine': 'Kyiv'
}

# print(capitals)
# print(capitals['Germany']) Results in error
# print(capitals.get('Germany')) Returns none if not found
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#     print(f'{key} => {value}')

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'Ukraine': 'Odessa'})
capitals.pop('China')
# capitals.pop('Germany')
print(capitals.items())
