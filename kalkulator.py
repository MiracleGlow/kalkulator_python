import re

def operasi(expression):
    try:
        hasil = eval(expression)
        return str(hasil)
    except Exception as e:
        return "Error"

def logika(input_nilai):
    input_nilai = input_nilai.lower()
    if re.match(r'^[\d\+\-\*/\(\) ]+$', input_nilai):
        return "hasilnya adalah : " + str(operasi(input_nilai))

print("Kalkulator Python Regex")
while True:
    input_nilai = input("Masukan Nilai Operasi : ")
    jawaban = logika(input_nilai)
    print(jawaban)