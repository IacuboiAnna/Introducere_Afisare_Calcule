#Maria vrea să verifice dacă greutatea şi înălţimea ei corespund vârstei pe care o are. Ea
#a găsit într-o carte următoarele formule de calcul ale greutăţii şi înălţimii unui copil, v
#fiind vârsta : greutate=2*v+8 (în kg), înălţime=5*v+80 (în cm). Realizaţi un program
#care să citească vârsta unui copil şi să afişeze greutatea şi înălţimea ideală, folosind
#aceste formule. 
v=int(input("Dati varsta copilului:"))
greutate=(2*v)+8
inaltime=(5*v)+80
print("Greutatea ideala este ", greutate, "kg")
print("Inaltimea ideala este ", inaltime, "cm")