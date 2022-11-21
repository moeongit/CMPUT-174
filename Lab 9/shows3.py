import requests

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

def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    new_url = f"https://api.tvmaze.com/shows/{show_id}/seasons"
    response = requests.get(new_url)
    if response.status_code == 200:
        return response.json()

def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    if season['number'] is not None:
        season_number = season['number']
    else:
        season_number = "?"
    if season['premiereDate'] is not None:
        season_premiere_year = season['premiereDate'].split("-")[0]
    else:
        season_premiere_year = "?"
    if season['endDate'] is not None:
        end_year = season['endDate'].split("-")[0]
    else:
        end_year = "?"
    if season['episodeOrder'] is not None:
        episodes_number = season['episodeOrder']
    else:
        episodes_number = "?"

    return f"Season {season_number} ({season_premiere_year} - {end_year}), {episodes_number} episodes"
    

def main():
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
        select = int(input("Select a show: "))
        print(f"Seasons of {query}:")
        selected_show = results[select - 1]["show"]
        show_id = selected_show["id"]
        seasons = get_seasons(show_id)
        counter = 1
        if len(seasons) == 0:
            print("no seasons found")
        else:
            for season in seasons:
                results = format_season_name(season)
                print(f"{counter}. {results}")
                counter += 1                
        
if __name__ == '__main__':
    main()