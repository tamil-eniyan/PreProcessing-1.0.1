import pandas as pd
import sys

def stats_columns(filename, xlabel, ylabel):
    df = pd.read_csv(filename)

    xdata = df[xlabel]
    ydata = df[ylabel]

    xstats = xdata.describe()
    ystats = ydata.describe()
    
    return xstats, ystats

if __name__ == '__main__':
    if len(sys.argv) < 4:
       print('You need to specify the filename and x and y coordinate names')
       sys.exit()
    #stats_columns('tempRainYearly.csv','Temp', 'Rain' )
    print(stats_columns(sys.argv[1],sys.argv[2], sys.argv[3] ))
