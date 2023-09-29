import random
import sys
from xml.dom import minidom

try:
    joiDoc = minidom.parse('joi.xml')
except:
    print ("Przepraszam, nie wiem co powiedzieć. Oddaj mi joi.xml, proszę!")
    sys.exit()
joiCount = joiDoc.getElementsByTagName('sentence').length

joiChoice = random.randrange(0,joiCount,1)

joiTalk = joiDoc.getElementsByTagName('sentence')[joiChoice]
print (joiTalk.firstChild.data)