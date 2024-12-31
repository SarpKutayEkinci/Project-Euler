def euler1():
    #küme problemlerindeki gibi 3ün katları ve 5in katlarını topladım bu durumda 3 ve 5in katlarında fazladan 15in katları kısmını topladığımızdan 15in katları kümesini 1 çıkardım
    sum=0
    UPPERLIMIT=int(input("üst limiti belirleyiniz: "))
    for i in range(1,UPPERLIMIT):
        if i%3==0:
            sum+=i
        if i%5==0:
            sum +=i
        if i%15==0:
            sum-=i
    print(sum)
def euler2():
    ENDLIMIT=4000001 #as a advancement in the code you or ı could take the limit by the user 
    fib1=1
    fib2=1
    sum=0
    while fib2<ENDLIMIT: #fibonacci kuralı gereği fibi fib1+fib2 yaptım sonra fib1 i fib2 fibide fib2 yaptım ilerlemesi için sonra even olma durumunu kontrol edip sum accumulatoruna ekledim
        fib=fib1+fib2
        fib1=fib2
        fib2=fib
        if fib%2==0:
            sum+=fib
    print(sum)
def euler3():
    num = int(input("Sayı giriniz: "))
    prime_dividers = []  # Asal çarpanları tutacağımız liste
    
    # Bir sayının asal çarpanlarını bul
    divider = 2
    while num > 1:
        if num % divider == 0:  # Eğer sayı, divider'a tam bölünüyorsa
            prime_dividers.append(divider)
            num //= divider  # Sayıyı böldüğümüz çarpana indir
        else:
            divider += 1  # Eğer bölünmüyorsa bir sonraki sayıya geç

    print("Asal çarpanlar:", prime_dividers)
    print("En büyük asal çarpanı: ",max(prime_dividers))
def euler4():
    palindrome=[]
    LOWERLIMIT=100
    UPPERLIMIT=999
    max_palindrome_multiplier1=0
    max_palindrome_multiplier2=0
    for i in range(LOWERLIMIT,UPPERLIMIT+1):
        for j in range(LOWERLIMIT,UPPERLIMIT+1):
            product=i*j
            strproduct=str(product)
            reverse_strproduct=strproduct[::-1]
            if strproduct==reverse_strproduct:
                palindrome.append(product)  
    print(max(palindrome))
def euler4_2():
    max_palindrome=0
    LOWERLIMIT=100
    UPPERLIMIT=999
    max_palindrome_multiplier1=0
    max_palindrome_multiplier2=0
    for i in range(LOWERLIMIT,UPPERLIMIT+1):
        for j in range(LOWERLIMIT,UPPERLIMIT+1):
            product=i*j
            strproduct=str(product)
            reverse_strproduct=strproduct[::-1]
            if strproduct==reverse_strproduct:
                if product>max_palindrome:
                    max_palindrome=product
                    max_palindrome_multiplier1=i
                    max_palindrome_multiplier2=j
    print(max_palindrome_multiplier1,"", max_palindrome_multiplier2)
    print(max_palindrome)
