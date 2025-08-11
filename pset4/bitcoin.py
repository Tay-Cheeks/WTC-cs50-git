#input from command line index 1
#input must be converted to float
#If no argument or invalid number → exit with an error message
#extract bitcoin current price with API JSON file
#JSON file has key of BTCUSD and get its value(float)
#Multiply the number of Bitcoins from the user by the API price.
#output: shows cost in USD
#4 decimal places
#using , as a thousands separator

import sys #read command-line arguments (argv) and to exit with sys.exit
import requests #to pull API data

#reusable function to get BTC price from CoinCap
def get_btc_price(api_key):
    """
    Fetches the current price of Bitcoin (USD) from the CoinCap API.
    Returns:
        float: Current price per Bitcoin in USD.
    Raises:
        SystemExit: If the API request fails or data parsing fails.
    """
    #fetch current btc price
    url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=8ea69efd6887851d02668ba4d52b99cd7abe57c451a97045e5d7be21f7e2f828"

    """
    {"data":{
    "id":"bitcoin",
    "rank":"1",
    "symbol":"BTC",
    "name":"Bitcoin",
    "supply":"19904934.0000000000000000",
    "maxSupply":"21000000.0000000000000000",
    "marketCapUsd":"2383681877354.6630183733449790",
    "volumeUsd24Hr":"26076222906.8617342709921743",
    "priceUsd":"119753.3173109070855685",
    "changePercent24Hr":"1.0278288570549161",
    "vwap24Hr":"120456.6432440796867520",
    "explorer":"https://blockchain.info/",
    "tokens":{}},"timestamp":1754937925536}
    """


    try:
        #send get request to API
        response = requests.get(url, timeout = 10) #timeout so it doesnt hang forever
        response.raise_for_status() #this will raise error if HTTP status is 4xx or 5xx(unsuccesful)

        #parse JSON data
        data = response.json() #converts response to a dictionary of data(key):priceUsd: xxx(value)

        #validate data nd priceUsd in API
        if "data" in data and "priceUsd" in data["data"]:
            #extract and return USD price as float
            price = float(data["data"]["priceUsd"]) #index into  the dict to get priceUsd value
            return price
        else:
            print("Unexpected data format from API")
            return None

    #catches all requests exceptions(incl Timeout)
    except requests.RequestException:
        return None
    except (KeyError, TypeError, ValueError):
        return None
    """
    If the function returns None,
    the main program can decide what to do next. for example,
    print an error message, try again, or safely exit.
    """

def main():

    #if length of sys args isnt 2(index0: script name and index2: no of btc)
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        #try convert argument[1] to float
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    #API key
    api_key = "8ea69efd6887851d02668ba4d52b99cd7abe57c451a97045e5d7be21f7e2f828"

    #get current btc price from API
    price_per_btc = get_btc_price(api_key)

    if price_per_btc is None:
        sys.exit("Failed to retrieve Bitcoin price.")

    total = bitcoins * price_per_btc

    #print output with comma per thou and 4 decimal places
    print(f"${total:,.4f}")


if __name__ == "__main__":
    main()



