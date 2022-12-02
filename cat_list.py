from cat import Cat

cats = [
    {
     "name": "Семён",
     "gender": "мальчик",
     "age": 2,
    },
    {
     "name": "Сэм",
     "gender": "мальчик",
     "age": 2,
    },
    {
        "name": "Киса",
        "gender": "девочка",
        "age": 1,
    },
    {
        "name": "Лапа",
        "gender": "девочка",
        "age": 0,
    },
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)
    print(cat_obj.name)