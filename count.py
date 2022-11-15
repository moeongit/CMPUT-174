def count_occurunces(string: str) -> dict:
    count = {}
    list_of_words = string.split()
    for word in list_of_words:
        if word not in count:
            count[word] = 1
        else:
            pass


def main():
    string = input("Enter String: ")
    count_occurunces(string)

if __name__ == "__main__":
    main()