with open('file.txt', 'w', encoding="utf-8") as f:
    f.write("Juan,123456,25\n")
    f.write("Pedro,789012,31\n")
    f.write("Maria,555555,22\n")
    
with open('file.txt', 'r', encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())