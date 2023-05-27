with open("markalar.txt","a") as file:
    file.write("opel")

with open("markalar.txt","r+", encoding="utf-8") as file:
    markalar = file.read()
    markalar = "wolswogen\n"+markalar
    file.seek(0)
    file.write(markalar)


with open("markalar.txt") as file:
    print(file.read())