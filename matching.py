import re
from PIL import Image
import pytesseract 


row_entry={'state': 'Karnataka',
           'registration_no':'RC10012',
           'serialno': '13456',
           'swd_of':'Father ffh',
           'address': 'Flat 300 Jayanagar, Bsk, asdfasdf, asfdasdf,',
           'vehicle_class' : 'LMVCAR',
           'model': 'car name',
           'makers_name':'Maruthi',    
           'year_of_manufacture':'2010',
           'chassis_no':'ASDF1291301',
           'engine_no':'ASDF129',
           'reg_date': '12/2/2000',
           'valid_date':'11/2/2020',
           'road_tax_upto':'2019',
           'seating_capacity':'5',
           'no_of_cylinders':'5',
           'horse_power':'756',
           'fuel_used':'Petrol',
           'color':'White',
           'purpose-code':'NEW'
           'wheel_base': '1234',
           'cc': '1598',
           'weight': 'null',
           'body_type': 'Saloon',
           'standing_capacity': 'null',
           }



# Registration number for vehicle
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

    
    
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    kar = pytesseract.image_to_string(Image.open('rv.jpeg'), lang='eng').upper()
    
    # REGEX
    REGNO = re.compile(r'[A-Z]{2}([0-9]{2}|O[0-9])[A-Z]{2}[0-9]{4}')
    CHASSIS = re.compile(r'[0-9A-Z]{17}')
    ENGINE = re.compile(r'[0-9A-Z]{8}[0-9A-Z]{1,10}')
    FUEL = re.compile(r'PETR(O|0)L')
    MAKERS = ['MARUTHI','TOYOTA','HYUNDAI','CHEVORLET','TATA','SKODA']
    NAME = re.compile(r'[A-Z]+[A-Z]*\s[A-Z]+[A-Z]*(\n|\s[A-Z]+[A-Z]*\n)')
    DATE = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
    MANUDATE = re.compile(r'[0-9]{2}(/|-)[0-9]{4}')
    
    STATES = {'TN':'Tamil Nadu',
          'AN':'Andaman and Nicobar',
          'AP':'ANDHRA PRADESH',
          'KA': 'Karnataka',
          'HR': 'Haryana',
          'TS': 'Telangana',
          'BR': 'Bihar',
          'MP': 'Madhya Pradesh',
          }

    # regno
    regno = REGNO.search(kar).group()
    
    # state
    state = regno.group()[:2]
    state = STATES[state]
    
    # owner
    name = NAME.search(kar).group()
    
    # chassis and engine
    chassis = CHASSIS.search(kar).group()
    
    def hasDigit(s):
        return any(char.isdigit() for char in s)
    
    engines = ENGINE.findall(kar)
    for engine in engines:
        if hasDigit(engine) and engine != regno and engine != chassis:
            break
    
    # dates (reg and valid)
    dates = DATE.findall(kar)
    import datetime
    now = datetime.datetime.now()
    for date in dates:
        year = int(date[6:])
        if year > now.year:
            expiry_date = year
        else:
            start_date = year
            
    #fuel type
    if FUEL.search(kar) == None:
        fuel = 'DIESEL'
    else:
        fuel = 'PETROL'
    
    # manufacture date
    manudate = MANUDATE.search(kar).group()
    
    # maker
    for m in re.findall(r'[A-Z][A-Z]+',kar):
        if m in MAKERS:
            maker = m
            break


    