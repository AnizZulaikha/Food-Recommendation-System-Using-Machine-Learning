import sys
from PyQt5.uic import loadUi

from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QMessageBox
from datasetLoader import dataLoad, clearData

from drinks import lunchdrinksrecom,dinnerdrinksrecom
from food import lunchfoodrecom,dinnerfoodrecom

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomeui.ui", self)
        self.lunchbtn.clicked.connect(self.gotolunch)
        self.dinnerbtn.clicked.connect(self.gotodinner)
        self.exit.clicked.connect(self.exitSys)
    def gotolunch(self):
        try:
            WelcomeScreen.gotolunch.name = self.nametxt.text()
            print(WelcomeScreen.gotolunch.name)
        except:
            print("error")
        lunch = LunchScreen()
        widget.addWidget(lunch)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodinner(self):
        try:
            WelcomeScreen.gotodinner.name = self.nametxt.text()
            print(WelcomeScreen.gotodinner.name)
        except:
            print("error")
        dinner = DinnerScreen()
        widget.addWidget(dinner)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def exitSys(self):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:

            prompt = QMessageBox.question(
            self, "Message",
            f"Thank you for using our system",
            QMessageBox.Ok)
            if prompt == QMessageBox.Ok:
                app.quit()

        else:
            pass






class DinnerScreen(QDialog):

    def __init__(self):
        super(DinnerScreen, self).__init__()
        loadUi("dinner.ui", self)
        self.browsefood.clicked.connect(self.loadfooddataset)
        self.browsedrinks.clicked.connect(self.loaddrinkdataset)
        self.start2btn.clicked.connect(self.generateCorr)
        self.exit.clicked.connect(self.exitSys)

    def loadfooddataset(self):
        try:
            self.lunchds = dataLoad()
        except:
            print("Error Load food dataset")
    def loaddrinkdataset(self):
        try:
            self.drinkds = dataLoad()
        except:
            print("Error Load drink dataset")

    def exitSys(self):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:

            prompt = QMessageBox.question(
                self, "Message",
                f"Thank you for using our system",
                QMessageBox.Ok)
            if prompt == QMessageBox.Ok:
                app.quit()

        else:
            pass



    def generateCorr(self):
        try:
            foodNamess = str(self.foodcmb.currentText())
            drinkNamess = str(self.drinkcmb.currentText())
            dinnerfoodnamerecom, dsdesc, foodratings, foodUIM, top3food, corr_food, top4food = dinnerfoodrecom(self.lunchds, foodNamess)
            dinnerdrinknamerecom, drdsdesc, drinkratings, drinksUIM, top3drink, corr_drinks, top4drink = dinnerdrinksrecom(self.drinkds, drinkNamess)
            # ALL OUTPUT FOR FOOD
            self.output.setText("\n=========================================FOOD=========================================\n")
            self.output.append("-DATASET DESCRIBE-\n")
            self.output.append(f"{dsdesc}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-RATINGS MEAN AND TOTAL RATES-\n")
            self.output.append(f"{foodratings}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-USER INTERACTION MATRIX-\n")
            self.output.append(f"{foodUIM}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-TOP 3 HIGH RATING-\n")
            self.output.append(f"{top3food}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-ALL CORRELATIONS BASED ON {foodNamess.upper()} -\n")
            self.output.append(f"{corr_food}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-TOP 4 HIGH CORRELATIONS WITH {foodNamess.upper()}-\n")
            self.output.append(f"{top4food}")

            # ALL OUTPUT FOR DRINKS
            self.output.append("\n=========================================DRINKS=========================================\n")
            self.output.append("-DATASET DESCRIBE-\n")
            self.output.append(f"{drdsdesc}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-RATINGS MEAN AND TOTAL RATES-\n")
            self.output.append(f"{drinkratings}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-USER INTERACTION MATRIX-\n")
            self.output.append(f"{drinksUIM}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-TOP 3 HIGH RATING-\n")
            self.output.append(f"{top3drink}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-ALL CORRELATIONS BASED ON {drinkNamess.upper()} -\n")
            self.output.append(f"{corr_drinks}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-TOP 4 HIGH CORRELATIONS WITH {drinkNamess.upper()}-\n")
            self.output.append(f"{top4drink}")
            self.output.append("\n======================RECOMENDATION RESULT======================\n")
            self.output.append(f"{WelcomeScreen.gotodinner.name.title()}, Based on your preferences, we would like to suggest you for lunch :- \nFood : {str(dinnerfoodnamerecom)} which have the highest correlation with your favourite food... \nDrink : {str(dinnerdrinknamerecom)} which have the highest correlation with your favourite drinks... \nThank You for using our systems....")

        except:
            print("Error fetching values")


