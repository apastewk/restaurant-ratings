# your code goes here

def restaurant_ratings(path):
    """Reads data file and displays scores.  

    Prints list of restaurants and ratings in albathetical order.
    """
    score_data = open(path)
    restaurant_ratings_dicts = {}

    for line in score_data:
        line = line.rstrip()
        restaurant_data = line.split(":")
        restaurant_name, rating = restaurant_data
        restaurant_ratings_dicts[restaurant_name] = rating

    sorted_restaurants = sorted(restaurant_ratings_dicts.items())

    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s." % (restaurant, rating)
  
    score_data.close()

# restaurant_ratings("scores.txt")

def review_new_restaurant(path):
    """Adds restaurant to ratings list .  

    Prints list of restaurants and ratings in albathetical order.
    """

    score_data = open(path)
    restaurant_ratings_dicts = {}

    for line in score_data:
        line = line.rstrip()
        restaurant_data = line.split(":")
        restaurant_name, rating = restaurant_data
        restaurant_ratings_dicts[restaurant_name] = rating

    new_restaurant_name = raw_input("What is the restaurants name that you would like to add?: ")
    new_restaurant_rating = int(raw_input("What is the rating of the restaurant?: "))
    restaurant_ratings_dicts[new_restaurant_name] = new_restaurant_rating

    sorted_restaurants = sorted(restaurant_ratings_dicts.items())

    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s." % (restaurant, rating)
  
    score_data.close()

# review_new_restaurant("scores.txt")

import random 

def random_rating(path):

    score_data = open(path)
    restaurant_ratings_dicts = {}

    raw_input("Hello! What is your name?: ")

    for line in score_data:
        line = line.rstrip()
        restaurant_data = line.split(":")
        restaurant_name, rating = restaurant_data
        restaurant_ratings_dicts[restaurant_name] = rating

    i = 0
    restaurant_name_list = restaurant_ratings_dicts.keys()
    i = random.randint(0, len(restaurant_ratings_dicts) -1)
    random_restaurant_name = restaurant_name_list[i]
    random_restaurant_rating = restaurant_ratings_dicts[random_restaurant_name] 
    print "The restaurant is %s and the rating is %s" % (random_restaurant_name, random_restaurant_rating)
    user_rating = raw_input("Enter your rating: ")

    restaurant_ratings_dicts[random_restaurant_name] = user_rating

    sorted_restaurants = sorted(restaurant_ratings_dicts.items())

    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s." % (restaurant, rating)
  
    score_data.close()

random_rating("scores.txt")