users_info = [
    {
        'name': 'Ram',
        'age': 25,
        'profession': 'Engineer'
    },
    {
        'name': 'Shyam',
        'age': 30,
        'profession': 'Doctor'
    },
    {
        'name': 'Hari',
        'age': 35,
        'profession': 'Artist'
    }
]

younger_than_30 = [user for user in users_info if user['age'] < 30]
print(younger_than_30)