msg = "Hello World"
print(msg)

import requests

urlGetCodes = 'https://v6.exchangerate-api.com/v6/838018586de17f4f39b03c4f/codes'
response = requests.get(urlGetCodes)
codes = response.json()
currencies = codes["supported_codes"]
print(len(currencies))

def getExchangeRate(b, t):
    print("called")
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/838018586de17f4f39b03c4f/pair/'+b+"/"+t

    # Making our request
    response = requests.get(url)
    data = response.json()

    base_code = data["base_code"]
    target_code = data["target_code"]
    rate = data["conversion_rate"]

    # Your JSON object
    conversion = base_code + " to " + target_code + " is 1 to " + str(rate) + " ratio."
    return conversion


