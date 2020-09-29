#Într-o tabără numărul de băieţi este cu 10 mai mare decât cel al fetelor. 
# Dacă se citeşte de la tastatură numărul de fete, să se spună câţi elevi sunt în tabără. 
# Exemplu: date de intrare: 50  date de ieşire: 110.
num_fete=int(input("Dati numarul de fete:"))
num_baieti=10+num_fete
num_elevi=num_fete+num_baieti
print("Numarul de elevi din tabara este:", num_elevi)
