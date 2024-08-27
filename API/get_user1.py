import requests
from assertpy import assert_that
from pprint import pprint
from OBJECT import object_data
from API.generate_token import generate_token
from requests import RequestException as Exp

def get_user_by_ID():
    try :
        access_token = generate_token()
        response = requests.get(url=object_data.link+"/api/core/users/66bba58f22156aa407fa557a",
                                  headers={
                                      'Authorization' : f'Bearer {access_token}'} )

        assert_that(response.status_code).is_equal_to(200)
        pprint(response.json())
        data_id = response.json().get('id')
        assert_that(data_id).is_equal_to('66bba58f22156aa407fa557a')

        authorised_data = response.json().get('authorised_signatory')
        # pprint(authorised_data)
        assert_that(authorised_data['address']['city']).is_equal_to('JAKARTA PUSAT')
        assert_that(authorised_data['documents']['ktp']['number']).is_equal_to('3372052106610006')
        assert_that(authorised_data['first_name']).is_equal_to('IR JOKO WIDODO')

    except Exp:
        print(f"An error occurred: {Exp}")



if __name__ == '__main__':
    get_user_by_ID()
