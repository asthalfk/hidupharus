# generate token using null value credential  for password and username

from OBJECT import object_data
import requests
from requests import RequestException as Exp
from assertpy import assert_that
from pprint import pprint

def generate_token_failed3():
    try :
        response = requests.post(url=object_data.link+"/api/auth/token", auth=(object_data.null_username, object_data.null_pass))
        assert_that(response.status_code).is_equal_to(401)
        print(response.status_code)
        jsonData = response.json()
        pprint(response.json())
        assert_that(jsonData['error_code']).is_equal_to("KEY_NOT_VALID")
        assert_that(jsonData['message']).is_equal_to("Your key is not valid")
        print("assert berhasil")

    except Exp:
        print(f"An error occurred: {Exp}")

if __name__ == '__main__':
   generate_token_failed3()



