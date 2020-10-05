#Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
#aceste cifre luate o singură dată. Exemplu : date de intrare : 3 4 2 Date de ieşire : 324
#342 243 234 432.
a=int(input("introduceti prima cifra:"))
b=int(input("introduceti a doua cifra:"))
c=int(input("introduceti a treia cifra:"))
print((a*100)+(b*10)+c, (a*100)+(c*10)+b, (b*100)+(a*10)+c, (b*100)+(c*10)+a, (c*100)+(b*10)+a)