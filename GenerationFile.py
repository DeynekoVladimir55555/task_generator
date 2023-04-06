from random import choice, randint
import GenerationFunctions, TranslateFunctions


def print_question(difficulty, in_types):
    #Генерация условия задачи
    typ = GenerationFunctions.generation_type(in_types)
    t = types[typ]
    #Генерация 1 типа
    if typ == 1:
        numbers = GenerationFunctions.generation_type_1(difficulty)
        #
        answer = TranslateFunctions.translate_from_ten(numbers[0], numbers[2])
        if numbers[1] != 10:
            numbers[0] = TranslateFunctions.translate_from_ten(numbers[0], numbers[1])
        resoult = str(numbers[0])

        task = html_format(t[0] + str(numbers[1]) + t[1] + str(numbers[2]) + t[2], resoult)
        return [task, answer]
    #Генерация 2 типа
    elif typ == 2:
        numbers = GenerationFunctions.generation_type_2(difficulty)
        line = ''
        resoult = ''
        for i in range(len(numbers)):
            elem = numbers[i]
            line += str(elem[0]) + ' ' + elem[2] + ' '
            if elem[1] != 10:
                numbers[i][0] = TranslateFunctions.translate_from_ten(elem[0], elem[1])
            resoult += str(numbers[i][0]) + indexes[elem[1]] + ' ' + numbers[i][2] + ' '
        answer = eval(line[:-3])
        task = html_format(t[0], resoult[:-3], t[1])
        return [task, str(int(round(answer, 0)))]

#Постоянные переменные
types = {1: ['Переведите данное число из ', '-ой системы счисления в ', '-ую систему счисления:'],
         2: ['Вычислите значение выражения:', '''Ответ запишите в 10-ой системе счисления. Если понадобится, округлите до целых.''']}

indexes = {10: u'\u2081\u2080', 2: u'\u2082',
           3: u'\u2083', 4: u'\u2084', 5: u'\u2085',
           6: u'\u2086', 7: u'\u2087', 8: u'\u2088',
           9: u'\u2089'}
def html_format(question1, details, question2=''):
    base_question = '<p class="question">' + question1 + '</p><p class="details">' + details + '</p>'
    if question2 != '':
        base_question += '<p class="question">' + question2 + '</p>'
    return base_question
