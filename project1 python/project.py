# Project : OTP Generator 
# generate a 6 character OTP

import random as r
import string
length=6
otp = ''
Character = string.ascii_letters + string.digits
print(Character)

for i in range(length):
   otp = otp + r.choice(Character)

print("OTP: ",otp)