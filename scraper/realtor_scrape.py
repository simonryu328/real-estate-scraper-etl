import boto3
import csv
from datetime import datetime
from re import sub
import realtor_requests
import requests

BUCKET = 'realtor-data'

def get_id(result):
    return result['Id']

def get_address(result):
    return result['Property']['Address']['AddressText']

def get_longitude(result):
    return float(result['Property']['Address']['Longitude'])

def get_latitude(result):
    return float(result['Property']['Address']['Latitude'])

def get_interior_size(result):
    size_string = result['Building']['SizeInterior']
    return int(size_string.split()[0])
    
def get_building_type(result):
    return result['Building']['Type']
    
def get_bedrooms(result):
    return int(result['Building']['Bedrooms'])

def get_bathrooms(result):
    return int(result['Building']['BathroomTotal'])

def get_agent_name(result):
    return result['Individual'][0]['Name']

def get_area_code(result):
    return result['Individual'][0]['Phones'][0]['AreaCode']

def get_phone_number(result):
    return result['Individual'][0]['Phones'][0]['PhoneNumber']

def get_price(result):
    price_string = result['Property']['Price']
    return int(sub(r'[^\d.]', '', price_string))

values = ['id','address', 'longitude', 'latitude', 'interior_size', 'building_type', 'bedrooms', 
          'bathrooms', 'agent_name', 'area_code', 'phone_number', 'price']
functions = [get_id, get_address, get_longitude, get_latitude, get_interior_size, get_building_type, get_bedrooms, 
             get_bathrooms, get_agent_name, get_area_code, get_phone_number, get_price]
             
def get_property_info(result):
    property_info = {}
    for val, func in zip(values, functions):
        try:
            property_info[val] = func(result)
        except:
            property_info[val] = None
    
    return property_info
    
def get_page(index):

    headers = realtor_requests.get_headers()
    data = realtor_requests.get_data()
    data['CurrentPage'] = index
    
    response = requests.post('https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)
    try:
        response.raise_for_status()
    except:
        return None
        
    result_json = response.json()
    result_items = result_json['Results']
    
    property_info_list = []
    for result in result_items:
        property_info_list.append(get_property_info(result))
        
    return property_info_list

def lambda_handler(event, context):
    property_info_list = []
    # there are 50 pages
    for i in range(1,3):
        property_info_list.extend(get_page(i))

    with open('/tmp/real_estate.csv', 'w', newline='') as f:
        keys = property_info_list[0].keys()
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(property_info_list)

    date = datetime.now()
    file_name = f"{date.year}/{date.month}/{date.day}/real_estate.csv"

    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(Filename='/tmp/real_estate.csv', Bucket=BUCKET, Key=file_name)


