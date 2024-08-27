from OBJECT import object_data
import requests
from assertpy import assert_that
from requests import RequestException as Exp


def generate_token():
    try :
        response = requests.post(url=object_data.link+"/api/auth/token", auth=(object_data.username, object_data.password))
        assert_that(response.status_code).is_equal_to(200)
        print(response.status_code)
        token_value = response.json().get('access_token')
        print(token_value)
        return token_value

    except Exp:
        print(f"An error occurred: {Exp}")

if __name__ == '__main__':
    generate_token()



