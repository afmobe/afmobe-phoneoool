import phonenumbers
from phonenumbers import carrier,geocoder,timezone
from pystyle import *
print("Alert : ")
Write.Print("\n\tWrite exit For Exit",Colors.orange)
Write.Print("\n\tPlease Write Your Country International Calling Code Before The Number",Colors.red)
Write.Print("\n\tExample :\t+33672652366",Colors.blue)
while True:
    Write.Print("\nAfMoBe\t",Colors.orange)
    inp=input("Phone Num : ")
    try:
        num=phonenumbers.parse(inp,None)
        country=geocoder.description_for_number(num,"en")
        company_name_number=carrier.name_for_number(num,"en")
        continent_and_city=timezone.time_zones_for_number(num)
        print(num)
        if country=='':
            print("Country : Unknown")
        else:
            print('Country : ',country)
        if company_name_number=='':
            print("Company Name Number : Unknown")
        else:
            print("Company Name Number : ",company_name_number)
        if continent_and_city=='':
            print('Continent And City : Unknown')
        else:
            print("Continent And City : ",continent_and_city)
    except:
        print('')
    if inp=="exit":
        break
    else:
        continue