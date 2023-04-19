message = input("ведите сообщение: ")
length = len(message)
cipher = f"\033[34m\033[43m{message}\033[0m"
print(cipher)
print(length) 
print(f"""Первая буква слова:{message[0]}
Последние буква слове:{message[-1]}
Первые три симлова строки:{message[:3]}
Последни три симлова строки: {message[-3:]}""")
first_shifr = message.replace('а','т')
first_shifr = first_shifr.replace('в','е')
first_shifr = first_shifr.replace('т','р')
first_shifr = first_shifr.replace('к','т')
first_shifr = first_shifr.replace('о','х')
print(f"Первый шифр-{first_shifr}")
second_shifr = message[::-1]
print(f"Второй шифр-{second_shifr}")
third_shifr = message[::2]+message[1::2]
print(f"третий шифр-{third_shifr}")
first_letter = message[0]
last_letter = message[-1]
quarter_shrift = last_letter + message[1:length-1] + first_letter
print(f"четвёртый шрифт-{quarter_shrift}")
half_length = length//2
fifth_shrift = message[half_length:] + message[:half_length]
print(f"пятый шрифт-{fifth_shrift}")
decipher_one = first_shifr.replace('т','а')
decipher_one = decipher_one.replace('е','в')
decipher_one = decipher_one.replace('р','т')
decipher_one = decipher_one.replace('т','к')
decipher_one = decipher_one.replace('х','о')
print(f"расшифровока 1 шрифта-{decipher_one}")
decipher_two = second_shifr[::-1]
print(f"расшифровока 2 шрифта-{decipher_two}")
decipher_three = ""
if length%2 == 1:
    half_length+=1
tmp_string_one = third_shifr[:half_length]
tmp_string_two = third_shifr[half_length:]
for symbol in range(len(tmp_string_one)):
    decipher_three += tmp_string_one[symbol]
    if symbol < len(tmp_string_two):
        decipher_three += tmp_string_two[symbol]
print(f"расшифровока 3 шрифта-{decipher_three}")
first_letter = quarter_shrift[0]
last_letter = quarter_shrift[-1]
decipher_four = last_letter + quarter_shrift[1:length-1] + first_letter
print(f"расшифровока 4 шрифта-{decipher_four}")
decipher_five = fifth_shrift[half_length:] + fifth_shrift[:half_length]
print(f"расшифровока 5 шрифта-{decipher_five}")
