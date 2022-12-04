import random

print("Loaded")


def generateCaptcha(n):
    chrs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    captch = ""
    while (n):
        captch += chrs[random.randint(1,1000)%62]
        n -= 1
    return captch

captcha=generateCaptcha(9)
print(captcha)

def checkCaptcha(captcha, user_captcha):
    if captcha == user_captcha:
        return True
    return False
    
if (checkCaptcha(captcha,input())):
    print("Captch Matched")
    print("Success")
else:
    print("Captcha Not Matched")