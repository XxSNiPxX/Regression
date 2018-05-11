import requests
from bs4 import BeautifulSoup as BS
import time
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import random
import matplotlib.pyplot as plt
for i<30:
    url='https://www.imdb.com/search/title?year=2017&title_type=feature&page={}&ref_=adv_nxt'.format(i)
    page = ''
    while page == '':
        try:
            page = requests.get(url)
            #print(page.status_code)
            break
        except:
            time.sleep(5) 
            continue
    soup=BS(page.text,'lxml')

    movie_ratings=[]   
    for z in soup.select('div.inline-block.ratings-imdb-rating'):
        a=z.text
        movie_ratings.append(a.strip())
    movie_genres=[]
    for b in soup.select('span.genre'):
        length=len(b.text.split())
        movie_genres.append(length)
def LR:
    movie_genre_X_train=movie_genres[:50]
    movie_genre_X_test=movie_genres[-20:]
    movie_ratings_Y_train=movie_ratings[:50]
    movie_ratings_Y_test=movie_ratings[-20:]
    regr=linear_model.LinearRegression()
    regr.fit(movie_genre_X_train,movie_ratings_Y_train)
    movie_rating_pred=regr.predict(movie_genre_X_test)
    print("Coefficients={}").format(regr.coef_)
    plt.scatter(movie_genre_X_test, movie_ratings_Y_test,color='black)
    plt.plot(movie_genre_X_test,movie_rating_pred,color='blue',linewidth=3)
    plt.xticks(())
    plot.yticks(())
    plt.show()


LR()    