import re
from PIL import Image
import pytesseract 
    
temp1 = pytesseract.image_to_string(Image.open('scanned.png'), lang='eng').upper()
temp2 = pytesseract.image_to_string(Image.open('out90.jpg'), lang='eng').upper()
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
            expiry_date = date
        else:
            start_date = date
            tax_date = date[:6] + str(int(date[6:])+15)
    
            
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


row_entry={'state': state,
           'registration_no': regno,
           'serialno': 'null',
           'swd_of':'null',
           'address': 'null',
           'vehicle_class' : 'null',
           'model': 'null',
           'makers_name': maker,    
           'year_of_manufacture': manudate,
           'chassis_no': chassis,
           'engine_no':engine,
           'reg_date': start_date,
           'valid_date': expiry_date,
           'road_tax_upto': tax_date,
           'seating_capacity':'null',
           'no_of_cylinders':'null',
           'horse_power':'null',
           'fuel_used': fuel,
           'color':'null',
           'purpose-code':'null',
           'wheel_base': 'null',
           'cc': 'null',
           'weight': 'null',
           'body_type': 'null',
           'standing_capacity': 'null',
           }

print(row_entry)