from jsonschema import validate, ValidationError
import requests
from API.generate_token import generate_token
from OBJECT.object_data import link, user_id


schenam ={
    "type" : "object",
    "properties" :{
         "authorised_signatory": {
            "type" : "object",
            "properties" : {
                    "address" : {
                    "type" : "object",
                        "properties" : {
                            "city" :{"type" : "string"},
                            "district" : {"type" : "string"},
                            "postal_code": {"type" : "string"},
                            "province": {"type" : "string"},
                            "rt": {"type" : "string"},
                            "rw": {"type" : "string"},
                            "street_address": {"type" : "string"},
                            "village": {"type" : "string"}
                        }
                        },
                    "bank_account": {
                    "type": "object",
                        "properties" : {
                            "holder_name":{"type" : "string"},
                            "number": {"type" : "string"},
                            "swift_code": {"type" : "string"}
                        }
                    },
                    "birth_date": {"type" : "string", "format" : "date"},
                    "birth_place": {"type" : "string"},
                    "business_type": {"type" : "string"},

                    "documents" : {
                        "type" : "object",
                        "properties" : {
                                "ktp" :{
                                    "type" : "object",
                                    "properties" : {
                                            "expiry_date" : {
                                                "type" : "string",
                                                "format" : "date"
                                            },
                                            "file" : {
                                                "type" : "string"
                                            },
                                            "issuing_city" : {
                                                "type" : "string"
                                            },
                                            "number":{
                                                "type" : "string"
                                            }

                                        }, "required" :["expiry_date","issuing_city", "file", "number"]
                                    },
                                "npwp" : {
                                    "type" : "object",
                                    "properties" : {
                                        "number":{
                                            "type":"string"}
                                        }, "required" :["number"]
                                    },
                                "selfie": {
                                    "type" : "object",
                                    "properties" : {
                                        "file":{"type":"string"}
                                        }, "required" :["file"]
                                    }

                        } ,"required" :["ktp", "npwp", "selfie"]
                    },
                    "domicile": {"type":"string"},
                    "education": {"type":"string"},
                    "email": {"type":"string", "format": "email"},
                    "emergency_contact_name": {"type":"string"},
                    "emergency_contact_number": {"type":"string"},
                    "first_name": {"type":"string"},
                    "gender": {"type":"string"},
                    "housing_status": {"type":"string"},
                    "job": {"type":"string"},
                    "marital_status": {"type":"string"},
                    "mobile_number": {"type":"string"},
                    "monthly_income_range": {"type":"string"},
                    "mother_maiden_name": {"type":"string"},
                    "religion": {"type":"string"},
                    "source_of_fund": {"type":"string"},
                    "title": {"type":"string"}



            },"required" :["email", "first_name", "mobile_number"]


        },
        "id": {"type" : "string"},
        "type": {"type" : "string"},
        "partner_id": {"type" : "string"},
        "status": {"type" : "string"}

    },"required" :["id", "type", "authorised_signatory"]
}

try:
    access_token = generate_token()
    response1 = requests.get(url=link + f"/api/core/users/{user_id}",
                            headers={
                                'Authorization': f'Bearer {access_token}'})
    resp1 = response1.json()
    validate(instance=resp1, schema=schenam)
    print("JSON data is valid.")
except ValidationError as e:
    print("JSON data is invalid:", e.message)
