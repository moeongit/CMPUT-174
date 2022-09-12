episode_name = input("Enter the Episode Name: ")
underscore = episode_name.find("_")
episode_season = episode_name[1:underscore]
episode_name = episode_name[underscore+1:]
underscore = episode_name.find("_")
episode_number = episode_name[1:underscore]
episode_name = episode_name[underscore+1:]

print("Season " + str(episode_season) + ", Episode " + str(episode_number) + ": " + episode_name + " (The Simpsons)")