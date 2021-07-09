from bs4 import BeautifulSoup
import requests
import codecs
import json
import time
import time

cooks = input("Enter your cookie: ")
refer = input("Enter website url: ")
headers = {
    'Host': 'admissions.nu.edu.kz',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': '' + refer + '',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Cookie': '' + cooks +  ''
}

# for itera in main_result:

while(1):
    print("--------------------------------------------------------")
    r = requests.get('' + refer + '', headers=headers).text
    r = ''.join(r.split())


    stri = "OfferLetterCabinetPortletObjectId=null"

    if stri in r: 
        print('Еще не вышло!')
    else:
        print('Резы вышли!')
    time.sleep(2)
    
