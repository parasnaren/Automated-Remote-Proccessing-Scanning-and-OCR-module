
row_entry={'state': 'Karnataka',
               'registration_no':'RC10012',
               'serialno': '13456',
               'name':'XXX',
               'swd_of':'XXX',
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
               'purpose-code':'NEW',
               'wheel_base': '1234',
               'cc': '1598',
               'weight': 'null',
               'body_type': 'Saloon',
               'standing_capacity': 'null',
               }
temp = "["

j = 1
k = 0
print(type(row_entry))
for i,dont in row_entry.items():
    temp = temp+"\""+i+"\""+",\n"



for i,dont in row_entry.items():
    temp = temp+"\""+dont+"\""+",\n"
    j = j +1
    k = k +1

output = open("tablerows.txt","w")

output.write(temp)
print(temp)
