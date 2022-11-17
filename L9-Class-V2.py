import requests, pprint


def main():
    url = 'https://api.exchangerate.host/latest'

    cur_from = "CAD"
    cur_to = []
    amount = float(input("Enter amount in Canadian Dollars: "))
    while True:
        currency_code = input("Enter currency code or just press Enter to stop: ")
        if currency_code == "":
            break
        cur_to.append(currency_code)
    payload = {'base': cur_from, 'symbols': ','.join(cur_to), 'amount': amount}
    response = requests.get(url, payload)
    data = response.json()
    rates = data["rates"]
    # pprint.pprint(rates)
    print(f"{amount} CAD is equal to: ")
    for code, amount in rates.items(): # Important - do .items() 
        print(f"{amount} {code}")



if __name__ == '__main__':
    main()