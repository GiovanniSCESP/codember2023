print([nombre for nombre in [value.split('-') for value in open(r'..\file.txt', 'r').read().splitlines()] if ''.join([word for word in [word for word in nombre[0]] if [word for word in nombre[0]].count(word)==1]) == nombre[1]][32])

# with open(r'..\file.txt', 'r') as f:
#     values = f.read().splitlines()

# for nombre in values:
#     cadena, unchecksum = nombre.split('-')
#     letras = [word for word in cadena]
#     gen_unchecksum = ''.join([word for word in letras if letras.count(word)==1])
#     if gen_unchecksum == unchecksum:
#         print(gen_unchecksum)
