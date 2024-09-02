from jsonschema import validate, ValidationError as e
from OBJECT import object_data
import requests
from requests import RequestException as Exp


schema = {
    "type" : "object",
    "properties": {
     "access_token" :{
         "type" : "string"
     }

    } }

def validate_tioken_schema():
    try :
        response = requests.post(url=object_data.link+"/api/auth/token", auth=(object_data.username, object_data.password))
        data = response.json()
        validate(instance=data, schema=schema)
        print("sasda")

    except Exp:
        print(f"An error occurred: {Exp}")
    except e:
        print(e)

if __name__ == '__main__':
    validate_tioken_schema()



