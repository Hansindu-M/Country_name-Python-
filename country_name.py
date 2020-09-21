#pip install phonenumbers

import phonenumbers

#geocoder: to know the specific

#location to that number

from phonenumbers import geocoder

phone_number = phonenumbers.parse("+14453678564")


#USA phone number example: +1**********
#SL phone number example: +94**********

#this will print the country name


print(geocoder.description_for_number(phone_number,'en'))

