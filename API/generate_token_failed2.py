# generate token using invalid credential username and valid password

from OBJECT import object_data
import requests
from requests import RequestException as Exp
from assertpy import assert_that
from pprint import pprint

def generate_token_failed2():
    try :
        response = requests.post(url=object_data.link+"/api/auth/token", auth=(object_data.invalid_username, object_data.password))
        assert_that(response.status_code).is_equal_to(500)
        print(response.status_code)
        jsonData = response.json()
        pprint(response.json())
        assert_that(jsonData['error_code']).is_equal_to("SERVER_ERROR")
        assert_that(jsonData['message']).is_equal_to("Something unexpected happened, we are investigating this issue right now")
        print("assert berhasil")

    except Exp:
        print(f"An error occurred: {Exp}")

if __name__ == '__main__':
    generate_token_failed2()



