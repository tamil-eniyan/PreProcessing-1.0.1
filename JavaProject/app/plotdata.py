import pandas as pd
from  matplotlib import pyplot as plt
import matplotlib
import seaborn as sns
import sys

def regression_plot(filename, xlabel, ylabel):
    # create the dataframe using the csv file upload
    df = pd.read_csv(filename)
    # note: the r means to read following slashes as actual slashes, not escape
    # Temp, Year and Rain(fall)
    # How we set width, height using matplotlib settings
    sns.set(rc={'figure.figsize':(12,6)})
    sns_plot = sns.regplot(x=xlabel, y=ylabel, data=df)
    # regression line shows a possible positive correlation - as temp increases so does rainfall.
    plt.show() 
    
    return

if __name__ == '__main__':
    if len(sys.argv) < 4:
       print('You need to specify the filename and x and y coordinate names')
       sys.exit()
    #regression_plot('tempRainYearly.csv','Temp', 'Rain' )
    regression_plot(sys.argv[1],sys.argv[2], sys.argv[3] )
