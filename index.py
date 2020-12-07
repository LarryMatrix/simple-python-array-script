my_arr = [
    {
        "id": "0dc240e2-0b7c-4005-b792-07369d562644",
        "active": True,
        "user_profession_type": 'sub'
    },
    {
        "id": "0dc240e2-0b7c-4005-b792-07369d5654657",
        "active": True,
        "user_profession_type": 'main'
    },
]

for item in my_arr:
    for key, value in item.items():
        if key == 'user_profession_type' and value == 'main':
            print('id', item.get('id'))
    # if 'main' in item.get('user_profession_type', None):
        # print('obj: ', item)
