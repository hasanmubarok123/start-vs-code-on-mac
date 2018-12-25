# Hallo teman-teman, jadi ini adalah program saya yang sangat cantik, saya menemukannya sendiri

def pickingNumbers(a):
    kumpulan = []
    a.sort()
    while len(a) != 0:
        # elemen pertama digunakan sebagain pengetes
        pengetes = a[0]
        #mengumpulkan semua elemen yang selisihnya kurang dari satu
        group = [item for item in a if abs(item - pengetes) <= 1]
        #memasukkan list yang sudah terkumpul elemennya tadi untuk diappend ke list yang akan menampung semuanya di kumpulan
        kumpulan.append(group)
        #Nah, di a, kita hapus semua elemen yang sudah tertampung, dan hanya menyisakan elemen yang belum
        a = [element for element in a if element not in group]
    
    pasangan = {}
    for item in kumpulan:
        pasangan[str(item)] = len(item)

    print(max(pasangan.values()))

        

pickingNumbers([1,1,2,2,4,4,5,5,5,32,45,45,46])