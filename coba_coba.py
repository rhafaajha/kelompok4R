from browser import document, alert  # Import Library Brython 
import math

# Deklarasi Variable
input1 = document['input1']
input2 = document['input2']
button = document['btn']
output = document['output']

# Dictionary untuk menyimapan variabel input1 dan input2
# untuk memudahkan saat pemanggilan keempat variabel secara berurut
input = {'1': input1,
         '2': input2}

# Dictionary Bangun Datar
type1 = {'formula': lambda TB, BB, x: (BB / ((TB/100)*(TB/100))), 'input1': 'Tinggi Badan (cm)', 'input2': 'Berat Badan (kg)'}

# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    temp = x
    # Convert string ke int
    try:
        temp = int(x)
    # Jika convert string ke int gagal (ValueError), maka convert ke float
    except ValueError:
        temp = float(x)
    finally:
        # Jika input (var temp) masih string (gagal convert ke int dan float),
        # maka munculkan alert dan return dengan variable kosong ('')
        if temp != '' and type(temp) is str:
            alert('Harap masukkan angka')
            temp = ''
            input1.value = temp
            return temp
        # Jika salah satu convert berhasil, maka return
        else:
            return temp

# Fungsi untuk memanggil formula pada dictionary
def formula(x, num1, num2):
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x]['formula'](num1, num2)

# Fungsi Main
# Dijalankan ketika button di-click atau tombol 'enter' ditekan
def main(ev):
    num1 = getNum(input1.value)
    num2 = getNum(input2.value)
    result = formula(num1, num2)
    output.textContent = str(result)

# Fungsi keyEnter
# Fungsi yang mengarahkan ke 'Fungsi Main' ketika tombol 'enter' ditekan
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)  # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketika keyboard ditekan pada salah satu input field
input1.bind("keypress", keyEnter)
input2.bind("keypress", keyEnter)
