def drinksnaturalization(drinknamerecom):
    ndrinknamerecom = str(drinknamerecom).replace('[', '').replace("'", "").replace(",", " and").replace("'", "").replace(']', '')
    return ndrinknamerecom

def foodnaturalization(foodnamerecom):
    nfoodnamerecom = str(foodnamerecom).replace('[', '').replace("'", "").replace(",", " and").replace("'", "").replace(']', '')

    return nfoodnamerecom
