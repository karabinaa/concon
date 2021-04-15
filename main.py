from functions import findXmls, getMeetingInfosFromXml, convertBBBMeeting2mp4, addLogos, search
from os.path import dirname, abspath, join
import os
import sys



os.chdir("/home/karabinaa/Desktop/pythondenemeleri/bbbrecorder/bbb-recorder")

pathList = findXmls("bbb18")

query = input("Sorguyu Giriniz : ")

searcher = search(query.replace("I","ı").replace("İ","i").lower())

matchDict = { }

key = 1
for path in pathList:
    try:
        ilist = getMeetingInfosFromXml(path)
    except:
        ilist = [""]

    if searcher(ilist[0].replace("I","ı").replace("İ","i").lower()) == True :
        matchDict.update( {key : ilist} )
        key += 1 

if len(query) > 0:
    for key,value in matchDict.items():
        print(str(key) + " : " + value[0])
 
    selection = input("Seçtiğiniz toplantıların numaralarını aralarına virgül koyarak yazıp enter'a basınız.Listelenen toplantıların tümünü seçmek için 0 yazıp entera basınız)  :  ")

else:
    selection = '0'

if selection == '0':
    selectedsList = range(1,len(matchDict)+1)
else:
    selectedsList = selection.split(",")

for key in selectedsList:

    key = int(key)    
    print("\n"+matchDict.get(key)[0] + ".mp4 oluşturuluyor")
    convertBBBMeeting2mp4(matchDict.get(key)[1],matchDict.get(key)[0])
    addLogos("mp4 file path")
    print("")
