from tkinter import Tk
from tkinter.filedialog import askopenfilename
import numpy
import matplotlib.pyplot as plt

def reverse_number(n, alpha):
    binary = bin(n)
    binary_reverse = binary[-1:1:-1]
    number_reverse = binary_reverse + (alpha - len(binary_reverse))*'0'
    return int(number_reverse, 2)

def w_cos(k, N):
    return numpy.cos((2 * numpy.pi * k) / N)

def w_sin(k, N):
    return -numpy.sin((2 * numpy.pi * k) / N)

Tk().withdraw()
filename = askopenfilename()
print(filename)
f = open(filename, 'r')
data = f.readlines()

for a in range(0, len(data)):
    data[a] = float(data[a].replace('\n', ''))

a = 2
alpha = 1

while a < len(data):
    a = a * 2
    alpha += 1

input_data = []
for i in range(0, a):
    if i > len(data):
        input_data.append(0)
    input_data.append(data[i])

jumlah_data = a

# OUTPUT data pada grafik

fig = plt.figure(figsize=(6,4))
plt.plot(input_data)
plt.xlabel("Sequence (n)")
plt.ylabel("Amplitude")
plt.title("Input")

#DFT FUNCTION

input_data_DFT = input_data

e  = 0
e = e + 0j*e
hasil = []
complex_multiplication_dft = 0

for k in range(0, jumlah_data):
    for n in range(0, jumlah_data):
        e += input_data_DFT[n] * numpy.exp(-2j * numpy.pi * k * n / jumlah_data)
        complex_multiplication_dft += 1

    hasil.append(abs(e) / jumlah_data)
    e = 0 + 0j*e

input_data_DFT = hasil

# OUTPUT data pada grafik

fig = plt.figure(figsize=(6,4))
plt.plot(input_data_DFT)
plt.xlabel("Frekuensi (Hz)")
plt.ylabel("Amplitude")
plt.title("Output DFT")
plt.annotate("Complex Multiplication = " + str(complex_multiplication_dft), xy=(0, max(input_data_DFT)))

#FFT FUNCTION

input_data_FFT = input_data
input_data_FFT_real = 0
input_data_FFT_imag = 0
complex_multiplication_fft = 0
temp1 = 0
temp2 = 0
temp3 = 0

'''
# METODE BUTTERFLY 1

input_data_FFT = input_data

for p in range(0, alpha): # p sebagai STAGE Identifier
    perulangan = jumlah_data // 2**p # perulangan sebagai nilai tengah
    for k in range(0, 2**p): # k sebagai pengali dalam a(0) dan b(0)
        l = 0
        for j in range(perulangan * k, perulangan * k + perulangan): # j sebagai perulangan dalam a(0) dan b(0)
            if j < (perulangan * k + perulangan // 2):
                temp[j] = input_data_FFT[j] + input_data_FFT[j + perulangan // 2]
            else:
                temp[j] = (input_data_FFT[j - perulangan // 2] - input_data_FFT[j]) * w(l,  perulangan)
                l += 2**p
    input_data_FFT = list(temp)
    print(temp, input_data_FFT)
    temp = numpy.zeros(a)
    temp = temp + 0j*temp

# BIT REVERSAL dari data yang sudah diolah dengan metode butterfly
for i in range(0, len(input_data_FFT)):
    temp[i] = input_data_FFT[reverse_number(i, alpha)]
input_data_FFT = list(temp)

'''

'''
# BUTTERFLY

for p in range(0, alpha):
    perulangan = 2**(p+1)
    for k in range(0, jumlah_data//perulangan):
        if k % 2 == 0 :
            for l in range(perulangan * k, perulangan * (k + 1)):
                if l < perulangan * k + perulangan // 2 :
                    temp[l] = input_data_FFT[l] + input_data_FFT[l + perulangan//2]
                    print(p, k, perulangan, l, "GANJIL")
                else:
                    temp[l] = input_data_FFT[l - perulangan//2] - input_data_FFT[l]
                    print(p, k, perulangan, l, "GENAP")
            continue
        m = 0
        for l in range(perulangan * k, perulangan * (k + 1)):
            if l < perulangan * k + perulangan // 2:
                temp[l] = (input_data_FFT[l] + input_data_FFT[l + perulangan // 2]) * w(m, jumlah_data)
                print(p, k, perulangan, l, "GANJILa", m)
            else:
                temp[l] = (input_data_FFT[l - perulangan // 2] - input_data_FFT[l]) * w(m, jumlah_data)
                print(p, k , perulangan, l, "GENAPa", m)
            m += 2**(alpha - p - 2)
    for k in range(0, jumlah_data // perulangan):
        input_data_FFT[k] = temp[k]

    temp = numpy.zeros(jumlah_data)
    temp = temp + 0j * temp
    #print(input_data)
    #print(input_data)

#for i in range(0, len(input_data)):
#    input_data_FFT[i] = abs(input_data_FFT[i])

'''

