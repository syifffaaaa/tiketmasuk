total = 0
while True:
    umur = input('Masukkan Umur : ')
    if umur == '':
        uang = int(input('Masukkan uang : '))
        if uang < total:
            print('Uang anda tidak mencukupi!')
        else:
            kembalian = uang - total
            print(f'''
Total Tiket = {total}
Uang Yang dimasukkan = {uang}

Running Kembalian : {kembalian}

''')
        break
    elif umur.isdigit():
        umur = int(umur)
        if umur <= 2:
            harga = 0.00
        elif 3 <= umur <= 12:
            harga = 14.00
        elif umur >= 65:
            harga = 18.00
        else:
            harga = 23.00
        total += harga
        print(f'''
Harga : ${harga}
Running Total : {total}
''')
    else:
        print("Masukan umur tidak valid. Silakan coba lagi.")