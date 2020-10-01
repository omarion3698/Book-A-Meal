import urllib.request,json
from .models import meal

# Getting api key
api_key = None

# Getting the meal base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MEAL_API_KEY']
    base_url = app.config['MEAL_API_BASE_URL']


def get_meals(category):
    '''
    Function that gets the json responce to our url request
    '''
    get_meals_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_meals_url) as url:
        get_meals_data = url.read()
        get_meals_response = json.loads(get_meals_data)

        meal_results = None

        if get_meals_response['results']:
            meal_results_list = get_meals_response['results']
            meal_results = process_results(meal_results_list)


    return meal_results


def get_meal(id):
    get_meal_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_meal_details_url) as url:
        meal_details_data = url.read()
        meal_details_response = json.loads(meal_details_data)

        meal_object = None
        if meal_details_response:
            id = meal_details_response.get('id')
            title = meal_details_response.get('original_title')
            overview = meal_details_response.get('overview')
            poster = meal_details_response.get('poster_path')
            vote_average = meal_details_response.get('vote_average')
            vote_count = meal_details_response.get('vote_count')

            meal_object = meal(id,title,overview,poster,vote_average,vote_count)

    return meal_object

def search_meal(meal_name):
    search_meal_url = 'https://api.themealdb.org/3/search/meal?api_key={}&query={}'.format(api_key,meal_name)
    with urllib.request.urlopen(search_meal_url) as url:
        search_meal_data = url.read()
        search_meal_response = json.loads(search_meal_data)

        search_meal_results = None

        if search_meal_response['results']:
            search_meal_list = search_meal_response['results']
            search_meal_results = process_results(search_meal_list)


    return search_meal_results




def process_results(meal_list):
    '''
    Function  that processes the meal result and transform them to a list of Objects

    Args:
        meal_list: A list of dictionaries that contain meal details

    Returns :
        meal_results: A list of meal objects
    '''
    meal_results = []
    for meal_item in meal_list:
        id = meal_item.get('id')
        title = meal_item.get('original_title')
        overview = meal_item.get('overview')
        poster = meal_item.get('poster_path')
        vote_average = meal_item.get('vote_average')
        vote_count = meal_item.get('vote_count')

        if poster:

            meal_object = meal(id,title,overview,poster,vote_average,vote_count)
            meal_results.append(meal_object)

    return meal_results