'''
#BUTTERFLY

for p in range (alpha):
    temp = []
    jumlah_perulangan = 2**(p+1)
    nilai_tengah = int(jumlah_perulangan / 2)
    perulangan_awal = 0
    perulangan_akhir = jumlah_perulangan
    for k in range (int(jumlah_data/jumlah_perulangan)):
        m = 0
        for l in range (perulangan_awal, perulangan_akhir):
            if l < perulangan_awal + jumlah_perulangan / 2:
                temp1 = input_data_FFT[l + nilai_tengah] * w_cos(m, jumlah_data)
                temp2 = input_data_FFT[l + nilai_tengah] * w_sin(m, jumlah_data)
                temp3 = numpy.sqrt(temp1**2+temp2**2)
                temp.append(input_data_FFT[l] + temp3)
                complex_multiplication_fft += 1
                print(k, l, l + nilai_tengah, m, "a")
            else:
                temp1 = input_data_FFT[l] * w_cos(m, jumlah_data)
                temp2 = input_data_FFT[l] * w_sin(m, jumlah_data)
                temp3 = numpy.sqrt(temp1 ** 2 + temp2 ** 2)
                temp.append(input_data_FFT[l - nilai_tengah] - temp3)
                complex_multiplication_fft += 1
                print(k, l, l - nilai_tengah, m,  "b")
                m += 2**(alpha - p - 1)
        perulangan_awal = perulangan_awal + jumlah_perulangan
        perulangan_akhir = perulangan_akhir + jumlah_perulangan
        #if input_data_FFT == temp:
            #print("CAAK", len(input_data_FFT), len(temp))
    if input_data_FFT != temp:
        input_data_FFT = temp
        #print("CUUKK", len(input_data_FFT), len(temp))
'''

# BUTTERFLY
for i in range (alpha):
    jumlah_perulangan = 2 ** (i + 1)
    status1 = 0
    status2 = 0
    m = 0
    nilai_tengah = int(jumlah_perulangan / 2)
    for k in range (jumlah_data):
        if status1 == nilai_tengah:
            status2 = 1
        if status1 == jumlah_perulangan:
            status2 = 0
            status1 = 0
            m = 0
        if status2 == 1:
            input_data_FFT_real = input_data_FFT[k] * w_cos(m, jumlah_perulangan)
            input_data_FFT_imag = input_data_FFT[k] * w_sin(m, jumlah_perulangan)
            input_data_FFT[k] = numpy.sqrt(input_data_FFT_real ** 2 + input_data_FFT_imag ** 2)
            complex_multiplication_fft += 1
            m += 2 ** (alpha - i - 1)
        status1 += 1

    for k in range (jumlah_data):
        if status1 == nilai_tengah:
            status2 = 1
        if status1 == jumlah_perulangan:
            status2 = 0
            status1 = 0
        if status2 == 0:
            input_data_FFT[k] = input_data_FFT[k] + input_data_FFT[k + nilai_tengah]
            print(k, k + nilai_tengah)
        if status2 == 1:
            input_data_FFT[k] = input_data_FFT[k - nilai_tengah] - input_data_FFT[k]
            print(k, k - nilai_tengah)
        status1 += 1

# BIT REVERSAL

temp = numpy.zeros(len(input_data_FFT))
for i in range(0, len(input_data_FFT)):
    temp[i] = input_data_FFT[reverse_number(i, alpha)]
input_data_FFT = list(temp)

# OUTPUT data pada grafik

print(reverse_number(15,6))

fig = plt.figure(figsize=(6,4))
plt.plot(input_data_FFT)
plt.xlabel("Frekuensi (Hz)")
plt.ylabel("Amplitude")
plt.title("Output FFT")
plt.annotate("Complex Multiplication = " + str(complex_multiplication_fft), xy=(0, max(input_data_FFT)))

plt.show()