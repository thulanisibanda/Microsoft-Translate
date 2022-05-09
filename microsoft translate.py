import pandas as pd
import json
import requests
import base64
import os
import datetime
import asyncio
from aiohttp import ClientSession
import urllib.parse

pd.options.mode.chained_assignment = None
path = os.getcwd()
files = os.listdir(path)
files_xls = [f for f in files if f[-4:] == 'xlsx' and f[:2] != '~$']
if not os.path.exists("processed"):
    os.mkdir("./processed")


UserAuthentication = base64.b64encode(str.encode("username:password"))

#portal translate setup
portalTranslateUrl = "https://env-test.apigee.net/get-portal-translations?"

#mts translate setup
microsoftTranslateUrl = "https://env-dev.apigee.net/ade/v1/translate-document"

headers = {
            'Authorization': 'Basic '+ UserAuthentication.decode(),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }

langs = {
        "english": "en",
        "german": "de",
        "spanish": "es",
        "french": "fr",
        "brazilian portuguese": "pt-br",
        "italian": "it",
        "czech": "cs",
        "polish": "pl",
        "indonesian": "id",
        "thai": "th",
        "finnish":"fi",
        "hungarian":"hu",
        "swedish":"sv",
        "norwegian":"nb",
        "danish":"da",
        "dutch":"nl",
        "russian":"ru",
        "turkish":"tr",
        "croatian":"hr",
        "japanese":"ja",
        "romanian":"ro",
        "ukrainian":"uk",
        "korean":"ko",
        "chinese":"zh-Hant",
        "greek":"el",
        "portuguese":"pt-pt"
    }
#Portal Translate Function
async def portalTranslate(text,lang,transType):
  portalTranslateUrlWithParams = portalTranslateUrl + "searchtext={}&language={}&transtype={}".format(text,lang,transType)
  async with ClientSession() as session:
      async with session.get(portalTranslateUrlWithParams,headers=headers,verify_ssl=None) as response:
          #print(str(response))
          if "414 Request-URI Too Large" in str(response):
            return "414"
          response = await response.read()
          #print(response)
          return response

#MTS translate Function         
async def mtsTranslate(lang,text):
  headers["Lang"] = lang
  async with ClientSession() as session:
      async with session.post(mtsUrl,headers=headers,json=[{"text" : text}],verify_ssl=None) as response:
          response = await response.read()
          return response

loop = asyncio.get_event_loop()


for f in files_xls:
  print("Translating " + f) 
# read from an excel file
  df = pd.read_excel('./' + f)
  df["Result Translation Type"] = ""
  i = 0

  for text in df["Key"]:

      try:  
            lang = langs.get((df["Language"][i]).lower())
            transType = df["Translation Type"][i]
            payloadText = urllib.parse.quote(text)
            portalResponse = loop.run_until_complete(portalTranslate(payloadText,lang,transType))
            if portalResponse == b'[]':
              response = loop.run_until_complete(mtsTranslate(lang,text))
              cell = json.loads(response)
              df["Translation"][i] = cell[0]["translations"][0]["text"]
              df["Result Translation Type"][i] = "Microsoft Translate Service"
            elif portalResponse == "414":
              print("=======================================")
              print("error on line: " + str(i + 2))
              print("The text to translate is too long and will have to be done manually.")
              print("=======================================\n")
            else:
              portalResponseJSON = json.loads(portalResponse)
              df["Translation"][i] = portalResponseJSON[0]["translation"]
              df["Result Translation Type"][i] = portalResponseJSON[0]["type"]
            i = i + 1
      except Exception as e:
            print("\n=============================================================")
            print("error on line: " + str(i + 2))
            print("\nresponse: " + str(portalResponse))
            print("\nerror: " + str(e))
            print("This may affect other lines so please fix the first error and run again")
            print("\n==============================================================")
            i = i + 1

  date = datetime.datetime.now()
  filename = str(date.year) + "_" + str(date.month) + "_" + str(date.day) + "_" + str(date.hour) + str(date.minute) + "_" + f

#./processed/{lang}yyymmddhhmm
  df.to_excel("./processed/" + filename,index=False) 
  print("Finished translating " + f ) 
  
print("Done!!")




