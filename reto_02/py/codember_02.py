mensaje = r'&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&'
entrada = '&##&*&@& '

res_txt = ''
res_num = 0

for element in mensaje:
    if element == '#': res_num += 1
    elif element == '@': res_num -= 1
    elif element == '*': res_num *= res_num
    elif element == '&': res_txt += str(res_num)

print(res_txt)
