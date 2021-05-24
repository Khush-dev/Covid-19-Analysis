import requests
import json
import csv
url = 'https://api.covid19india.org/v4/min/data.min.json'
rq = requests.get(url)
data = rq.json()

#getting a list of states and codes
st_ut = ['andaman and nicobar islands',
 'andhra pradesh',
 'arunachal pradesh ',
 'assam',
 'bihar',
 'chhattisgarh',
 'chandigarh',
 'delhi',
 'daman and diu',
 'goa',
 'gujarat',
 'himachal pradesh',
 'haryana',
 'jharkhand',
 'jammu and kashmir',
 'karnataka',
 'kerala',
 'ladakh',
 'lakshadweep',
 'maharashtra',
 'meghalaya',
 'manipur',
 'madhya pradesh',
 'mizoram',
 'nagaland',
 'odisha',
 'punjab',
 'puducherry',
 'rajasthan',
 'sikkim',
 'telangana',
 'tamil nadu',
 'tripura',
 'india',
 'uttar pradesh',
 'uttarakhand',
 'west bengal']
codes = []
for i in data:
  codes.append(i)

my_code = -1
state = input().lower()             #case-insensitive
if state in st_ut:
  my_code = codes[st_ut.index(state)]
elif state.upper() in codes:
    my_code = state.upper()
elif state == '?':
    for i in range(len(codes)):
        print(codes[i],st_ut[i].capitalize())
else:
    print("Enter a valid State or Union territory(Eg. GJ or Gujarat or gujarat) Press '?' for list of valid inputs")
#now we have the user input state in the form of state code string

if my_code == 'TT':
    print("Enter a valid State or Union territory(Eg. GJ or Gujarat or gujarat)")
elif my_code != -1:
    mylist = [['District', 'Total cases']]
    for i in data[my_code]['districts']:
        mylist.append([i, data[my_code]['districts'][i]['total']['confirmed']])
    #creating the required csv file
    with open('total_' + my_code+ '_cases.csv', 'w', newline='') as my_file:
         writer = csv.writer(my_file)
         writer.writerows(mylist)
    print('total_' + my_code+ '_cases.csv created successfully!')
