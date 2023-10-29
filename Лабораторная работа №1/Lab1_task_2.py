# TODO Найдите количество книг, которое можно разместить на дискете

stranic = 100
strok = 50
simvolov = 25
volume_disk = 1.44
volume_sim = 4 #Байт

odna_kniga = strok*simvolov*stranic*volume_sim #Объем одной книги байт
v = float(volume_disk*1024*1024)
count = int(v // odna_kniga)
print("Количество книг, помещающихся на дискету:", count)