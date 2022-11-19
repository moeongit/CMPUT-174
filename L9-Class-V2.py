import requests, pprint


def get_currency_name(code):
    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    return data["symbols"][code]["description"]


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
        name = get_currency_name(code)
        print(f"{round(amount, 2)} {name}")



if __name__ == '__main__':
    main()