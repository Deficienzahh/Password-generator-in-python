import random 


lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
simbols = "*+@$%&£!§-:_"



print ('Ciao questo tool offre la possibilità di creare password con due diversi livelli di difficolta.')

if input ('Desideri creare una password semplice o complessa? (S/C)') == "C":
    use_for = lower_case + upper_case + numbers + simbols
    lenght_for_pass = 20
else: 
    use_for = lower_case + numbers
    lenght_for_pass = 8


password = "".join(random.sample(use_for, lenght_for_pass))

print ("your generated password is", password)