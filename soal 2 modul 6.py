print("This Program will determine the number of days of a given a month")
print("Enter -1 to stop the program")
def inifungsi(bulan = int(input("Enter the month(1-12): "))):
    while bulan >= 0 or bulan < -1:
        if bulan >= 13 or bulan == 0 or bulan < -1:
            print(f"Invalid value entered : {bulan}")
        elif bulan in (1,3,5,7,8,10,12):
            print("There are 31 days in the month")
        elif bulan in (4,6,9,11):
            print("There are 30 days in the month")
        elif bulan == 2:
            tahun = int(input("Please enter the year (e.g., 2021): "))
            if (tahun % 4 == 0 ):
                    print("There are 29 days in the month")
            else:
                    print("There are 28 days in the month")
        print("Enter -1 to stop the program")
        bulan = int(input("Enter the month(1-12): "))
    while bulan == -1:
        b = "Terima kasih telah menggunakan program saya. Sampai berjumpa lagi"
        return b
    
print(inifungsi())