class LunchScreen(QDialog):

    def __init__(self):
        super(LunchScreen, self).__init__()
        loadUi("lunch.ui", self)
        self.browsefood.clicked.connect(self.loadfooddataset)
        self.browsedrinks.clicked.connect(self.loaddrinkdataset)
        self.start2btn.clicked.connect(self.generateCorr)
        self.exit.clicked.connect(self.exitSys)

    def loadfooddataset(self):
        try:
            self.lunchds = dataLoad()
        except:
            print("Error Load food dataset")
    def loaddrinkdataset(self):
        try:
            self.drinkds = dataLoad()
        except:
            print("Error Load drink dataset")


    def exitSys(self):
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit?",
            QMessageBox.Yes | QMessageBox.Cancel)
        if reply == QMessageBox.Yes:

            prompt = QMessageBox.question(
                self, "Message",
                f"Thank you for using our system",
                QMessageBox.Ok)
            if prompt == QMessageBox.Ok:
                app.quit()

        else:
            pass

    def generateCorr(self):
        try:
            foodNamess = str(self.foodcmb.currentText())
            drinkNamess = str(self.drinkcmb.currentText())
            lunchfoodnamerecom, dsdesc, foodratings, foodUIM, top3food, corr_food, top4food = lunchfoodrecom(self.lunchds, foodNamess)
            lunchdrinknamerecom, drdsdesc, drinkratings, drinksUIM, top3drink, corr_drinks, top4drink = lunchdrinksrecom(self.drinkds, drinkNamess)
            # ALL OUTPUT FOR FOOD
            self.output.setText("\n=========================================FOOD=========================================\n")
            self.output.append("-DATASET DESCRIBE-\n")
            self.output.append(f"{dsdesc}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-RATINGS MEAN AND TOTAL RATES-\n")
            self.output.append(f"{foodratings}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-USER INTERACTION MATRIX-\n")
            self.output.append(f"{foodUIM}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-TOP 3 HIGH RATING-\n")
            self.output.append(f"{top3food}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-ALL CORRELATIONS BASED ON {foodNamess.upper()} -\n")
            self.output.append(f"{corr_food}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-TOP 4 HIGH CORRELATIONS WITH {foodNamess.upper()}-\n")
            self.output.append(f"{top4food}")

            # ALL OUTPUT FOR DRINKS
            self.output.append("\n=========================================DRINKS=========================================\n")
            self.output.append("-DATASET DESCRIBE-\n")
            self.output.append(f"{drdsdesc}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-RATINGS MEAN AND TOTAL RATES-\n")
            self.output.append(f"{drinkratings}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-USER INTERACTION MATRIX-\n")
            self.output.append(f"{drinksUIM}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")

            self.output.append("-TOP 3 HIGH RATING-\n")
            self.output.append(f"{top3drink}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-ALL CORRELATIONS BASED ON {drinkNamess.upper()} -\n")
            self.output.append(f"{corr_drinks}")
            self.output.append("\n--------------------------------------------------------------------------------------\n")
            self.output.append(f"-TOP 4 HIGH CORRELATIONS WITH {drinkNamess.upper()}-\n")
            self.output.append(f"{top4drink}")
            self.output.append("\n======================RECOMENDATION RESULT======================\n")
            self.output.append(f"{WelcomeScreen.gotolunch.name.title()}, Based on your preferences, we would like to suggest you for lunch :- \nFood : {str(lunchfoodnamerecom)} which have the highest correlation with your favourite food... \nDrink : {str(lunchdrinknamerecom)} which have the highest correlation with your favourite drinks... \nThank You for using our systems....")

        except:
            print("Error fetching values")

#main
app = QApplication(sys.argv)
welcome=WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(681)
widget.setFixedWidth(963)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")