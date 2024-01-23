import json
import requests
import sys

if len(sys.argv) == 2:
    try:
        number_as_float = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    price = response.json()
    btc_price = price.get('bpi', {}).get('USD', {}).get('rate_float')
    total_amount = btc_price * number_as_float
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("RequestException")
    sys.exit(1)
    
