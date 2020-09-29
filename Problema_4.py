#Un brăduţ este împodobit cu globuleţe albe, roşii şi albastre. 
# Numărul globuleţelor albe se citeşte de la tastatură. 
# Câte globuleţe are brăduţul, ştiind că 
# numărul de globuleţe roşii este cu 3 mai mare decât numărul de globuleţe albe, 
# iar globuleţele albastre sunt cu 2 mai puţine decât totalul celor albe şi roşii. 
# Exemplu: Date de intrare: 12 Date de ieşire: 52.
numgl_albe=int(input("Dati numarul de globulete albe:"))
numgl_rosii=3+numgl_albe
numgl_albastre=(numgl_albe+numgl_rosii)-2
numgl_total=numgl_albe+numgl_rosii+numgl_albastre
print("Bradutul are:", numgl_total, "globulete")
