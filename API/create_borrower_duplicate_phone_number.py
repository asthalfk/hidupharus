#using 6285740001322 as phone number

import requests
from assertpy import assert_that
from pprint import pprint
from OBJECT import object_data
from API.generate_token import generate_token
from requests import RequestException as Exp
from OBJECT.pl_borrower_duplicate_phone_number import payload_duplicate_phone_number


def duplicate_phone_number():
    try :
        access_token = generate_token()
        response = requests.post(url=object_data.link+"/api/core/users", json=payload_duplicate_phone_number,
                                  headers={
                                      'Authorization': f'Bearer {access_token}'})

        assert_that(response.status_code).is_equal_to(409)
        print(response.status_code)
        pprint(response.json())
        jsonData = response.json()
        assert_that(jsonData['error_code']).is_equal_to('DUPLICATE_DATA')
        assert_that(jsonData['message']).is_equal_to(
            '{"authorisedSignatory.mobileNumber":"+6285740001322"}')


    except Exp:
        print(f"An error occurred: {Exp}")



if __name__ == '__main__':
    duplicate_phone_number()