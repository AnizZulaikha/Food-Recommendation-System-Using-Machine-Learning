def dataLoad():
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()  # hide Tk windows from open
    filename = askopenfilename()

    import pandas as pd
    dataset = pd.read_csv(filename)
    return dataset

def clearData():

    dataset = " "
    return dataset

