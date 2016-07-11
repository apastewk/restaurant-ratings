# your code goes here

def restaurant_ratings(path):
    """Reads data file and displays scores.  

    Returns list of restaurants and ratings in albathetical order.
    """
    score_data = open(path)
    restaurant_ratings_dicts = {}

    for line in score_data:
        line = line.rstrip()
        restaurant_data = line.split(":")
        restaurant_name, rating = restaurant_data
        restaurant_ratings_dicts[restaurant_name] = rating

    sorted_restaurants = sorted(restaurant_ratings_dicts)

    for restaurants in sorted_restaurants:
        print "%s is rated at %s." % (restaurants, restaurant_ratings_dicts[restaurants])
  
    score_data.close()

    return None 

restaurant_ratings("scores.txt")

#unordered dictionary 
