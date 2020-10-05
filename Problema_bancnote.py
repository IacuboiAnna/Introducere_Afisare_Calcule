#De la tastatura se introduce o suma in lei.
#Determinati numarul minim de bancnote necesare, stiind ca 
#in Republica Moldova avem bancnote de 1000,500,200,100,50,20,10,5,2,1
s=int(input("Dati suma in lei:"))
num_1000=s//1000
num_500=(s%1000)//500
num_200=((s%1000)%500)//200
num_100=(((s%1000)%500)%200)//100
num_50=((((s%1000)%500)%200)%100)//50
num_20=(((((s%1000)%500)%200)%100)%50)//20
num_10=((((((s%1000)%500)%200)%100)%50)%20)//10
num_5=(((((((s%1000)%500)%200)%100)%50)%20)%10)//5
num_2=((((((((s%1000)%500)%200)%100)%50)%20)%10)%5)//2
num_1=((((((((s%1000)%500)%200)%100)%50)%20)%10)%5)%2
print(num_1000,"de 1000.",num_500,"de 500.",num_200,"de 200.",num_100,"de 100.",num_50,"de 50.",num_20,"de 20.",num_10,"de 10.",num_5,"de 5.",num_2,"de 2.",num_1,"de 1.")
print("Numarul minim de bancnote este",num_1000+num_500+num_200+num_100+num_50+num_20+num_10+num_5+num_2+num_1)
