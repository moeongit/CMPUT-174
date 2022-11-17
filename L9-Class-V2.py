import requests, pprint


def main():
    url = 'https://api.exchangerate.host/latest'

    cur_from = "CAD"
    cur_to = ["INR", "EUR", "UZS", "PKR"]
    amount = 1000
    payload = {'base': cur_from, 'symbols': ','.join(cur_to), 'amount': amount}
    response = requests.get(url, payload)
    data = response.json()
    rates = data["rates"]
    pprint.pprint(rates)


if __name__ == '__main__':
    main()