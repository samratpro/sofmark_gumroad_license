import requests

GUMROAD_PRODUCT_ID = "m8P4pqFnq91JmZy0MkE18g=="
LICENSE_KEY = "DFBBE463-00F241B7-B7E08C8B-DA143698"
access_token = "9BxeJ6xlF-AXcQi0NlC2oZ02ILcz9Z9UfVpZPIrA9BM"



def verify_license(LICENSE_KEY):
    url = "https://api.gumroad.com/v2/licenses/verify"
    payload = {
        "product_id": GUMROAD_PRODUCT_ID,
        "license_key": LICENSE_KEY
    }
    response = requests.post(url, data=payload)
    gumroad_response = response.json()
    user = gumroad_response.get('uses',0)
    price = gumroad_response.get('purchase').get('price', 0)

    print(user)
    print(price)

def license_enable(LICENSE_KEY):
    url = "https://api.gumroad.com/v2/licenses/enable"
    payload = {
        "access_token": access_token,
        "product_id": GUMROAD_PRODUCT_ID,
        "license_key": LICENSE_KEY
    }
    response = requests.put(url, data=payload)
    gumroad_response = response.json()
    user = gumroad_response.get('uses',0)
    price = gumroad_response.get('purchase').get('price', 0)

    print(user)
    print(price)

def decrement_user(LICENSE_KEY):
    url = "https://api.gumroad.com/v2/licenses/decrement_uses_count"
    payload = {
        "access_token": access_token,
        "product_id": GUMROAD_PRODUCT_ID,
        "license_key": LICENSE_KEY
    }
    response = requests.put(url, data=payload)
    gumroad_response = response.json()
    print(gumroad_response)



# decrement_user()
# verify_license()
license_enable()
