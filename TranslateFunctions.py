#Перевод из 10 системы счисления
def translate_from_ten(number, sistem):
    res = ''
    while number > 0:
        res += str(number % sistem)
        number //= sistem
    return res[::-1]

#Перевод в 10 систему счисления
def translate_to_ten(number, sistem):
    res = 0
    k = 0
    for elem in str(number)[::-1]:
        res += int(elem) * sistem ** k
        k += 1
    return res

def translate_to_db(difficulty, in_types):
    if difficulty == 'Легко':
        d = 1
    elif difficulty == 'Нормально':
        d = 2
    else:
        d = 3
    types = []
    if in_types[0] == 'on':
        types.append('True')
    else:
        types.append('False')
    if in_types[1] == 'on':
        types.append('True')
    else:
        types.append('False')

    return d, types


def translate_to_ui(difficulty, types):
    if difficulty == 1:
        d = 'Легко'
    elif difficulty == 2:
        d = 'Нормально'
    else:
        d = 'Сложно'
    if types[0] == 'True':
        types[0] = 'on'
    else:
        types[0] = 'off'
    if types[1] == 'True':
        types[1] = 'on'
    else:
        types[1] = 'off'

    return d, types
