episode_name = input("Enter the Episode Name: ") # Takes the format of the episode name
underscore = episode_name.find("_") # Finds the index of the first underscore
episode_season = episode_name[1:underscore] # Takes the season number 
episode_name = episode_name[underscore+1:] # We update the string so that it removes the "SXY_" 
underscore = episode_name.find("_") # we find the second underscore 
episode_number = episode_name[1:underscore] # Takes the episode number
episode_title_name = episode_name[underscore+1:] # Takes the title 

print("Season " + str(episode_season) + ", Episode " + str(episode_number) + ": " + episode_title_name + " (The Simpsons)")