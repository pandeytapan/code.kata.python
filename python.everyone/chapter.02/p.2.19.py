month_name = "JanFebMarAprMayJunJulAugSepOctNovDec"

month_num = int(input("Enter the month number: ")) - 1
print (f"Month number {month_num + 1} is {month_name[3 * month_num : 3 * month_num + 3]}")
