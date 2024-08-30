import requests
from assertpy import assert_that
from pprint import pprint
from OBJECT import object_data
from generate_token import generate_token
from requests import RequestException as Exp
from OBJECT.pl_patch import payload_patch, payload_repatch

user_id = '66cdc3a6e6fd8ede0810afec'

def patch_user():
    try :
        access_token = generate_token()
        response = requests.patch(url=object_data.link+f"/api/core/users/66cdc3a6e6fd8ede0810afec", json=payload_patch,
                                  headers={
                                      'Authorization' : f'Bearer {access_token}'} )

        assert_that(response.status_code).is_equal_to(200)
        # pprint(response.status_code)
        # pprint(response.json())


        data_patch = requests.get(url=object_data.link+f"/api/core/users/66cdc3a6e6fd8ede0810afec",
                            headers={
                                       'Authorization' : f'Bearer {access_token}'} )
        pprint(data_patch.json())
        patch = data_patch.json().get('authorised_signatory')
        assert_that(patch['address']['district']).is_equal_to("pondok gede bage haduha")
        # pprint("assert berhasil")


    except Exp:
        print(f"An error occurred: {Exp}")


def repatch_user():
    try:
        access_token = generate_token()
        response = requests.patch(url=object_data.link + f"/api/core/users/66cdc3a6e6fd8ede0810afec",
                                  json=payload_repatch,
                                  headers={
                                      'Authorization': f'Bearer {access_token}'})

        assert_that(response.status_code).is_equal_to(200)


    except Exp:
        print(f"An error occurred: {Exp}")

if __name__ == '__main__':
    patch_user()
    # repatch_user()