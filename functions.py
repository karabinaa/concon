from os import listdir, system
from os.path import dirname, abspath
import xml.etree.ElementTree as ET
import shlex, re

def findXmls(directoryName):
    """
    Bulunulan dizin içerisindeki directoryName isimli klasörün Alt dizinlerdeki xml dosyalarının yollarını döndürür

    :param directoryName: alt dizinlerindeki xml dosyaları bulunacak dizinin adı

    """
    pass

    relPath = (dirname(dirname(dirname(abspath(__file__)))))

    dirPath = relPath+"/"+ directoryName

    idList = listdir(dirPath)

    pathList = []

    for id in idList:
        pathList.append(dirPath + "/" + id + "/" + 'metadata.xml' )

    return pathList

#
def trimmer(rawText):
    """
    Bazı kayıtların başında ve sonundaki whitespace ve \n karakterlerini giderir

    :param rawText: xml dosyasından okunan ham metin
    """
    pass

    return "-".join(rawText.split())


def getMeetingInfosFromXml(xml_file_path):
    """
    Verilen xml dosyasındaki toplantı adı ve toplantı linkini döndürür

    :param xml_file_path: okunacak xml dosyasının yolu

    """
    pass

    try:
        tree = ET.parse(xml_file_path)
        
        root = tree.getroot()

        for meetingName in root.iter("meetingName"):
            mName = trimmer(meetingName.text)
        for link in root.iter('link'):
            pbLink = trimmer(link.text)

        return [mName, pbLink]
    except:
        return ["", ""]


def search(query):
    pieces = shlex.split(query)
    include, exclude = [], []
    for piece in pieces:
        if piece.startswith('-'):
            exclude.append(re.compile(piece[1:]))
        else:
            include.append(re.compile(piece))
    def validator(s):
        return (all(r.search(s) for r in include) and
                not any(r.search(s) for r in exclude))
    return validator





def convertBBBMeeting2mp4(meetingLink, outputFileName):
    """
    Verilen Linkteki BBB toplantısını outputFileName.mp4 dosyası olarak kaydeder

    :param meetingLink: BBB toplantı linki
    :param outputFileName: çıktı dosyasına verilecek isim

    """
    pass

    system('node export.js "' + meetingLink + '" ' + outputFileName + ' 10 true')


def addLogos(filePath):
    print("to be implemented")
