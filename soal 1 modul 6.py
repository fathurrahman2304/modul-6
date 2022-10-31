def rata(a = 0, nilai = 0, c = 0):
    while (a != ''):
        a = str(input('masukan nilai : '))
        c +=1
        if (a.upper() == "A"):
            print('nilai = 4')
            nilai += 4
        elif (a.upper() == 'A-'):
            print('nilai = 3.75')
            nilai +=3.75
        elif (a.upper() == 'B+'):
            print('nilai = 3.5')
            nilai += 3.5
        elif (a.upper() == 'B'):
             print('nilai = 3.5')
             nilai += 3
        elif (a.upper() == 'B-'):
              print('nilai = 2.75')
              nilai += 2.75
        elif (a.upper() == 'C+'):
              print('nilai = 2.5')
              nilai += 2.5
        elif(a == ''):
            if(c == 1):
                return 0
            else:
                return nilai/(c - 1)
        else:
            c -=1
            print("masukan nilai yang benar")
            
rerata = rata()
print ("rata-ratanya adalah: ", rerata)
