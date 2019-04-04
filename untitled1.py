from PIL import Image
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
tela = pytesseract.image_to_string(Image.open('out11.jpg'), lang='eng')
maha = pytesseract.image_to_string(Image.open('out.jpg'), lang='eng')
anda = pytesseract.image_to_string(Image.open('out.jpg'), lang='eng')
bihar = pytesseract.image_to_string(Image.open('3.jpeg'), lang='eng')
andra = pytesseract.image_to_string(Image.open('out5.jpeg'), lang='eng')




"""# Registration number for vehicle
REGNO = re.compile(r'[A-Z]{2}([0-9]{2}|O[0-9])[A-Z]{2}[0-9]{4}')
temp = 'MHO2AB8561'
no = REGNO.search(temp)
no = REGNO.search(s)
regno = no.group()
if regno[2] == 'O':
    regno[2] = 0
if regno[:2] == 'KA':
    state = 'Karnataka'


# Chassis retrieval
CHASSIS = re.compile(r'[0-9A-Z]{17}')
temp = 'MELBBS1BR9O0M71WR43'
no = CHASSIS.search(temp)
no.group()

# Engine retrieval
ENGINE = re.compile(r'[0-9A-Z]{6}[0-9A-Z]{1,4}\n')
temp = 'ME2BBS1111\n'
no = ENGINE.search(temp)
no.group()



# Names of people
NAME = re.compile(r'[A-Z]+[A-Z]*\s[A-Z]+[A-Z]*(\n|\s[A-Z]+[A-Z]*\n)')
temp = 'Paras Naren VV\n'
no = NAME.search(temp)
no = NAME.search(s)
no.group()

# Address
ADDR = re.compile(r'.+,\s.+,\s.+,\s.+,')

# Date for person
import datetime
now = datetime.datetime.now()

DATE = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
temp = """22/03/2019
        21/03/2035
        15/03/2022"""
dates = DATE.findall(temp)
#DATE.search(temp).group()



# Manufacturer date(mmyyyy)
MANUDATE = re.compile(r'[0-9]{2}(/|-)[0-9]{4}')
no = MANUDATE.search(temp)
manudate = no.group()


# petrol/diesel
FUEL = re.compile(r'PETR(O|0)L')
temp = 'asdfasdf\nasd a\nPETROL\n345234 sdaf asd f\n'
if FUEL.search(temp) == None:
    fuel = 'DIESEL'
else:
    fuel = 'PETROL'


# State identification
STATES = {'TN':'Tamil Nadu',
          'AN':'Andaman and Nicobar',
          'AP':'ANDHRA PRADESH',
          'KA': 'Karnataka',
          'HR': 'Haryana',
          'TS': 'Telangana',
          'BR': 'Bihar',
          'MP': 'Madhya Pradesh',
          }


# Color of vehicle
COLOR = re.compile(r'[A-Z]+\n')
temp = 'Black\n RED\n White\n'
no = COLOR.findall(temp)
for c in no:
    c = c.strip()
    if c in ['RED','BLACK','WHITE','BLUE']:
        #color = c
        print(c)
        #break
        
# Serial number
SERIAL = re.compile(r'[0-9]{5}')
temp = '12431\nasjg asgapshg af\nsafdnahsdf afg asfg \n'
no = SERIAL.search(temp)
no.group()
serial = no.group()

# Body types
BODY = re.compile(r'[A-Z]([a-z]+|[A-Z]+)')
bodytypes = ['Saloon','Convertible','Coupe','Hatchback','SUV']
no = BODY.findall(temp)
for b in no:
    if b in bodytypes:
        body = b
        break

# Maker
MAKERS = ['MARUTHI','TOYOTA','HYUNDAI','CHEVORLET','TATA']
"""




