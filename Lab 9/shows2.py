import requests
# Uncomment two lines below if you get status code 429 (rate limit exceeded)
# import requests_cache
# requests_cache.install_cache('cmput174_cache')

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    new_url = "https://api.tvmaze.com/search/shows/"
    query = {"q":query}
    response = requests.get(new_url, query)
    results = response.json()
    if query not in results:
        return results
    return None

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    show_premiered = '?'
    if show['premiered'] is not None:
        show_premiered = show['premiered'][:4]
    show_ended = '?'
    if show['ended'] is not None:
        show_ended = show["ended"][:4]
    show_genres = '?'
    if show['genres'] != []:
        show_genres = ', '.join(show['genres'])
    for i in range(len(show_genres)):
        show_genres = show_genres.lower()
    return f"{show['name']} ({show_premiered} - {show_ended}, {show_genres})"

def main():
    """
    Main function 
    """
    query = input("Search for a show: ")
    results = get_shows(query)
    if not results:
        print("No results found")
    else:
        n = 1
        print("Here are the results:")
        for result in results:
            show = result["show"]
            print(f"{n}. {format_show_name(show)}")
            n += 1 

if __name__ == '__main__':
    main()