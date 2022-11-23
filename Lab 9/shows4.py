# This program takes a user input which is the name of a show and returns a maximum of 10 shows which contain the users input
# It then asks the user to select a show and then gives him the seasons of that show, as well as the premiere date and ending of each season with the number of episodes
# It then asks the user to input a season, and gives the user the episode name of of each episode, along with the rating

import requests

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    new_url = "https://api.tvmaze.com/search/shows/" # Function that just gets the shows from this api
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
    show_premiered = '?' # Using keys from the parameter and checks if theyre not None, if they arent it does whatever is under the if statement
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
    return f"{show['name']} ({show_premiered} - {show_ended}, {show_genres})" # Returns the show name, the date it premiered - the date it ended, and the genres

def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    new_url = f"https://api.tvmaze.com/shows/{show_id}/seasons" # Url that contains the show ID
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

def get_episodes_of_season(season_id: int) -> list[dict]:
    """
    Get the episodes of a given season of a show
    season_id is the id (not the number!) of the season
    """
    new_url = f"https://api.tvmaze.com/seasons/{season_id}/episodes"
    response = requests.get(new_url)
    if response.status_code == 200:
        return response.json()

def format_episode_name(episode: dict) -> str:
    """
    Format the episode name
    """
    if episode['name'] is not None:
        episode_name = episode['name']
    else:
        episode_name = '?'
    if episode['season'] is not None:
        episode_season_number = episode['season']
    else:
        episode_season_number = '?'
    if episode['number'] is not None:
        episode_number = episode['number']
    else:
        episode_number = '?'
    if episode['rating'] is not None:
        episode_rating = episode['rating'].get("average")
    else:
        episode_rating = '?'
    return f"S{episode_season_number}E{episode_number} {episode_name} (rating: {episode_rating})"

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
        print(f"Seasons of {results[select - 1]['show']['name']}:")
        selected_show = results[select - 1]["show"]
        show_id = selected_show["id"]
        seasons = get_seasons(show_id)
        season_id = selected_show["id"]
        episodes = get_episodes_of_season(season_id)
        counter = 1
        counter_episodes = 1
        
        if len(seasons) == 0:
            print("no seasons found")
        else:
            for season in seasons:
                results_season = format_season_name(season)
                print(f"{counter}. {results_season}")
                counter += 1
            select_episode = int(input("Select a season: "))
            print(f"Episodes of {results[select - 1]['show']['name']} S{select_episode}:")
            for episode in episodes:
                episode_results = format_episode_name(episode)
                print(f"{counter_episodes}. {episode_results}")
                counter_episodes += 1

if __name__ == '__main__':
    main()