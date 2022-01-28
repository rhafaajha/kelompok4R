from browser import document, alert  
import math

# Deklarasi Variable
data1 = document['data1']
data2 = document['data2']
button = document['btn']
output = document['output']

# Dictionary
type1 = {'hitung': lambda TB, BB: round(BB / ((TB/100) ** 2), 1),
         'data1': 'Tinggi Badan (cm)', 'data2': 'Berat Badan (kg)'}

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
            data1.value = temp
            return temp
        else:
            return temp

# Fungsi untuk memanggil formula pada dictionary
def hitung(num1, num2):
    for key in type1.keys():
        return type1['hitung'](num1, num2)

# Fungsi Main
def main(ev):
    num1 = getNum(data1.value)
    num2 = getNum(data2.value)
    result = hitung(num1, num2)
    output.textContent = str(result)

# Fungsi keyEnter
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

button.bind('click', main)  # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketika keyboard ditekan pada salah satu input field
data1.bind("keypress", keyEnter)
data2.bind("keypress", keyEnter)
