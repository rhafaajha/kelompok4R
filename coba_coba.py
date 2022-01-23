from browser import document, alert  
import math

# Deklarasi Variable
input1 = document['input1']
input2 = document['input2']
button = document['btn']
output = document['output']

# Dictionary
type1 = {'formula': lambda TB, BB: round(BB / ((TB/100) ** 2), 1),
         'input1': 'Tinggi Badan (cm)', 'input2': 'Berat Badan (kg)'}

# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan data yang sesuai!!!')
            temp = ''
            input1.value = temp
            return temp
        else:
            return temp

# Fungsi untuk memanggil formula pada dictionary
def formula(num1, num2):
    for key in type1.keys():
        return type1['formula'](num1, num2)

# Fungsi Main
def main(ev):
    num1 = getNum(input1.value)
    num2 = getNum(input2.value)
    result = formula(num1, num2)
    output.textContent = str(result)

# Fungsi keyEnter
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)  # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketika keyboard ditekan pada salah satu input field
input1.bind("keypress", keyEnter)
input2.bind("keypress", keyEnter)
