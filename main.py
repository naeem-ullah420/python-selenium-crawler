from driver import selenium_driver
from selenium.webdriver.common.by import By
from pprint import pprint
import miscelleneous_helpers, pandas as pd

driver = selenium_driver.get_instance()

driver.get("https://www.imdb.com/search/title/?title_type=feature&genres=action&explore=genres")

all_movies = driver.find_elements(By.CSS_SELECTOR, '.lister-list > div')

print(f"No of movies: {len(all_movies)}")

scrapped_movies_data = []

for index, movie in enumerate(all_movies):
    try:

        movie_detail = {
            'movie_image'        : miscelleneous_helpers.find_text(movie, By.CLASS_NAME, 'lister-item-image img', 'src'),
            'movie_name'         : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.lister-item-header a'),
            'movie_year'         : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.lister-item-header .lister-item-year'),
            'certificate'        : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.certificate'),
            'movie_duration'     : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.runtime'),
            'genre'              : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.genre'),
            'movie_status'       : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.genre ~ b'),
            'rating'             : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.ratings-imdb-rating strong'),
            'rating_metascore'   : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.ratings-metascore'),
            'movie_description'  : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, 'p:not(:has(span))'),
            'cast_detail'        : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, 'p:has(a)'),
            'movie_votes_detail' : miscelleneous_helpers.find_text(movie, By.CSS_SELECTOR, '.sort-num_votes-visible')
        }

        pprint(movie_detail)
        scrapped_movies_data.append(movie_detail)
        driver.execute_script("arguments[0].scrollIntoView();", all_movies[index + 1])
    except Exception as e:
        pass

print(f"scrapped_movies_data = {len(scrapped_movies_data)}")
df = pd.DataFrame.from_dict(scrapped_movies_data)

print (df)
df.to_excel('movies.xlsx')
df.to_csv('movies.csv')