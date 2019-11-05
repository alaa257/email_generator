import json  # to read json files
import os  # to access operation for get and changing directory
import random
from tqdm import tqdm
import hashlib

def writeTextFile(text,index):
    f = open('email_%s.txt'%index,'w+')
    f.write(text)
    f.close()

def writeHashFile(text):
    f = open('00_Hash.json','w+')
    f.write(str(text))
    f.close()                

def readJsonCordinate(fileName):
    """Read the json data."""
    with open(fileName, 'r', encoding='utf-8') as f:     # Opening the file
        data = json.load(f)    # Read the json file
    return data


def convert(x):
    x = x.replace("\t", "\\t")
    x = x.replace("\v", "\\v")
    x = x.replace("\0", "\\0")
    x = x.replace("\b", "\\b")
    x = x.replace("\f", "\\f")
    return x


def toJson(body, titel, artikel, index):
    dict1 = {
        "data":
            {
                "Subject": ""
                ,
                "body": ""
            },
        "meta":
            {
                "article": []
            }
    }
    dict1['data']['Subject'] = convert(titel)
    dict1['data']['body'] = convert(body)
    dict1['meta']['article'] = [artikel]
    with open("email_%s.json" % index, 'w+', encoding='utf-8') as outfile:
        json.dump(dict1, outfile, ensure_ascii=False)


def TextToHash(text):
    x= hashlib.md5(text.encode())
    return x.hexdigest()

def search(hashed_new):
    h_exist = 0
    for i in range(len(hash_dict['data'])):
        if(hashed == hash_dict['data'][i]):
            h_exist += 1 # do nothing
    return (bool(h_exist))


def addToHashDict(hashed):
    JtoL = hash_dict['data']
    JtoL.append(hashed)
    hash_dict.update({'data':JtoL})

hash_dict = {'data':[]}

betreff = readJsonCordinate('Betreff.json')
anreden = readJsonCordinate('Anreden.json')
vornamen = readJsonCordinate('Vornamen.json')
nachnamen = readJsonCordinate('nachnamen.json')
vorhaben = readJsonCordinate('Vorhaben.json')
vorhabendetails = readJsonCordinate('vorhabendetails.json')
kennung = readJsonCordinate('kennung.json')
geburtsdatum = readJsonCordinate('geburtsdatum.json')
anspruch = readJsonCordinate('Rechtlicher_Anspruch.json')
bestaetigung = readJsonCordinate('Bestaetigung.json')
abschlussworte = readJsonCordinate('Abschlussworte.json')

# define the length of variables 
len_betreff = len(betreff['betreff'])
len_anreden = len(anreden['Anreden'])
len_vornamen = len(vornamen['vornamen'])
len_nachnamen = len(nachnamen['Nachname'])
len_vorhaben = len(vorhaben['Vorhaben'])
len_vorhabendetails = len(vorhabendetails['vorhabendetails'])
len_kennung = len(kennung['identifikation'])
len_geburtsdatum = len(geburtsdatum['geburtsdatum'])
len_anspruch = len(anspruch['Rechtlicher_Anspruch'])
len_bestaetigung = len(bestaetigung['bestaetigung'])
len_abschlussworte = len(abschlussworte['abschlussworte'])

# Geburtsdatum , Kennungsnr sind nicht gezählt
max_emails = len_betreff*len_anreden*len_vornamen*len_nachnamen*len_vorhaben*len_vorhabendetails*len_kennung*len_anspruch*len_bestaetigung*len_abschlussworte
#print(len_betreff)
#print(len_anreden)
#print(len_vornamen)
#print(len_nachnamen)
#print(len_vorhaben)
#print(len_vorhabendetails)
#print(len_kennung)
#print(len_anspruch)
#print(len_bestaetigung)
#print(len_abschlussworte)




Kennungsnr = [1458745,2547,985478,21569,87451,12547,87459,12698,1258478,85236,44745,1258,4555,2125,3225,1224,4578]
ignored= 0
anzahl_emails=int(input("Please enter the number of emails you want to create"))
index = 0
for a in tqdm(range(anzahl_emails), ncols=90):   
     #Betreff
    t1 = random.randrange(len_betreff)
    p1 = betreff['betreff'][t1]
    #Anrede
    t2 = random.randrange(len_anreden)
    p2 = anreden['Anreden'][t2]
     #Nachname
    t3 = random.randrange(len_nachnamen)
    if t2 in range(14, 26):
        p3=""
    else:
        p3 = nachnamen['Nachname'][t3]+',' 
    #vorhaben
    t4 = random.randrange(len_vorhaben)
    p4 = vorhaben['Vorhaben'][t4]
    #vorhabendetail
    t5 = random.randrange(len_vorhabendetails)
    p5 = vorhabendetails['vorhabendetails'][t5]
    #Kennung
    trigger1 = random.choice([True, False])
    if(trigger1):
        t6 = random.randrange(len_kennung)
        p6 = kennung['identifikation'][t6]+'\n'
         #geburtsdatum
        t7 = random.randrange(len_geburtsdatum)
        p7 = 'Geburtsdatum: '+ geburtsdatum['geburtsdatum'][t7]+'\n'+ 'Kennungsnummer: '+ str(Kennungsnr)+'\n'
    else:
        p6=""
        p7=""
    # Anspruch
    trigger2 = random.choice([True, False])
    if(trigger2):
        t8 = random.randrange(len_anspruch)
        p8 = anspruch['Rechtlicher_Anspruch'][t8] + "\n"
    else:
        p8 = ""
    #Bestätigung
    trigger3 = random.choice([True, False])
    if(trigger3):
        t9 = random.randrange(len_bestaetigung)
        p9 = bestaetigung['bestaetigung'][t9] + "\n"
    else:
        p9 = ""
    #Abschlussworte
    t10 = random.randrange(len_abschlussworte)
    p10= abschlussworte['abschlussworte'][t10] 
     #vorname
    t11 = random.randrange(len_vornamen)
    p11= vornamen['vornamen'][t11]
    #nachname
    t12 = random.randrange(len_nachnamen)
    p12= nachnamen['Nachname'][t12]
    email = p1 + '\n\n'+ p2 + ' ' + p3 + '\n\n' + p4 + '\n' + p5 + '\n' + p6+ p7 + p8 + p9 + '\n' + p10+'\n\n'+ p11+' '+p12
    hashed= TextToHash(email)
    if(len(hash_dict['data'])==0):
        addToHashDict(hashed)
        writeTextFile(email,index)
        toJson(email,p1,17,index)
        index+=1
    else:
        if(search(hashed)):
            ignored +=1
        else:
            addToHashDict(hashed)
            writeTextFile(email,index)
            toJson(email,p1,17,index)
            index+=1
    writeHashFile(hash_dict)
print(ignored,"duplicate emails have been ignored",sep=" ")
print(anzahl_emails,"emails of max",max_emails,"have been generated",sep=" ")




