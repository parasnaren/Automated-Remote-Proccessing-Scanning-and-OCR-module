import re
from PIL import Image
import pytesseract 
    
normal = pytesseract.image_to_string(Image.open('normal.png'), lang='eng').upper()
thresh = pytesseract.image_to_string(Image.open('thresh.png'), lang='eng').upper()



def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    kar = pytesseract.image_to_string(Image.open('rv.jpeg'), lang='eng').upper()
    
    # REGEX
    REGNO = re.compile(r'[A-Z]{2}([0-9]{1,2}|O[0-9]?)[A-Z]{1,2}[0-9]{3,4}')
    CHASSIS = re.compile(r'[0-9A-Z]{11}[0-9]{6}')
    ENGINE = re.compile(r'[0-9A-Z]{6}[0-9A-Z]{1,8}\s')
    FUEL = re.compile(r'PETR(O|0)L')
    MAKERS = ['MARUTHI','TOYOTA','HYUNDAI','CHEVORLET','TATA','SKODA','HONDA','MAHINDRA','NISSAN','RENAULT','MERCEDES','AUDI','BMW','VOLKSWAGEN','BAJAJ','TVS','SUZUKI','YAMAHA','KAWASAKI','HERO','ENFIELD','DAVIDSON']
    #NAME = re.compile(r'[A-Z]+[A-Z]*\s[A-Z]+[A-Z]*(\n|\s[A-Z]+[A-Z]*\n)')
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

    # preprocessing
    re.sub(r'-','/',kar)
    

    # regno
    regno = REGNO.search(kar)
    if regno == None:
        regno = 'null'
    else:
        regno = regno.group()
    
    
    # state
    state = 'null'
    if regno != 'null':
        state = regno[:2]
        state = STATES[state]
        
    
    # chassis and engine
    chassis = CHASSIS.search(kar)
    if chassis == None:
        chassis = 'null'
    else:
        chassis = chassis.group()
    
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
    manudate = MANUDATE.search(kar)
    if manudate == None:
        manudate = 'null'
    else:
        manudate = manudate.group()
    
    # maker
    maker = 'null'
    for m in re.findall(r'[A-Z][A-Z]+',kar):
        if m in MAKERS:
            maker = m
            break
        
        
    # owner
    junk = [':','Regn No','Regd Owner','ADDRESS','Maker’s Class','VEHICLE CLASS',
            'Mth. Yr.Of.Mfg','Fuel Used','Type Of Body','Reg No', 'DATE OF REG',
            'Reg Validity','Chassis No','Engine No','Son/Daughter/Wife Of',
            'REG.DATE','REG DATE','CHASSIS.NO','ENGINE.NO','OWNER NAME','S.W.D OF','MODEL',
            'BODY','NO OF CYCLE','WHEEL BASE','UNLADEN WT','MFG DATE','TAX UPTO',
            'ENG NO','NO OF CYCL','REG VALID UPTO','TAX VALID UPTO',
            'Dealers’s Name and Address','Date of Issue','Type Of Body','Mth. Yr. Of Mfg',
            'Signature of Issuing Authority']
    junk = [j.upper() for j in junk]
    for j in junk:
        kar = kar.replace(j, '')

    #OWNER = re.compile(r'[A-Z]+\s[A-Z]+\n|[A-Z]+\n|[A-Z]+\s[A-Z]\n')
    owners = kar.split('\n')
    owners = [k.replace(':','').strip() for k in owners]
    OWNER = re.compile(r'\w+\s\w+\s\w*\s?\w*\s?')
    #temp = 'PARAS NAREN\n'
    owner = 'null'
    for s in owners:
        owner = OWNER.search(s)
        if owner != None and owner not in junk:
            owner = owner.group()
            break
        
        
    # Model name
    
        
    
            
            



row_entry={'state': state,
           'registration_no': regno,
           'owner':'null',
           'model': 'null',
           'makers_name': maker,    
           'year_of_manufacture': manudate,
           'chassis_no': chassis,
           'engine_no':engine,
           'reg_date': start_date,
           'valid_date': expiry_date,
           'road_tax_upto': tax_date,
           'fuel_used': fuel,
           }

print(row_entry)