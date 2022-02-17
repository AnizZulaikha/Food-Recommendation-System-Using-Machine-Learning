import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from correlation import lunch_drinks_name, dinner_drinks_name
import warnings
warnings.filterwarnings('ignore')
from listnaturalization import drinksnaturalization

def dinnerdrinksrecom(drinksdatasets,drinkNamess):
    # from datasetLoader import dataLoad
    # drinksdatasets = dataLoad()
    print("-DATASET DESCRIBE-\n")
    print(drinksdatasets.describe())
    print("\n--------------------------------------------------------------------------------------\n")

    ratings = pd.DataFrame(drinksdatasets.groupby('drink_name')['rating'].mean())
    ratings['totalRateCounts'] = drinksdatasets.groupby('drink_name')['rating'].count()
    print("-RATINGS MEAN AND TOTAL RATES-\n")
    print(ratings)
    print("\n--------------------------------------------------------------------------------------\n")

    sns.jointplot(x='rating', y='totalRateCounts', data=ratings)
    plt.show()

    drinksUIM = drinksdatasets.pivot_table(index='user_id', columns='drink_name', values='rating')
    print("-USER INTERACTION MATRIX-\n")
    print(drinksUIM)

    print("\n--------------------------------------------------------------------------------------\n")
    print("-TOP 3 HIGH RATING-\n")
    top3 = ratings.sort_values('totalRateCounts', ascending=False).head(3)
    print(top3)
    print("\n--------------------------------------------------------------------------------------\n")

    drinkRatings = dinner_drinks_name(drinksUIM, drinkNamess)
    print("\n--------------------------------------------------------------------------------------\n")
    similar_to_drinkratings = drinksUIM.corrwith(drinkRatings)

    corr_drinks = pd.DataFrame(similar_to_drinkratings, columns=['Correlation'])
    corr_drinks.dropna(inplace=True)

    corr_drinks = corr_drinks.join(ratings['totalRateCounts'])
    print(f"-ALL CORRELATIONS BASED ON {drinkNamess.upper()} -\n")
    print(corr_drinks)
    print("\n--------------------------------------------------------------------------------------\n")
    print(f"-TOP 4 HIGH CORRELATIONS WITH {drinkNamess.upper()}-\n")
    top4 = corr_drinks.sort_values(by='Correlation', ascending=False).head(4)
    print(top4)
    drinkcorr = corr_drinks.sort_values(by='Correlation', ascending=False).head(3)
    drinkcorr = drinkcorr.to_dict(orient='index')
    del drinkcorr[drinkNamess]
    drinknamerecom = list(drinkcorr)
    drinknamerecom = drinksnaturalization(drinknamerecom)
    return drinknamerecom, drinksdatasets.describe(), ratings, drinksUIM, top3, corr_drinks, top4


def lunchdrinksrecom(drinksdatasets, drinkNamess):
    # from datasetLoader import dataLoad
    # drinksdatasets = dataLoad()
    print("-DATASET DESCRIBE-\n")
    print(drinksdatasets.describe())
    print("\n--------------------------------------------------------------------------------------\n")

    ratings = pd.DataFrame(drinksdatasets.groupby('drink_name')['rating'].mean())
    ratings['totalRateCounts'] = drinksdatasets.groupby('drink_name')['rating'].count()
    print("-RATINGS MEAN AND TOTAL RATES-\n")
    print(ratings)
    print("\n--------------------------------------------------------------------------------------\n")

    sns.jointplot(x='rating', y='totalRateCounts', data=ratings)
    plt.show()

    drinksUIM = drinksdatasets.pivot_table(index='user_id', columns='drink_name', values='rating')
    print("-USER INTERACTION MATRIX-\n")
    print(drinksUIM)

    print("\n--------------------------------------------------------------------------------------\n")
    print("-TOP 3 HIGH RATING-\n")
    top3 = ratings.sort_values('totalRateCounts', ascending=False).head(3)
    print(top3)

    drinkRatings = lunch_drinks_name(drinksUIM, drinkNamess)
    print("\n--------------------------------------------------------------------------------------\n")
    similar_to_drinkratings = drinksUIM.corrwith(drinkRatings)


    corr_drinks = pd.DataFrame(similar_to_drinkratings, columns=['Correlation'])
    corr_drinks.dropna(inplace=True)

    corr_drinks = corr_drinks.join(ratings['totalRateCounts'])
    print(f"-ALL CORRELATIONS BASED ON {drinkNamess.upper()} -\n")
    print(corr_drinks)
    print("\n--------------------------------------------------------------------------------------\n")
    print(f"-TOP 4 HIGH CORRELATIONS WITH {drinkNamess.upper()}-\n")
    top4 = corr_drinks.sort_values(by='Correlation', ascending=False).head(4)
    print(top4)
    drinkcorr = corr_drinks.sort_values(by='Correlation', ascending=False).head(3)
    drinkcorr = drinkcorr.to_dict(orient='index')
    del drinkcorr[drinkNamess]
    drinknamerecom = list(drinkcorr)
    drinknamerecom = drinksnaturalization(drinknamerecom)
    return drinknamerecom, drinksdatasets.describe(), ratings, drinksUIM, top3, corr_drinks, top4