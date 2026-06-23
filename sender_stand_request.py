import requests
import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_create_kit(body, token):
    h = data.headers.copy()
    h['Authorization'] = "Bearer " + token
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=body,
                         headers=h)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
token = response.json()['authToken']

resp_kit = post_create_kit(data.kit_body, token)
print(resp_kit.status_code)
print(resp_kit.json())

