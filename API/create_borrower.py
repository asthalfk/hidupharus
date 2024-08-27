#need change for email adn phone number field
import requests
from assertpy import assert_that
from pprint import pprint
from OBJECT import object_data
from API.generate_token import generate_token
from requests import RequestException as Exp
from OBJECT.pl_create_borrower import payload_create



def create_borrower():
    try :
        access_token = generate_token()
        response = requests.post(url=object_data.link+"/api/core/users", json=payload_create,
                                  headers={
                                      'Authorization': f'Bearer {access_token}'})

        assert_that(response.status_code).is_equal_to(200)
        print(response.status_code)
        pprint(response.json())

    except Exp:
        print(f"An error occurred: {Exp}")



if __name__ == '__main__':
    create_borrower()
