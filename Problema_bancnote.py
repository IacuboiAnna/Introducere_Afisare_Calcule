#De la tastatura se introduce o suma in lei.
#Determinati numarul minim de bancnote necesare, stiind ca 
#in Republica Moldova avem bancnote de 1000,500,200,100,50,20,10,5,2,1
s=int(input("Dati suma in lei:"))
n_1000=s//1000
n_500=(s%1000)//500
n_200=((s%1000)%500)//200
n_100=(((s%1000)%500)%200)//100
n_50=((((s%1000)%500)%200)%100)//50
n_20=(((((s%1000)%500)%200)%100)%50)//20
n_10=((((((s%1000)%500)%200)%100)%50)%20)//10
n_5=(((((((s%1000)%500)%200)%100)%50)%20)%10)//5
n_2=((((((((s%1000)%500)%200)%100)%50)%20)%10)%5)//2
n_1=((((((((s%1000)%500)%200)%100)%50)%20)%10)%5)%2
print(n_1000,"de 1000.",n_500,"de 500.",n_200,"de 200.",n_100,"de 100.",n_50,"de 50.",n_20,"de 20.",n_10,"de 10.",n_5,"de 5.",n_2,"de 2.",n_1,"de 1.")
print("Numarul minim de bancnote este",n_1000+n_500+n_200+n_100+n_50+n_20+n_10+n_5+n_2+n_1)
