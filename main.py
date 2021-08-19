import phonenumbers
from phonenumbers import carrier

# Built in function for country name
from phonenumbers import geocoder

def service_provider_details(number):
    # Provide service provider details
    try:
        service_number = phonenumbers.parse(number,"RO")
        print("Service Provider : ",end="")
        if(carrier.name_for_number(service_number,"en") != ""):
            print(carrier.name_for_number(service_number,"en"))
        else:
            print("Entered number is wrong or no details of service provider is registered")

    except:
        print("Does not seems like a valid number enter valid number")


def country_history(number):
    
    try:
    
        # In CH ( C is for country and H is for history)
        ch_number = phonenumbers.parse(number,"CH")

        print(f"Phone Number : {number}")
        print("Country : ",end="")

        if((geocoder.description_for_number(ch_number,"en")) != ""): 
            print(geocoder.description_for_number(ch_number,"en"),)
        else:
            print("Entered number is wrong /country code is missing no details of country is registered")

    except:
        print("Does not seems like a valid number enter valid number")
        exit(0)

def get_details():
    number = input("Enter your valid number along with country code : ").replace(" ","")

    country_history(number)
    service_provider_details(number)


if __name__ == '__main__':

    # Main-driver function
    get_details()    
