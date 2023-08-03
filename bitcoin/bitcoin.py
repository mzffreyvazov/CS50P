import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

try:
    value = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bitcoin_to_USD = float(response['bpi']['USD']['rate'].replace(",",""))
    amount = bitcoin_to_USD * value
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)


