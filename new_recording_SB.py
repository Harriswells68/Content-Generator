from seleniumbase import SB
import requests
import re
import time

def generate_vlink(c):
    k=0

    while k<5:
        url = f"https://api.catchmail.io/api/v1/mailbox?address=ytprojectelevenlabsacckbkb{c}@catchmail.io"
        r = requests.request("GET", url).json()
        if r["count"]>0:
            url = f"https://api.catchmail.io/api/v1/message/{r["messages"][0]["id"]}?mailbox=ytprojectelevenlabsacckbkb{c}@catchmail.io"
            r = requests.request("GET", url).json()

            return re.findall(r"(https?://[^\s)]+)(?=\s\))", (r["body"]["text"]))[1]        
        else:
            k+=1
            time.sleep(4)
    
    raise Exception("ERRROR")

with SB(uc=True, test=True, locale_code="en", xvfb=True) as sb:
    sb.activate_cdp_mode("https://elevenlabs.io/app/sign-up")

    sb.sleep(3)
    sb.cdp.press_keys('input[name="email"]', "ytprojectelevenlabsacckbkb92947@catchmail.io")  # human-speed
    sb.cdp.press_keys('input[name="password"]', "Prince!4438#")

    # Standard syntax for clicking a button containing specific text in CDP Mode
    sb.cdp.click('div[data-testid="signup-signup-button-div"] button:contains("Sign up")')

    sb.sleep(0.5)

    sb.solve_captcha()

    sb.sleep(2)

    link=generate_vlink(92947)

    sb.save_screenshot("screenshots/after_captcha.png")

    sb.cdp.open(link)

    sb.sleep(5)
    sb.cdp.press_keys('input[name="password"]', "Prince!4438#")

    sb.save_screenshot("screenshots/login.png")

    # Standard syntax for clicking a button containing specific text in CDP Mode
    sb.cdp.click('#sign-in-form > div.relative.flex.items-center.justify-between.w-full.h-fit.mt-4 > div.relative.w-full > button:contains("Sign in")')

    


        
