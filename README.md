# RoPy
Fast & Very Simple

## Examples
### Check 🍪
It use's the balance method to check or authorize account validity
```py
# bot = RoPy() 
# bot

YourCookie = ""
YourCookie

if RoPy().Login(roblo_security = YourCookie):
   print('Valid Cookie')
```
### Register 🍪
Can create roblox accounts using requests, but you need to generate a funcaptcha code.

#### Requirements
```
- FunCaptcha Code
- Valid Username
- Valid Password
```
################
```py
import string
import random

# bot = RoPy()
# bot

funCaptchaCode = "" # Accessible from (https://roblox-captcha-v2.herokuapp.com/)
funCaptchaCode

if __name__ == "__main__":
   print(RoPy().Register(
                user_name = "".join(random.choice(string.ascii_lowercase) for x in range(20)),
                pass_word = "".join(random.choice(string.ascii_lowercase) for y in range(20)),
                
                fun_captcha = funCaptchaCode
   ))
```
