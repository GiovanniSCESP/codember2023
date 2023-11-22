print([clave for clave in [linea.replace(':','').split() for linea in open(r'..\file.txt').read().splitlines()] if not [int(wrd) for wrd in clave[0].split('-')][0] <= len([wrd for wrd in clave[2] if wrd == clave[1]]) <= [int(wrd) for wrd in clave[0].split('-')][1]][41])

# with open(r'..\file.txt', 'r') as f:
#     values = f.read()

# claves = [linea.replace(':','').split() for linea in values.splitlines()]
# i = 0
# for clave in claves:
#     var_min, var_max = [int(wrd) for wrd in clave[0].split('-')]
#     letter = clave[1]
#     chain = clave[2]

#     value = len([wrd for wrd in chain if wrd == letter])

#     if var_min <= value <= var_max:
#         ...
#     else:
#         i += 1
#         if i == 42: print(clave)

