import json

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)

# Output: ['English', 'French']
print(person_dict['languages'])

json_string = """{"a": 1, "b": 2, "c": 3}"""
a_dictionary = json.loads(json_string)

b_in_dict =  "blol" in a_dictionary
print(b_in_dict)