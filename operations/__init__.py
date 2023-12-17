from . import plus, minus, multiple, divide, power, sinus, cosinus, tan, cot, remaining, ln, factoriel, log
dictionary = {'+': plus, '-': minus, '*': multiple, '/': divide, '^': power, 'sin': sinus, '!!': factoriel,
              'cos': cosinus, 'tan': tan, 'cot': cot, 'ln': ln, 'log': log, '%': remaining}
importance_dictionary = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, 'sin': 4, '!!': 4, 'cos': 4, 'tan': 4,
                         'cot': 4, 'ln': 4, 'log': 4}
