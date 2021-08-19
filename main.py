import phonenumbers
from phonenumbers import carrier

# Built in function for country name
from phonenumbers import geocoder

def service_provider_details(number):
    # Provide service provider details

    service_number = phonenumbers.parse(number,"RO")
    print("Service Provider : ",end="")
    print(carrier.name_for_number(service_number,"en"))

def country_history(number):
    
    # In CH ( C is for country and H is for history)
    ch_number = phonenumbers.parse(number,"CH")

    print(f"Phone Number : {number}")
    print("Country : ",end="")
    print(geocoder.description_for_number(ch_number,"en"),)

def get_details():
    number = input("Enter your valid number along with country code : ")

    country_history(number)
    service_provider_details(number)


if __name__ == '__main__':

    # Main-driver function
    get_details()    