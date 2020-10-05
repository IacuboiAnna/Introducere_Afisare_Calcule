#Măriuca ţine evidenţa iepurilor din crescătorie. Ea îşi notează câţi iepuri sunt la
#începutul fiecărei luni, câţi au murit şi câţi s-au născut în cursul fiecăei luni. Puteţi să
#realizaţi un program care, primind aceste date, să afişeze la sfârşitul fiecărei luni câţi
#iepuri sunt în crescătorie? Exemplu : Date de intrare : nr. Iepuri la început de luna 10
#nr. iepuri morti 2 nr. iepuri nascuti 6 Date de ieşire : 14 iepuri.
num_inc=int(input("Dati numarul de iepuri la inceput de luna:"))
num_mor=int(input("Dati numarul de iepuri morti:"))
num_nas=int(input("Dati numarul de iepuri ce s-au nascut:"))
print("La sfarsit de luna in crescatorie sunt",num_inc-num_mor+num_nas,"iepuri")