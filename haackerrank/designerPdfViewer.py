def designerPdfViewer(h, word):
    indexLetter = "abcdefghijklmnopqrstuvwxyz"
    height = []
    for char in word:
        indeks = indexLetter.index(char)
        height.append(h[indeks])

    return max(height)*len(word)

designerPdfViewer([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7], "zaba")