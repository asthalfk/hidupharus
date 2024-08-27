import requests
from assertpy import assert_that
from pprint import pprint
from OBJECT import object_data
from API.generate_token import generate_token
from requests import RequestException as Exp

def get_all_user():
    try:
        access_token = generate_token()
        response = requests.get(url=object_data.link+"/api/core/users",
                                  headers={
                                      'Authorization' : f'Bearer {access_token}'} )

        print(response.status_code)
        assert_that(response.status_code).is_equal_to(200)
        pprint(response.json())
        data = response.json().get('users')
        pprint(data)

    except Exp:
        print(f"An error occurred: {Exp}")

if __name__ == '__main__':
    get_all_user()
