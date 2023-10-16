def parsing(json_str: dict, keyword_callback, required_fields=None, keywords=None):
    for key, value in json_str.items():
        if key in required_fields:
            for word in keywords:
                if value.index(word) != -1:
                    print(keyword_callback(word))


def read_fields():
    result = set()
    field = ''
    print("Введите значения нужных полей (в конце напишите end): ")
    while field != 'end':
        field = input()
        result.add(field)
    return result


def read_values():
    result = set()
    field = ''
    print("Введите нужные значения (в конце напишите end): ")
    while field != 'end':
        field = input()
        result.add(field)
    return result


def func(x: str):
    return x.upper()
