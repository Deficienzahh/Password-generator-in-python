import random 

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"


use_for = lower_case + upper_case + numbers 
lenght_for_pass = 8

password = "".join(random.sample(use_for, lenght_for_pass))

print ("your generated password is", password)