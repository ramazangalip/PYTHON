with open("newfile.txt","w",encoding="utf-8") as file:
 file.write("ramazan")
 file.write("galip")
 print(file)

with open("newfile.txt") as file:
    print(file.read())