chicken = 2.32 # 2.32 is our number in kg
consumed_chicken = chicken * (1/3) # She ate one third of the chicken
consumed_chicken_ounces = 2.20462 * 16 * consumed_chicken # We convert it to pounds first, 1 kg = 2.20462 lbs, and multiply it by 16 (ounces) and mulitply it by consumed chicken (kg) to cancel
consumed_chicken_ss = consumed_chicken_ounces / 6 # We take our consumed chicken in ounces and divide it by 6 ounces to get grams
grams_of_protein = int(consumed_chicken_ss * 23)  # We then take our number in grams and multiply it by 23, our number of grams of protein in 1/3 of the chicken.

print("You consumed " + str(grams_of_protein) + " grams of protein.")