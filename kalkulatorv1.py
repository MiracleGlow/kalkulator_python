def hitung():
    if operasi == "+":
        return firstN + secondN
    elif operasi == "-":
        return firstN - secondN
    elif operasi == "*":
        return firstN * secondN
    elif operasi == "/":
        return firstN / secondN
    elif operasi == "":
        return print("Error : operasi tidak valid")
    elif firstN == "":
        return print("Error : nilai pertama tidak valid")
    elif secondN == "":
        return print("Error : nilai kedua tidak valid")

while True:
    print("Kalkulator")
    firstN = int(input("masukan nilai pertama : "))
    operasi = input("silahkan pilih operasi : ")
    secondN = int(input("masukan nilai ke dua :"))
    kalkulsasi = hitung()
    print("hasilnya adalah :", kalkulsasi)