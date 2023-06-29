import glob
import pandas as pd
import numpy as np

def summary():
    files = glob.glob("*.csv")
    df = []
    z = 0
    for f in files:
        z += 1
        csv = pd.read_csv(f)
        df.append(csv)

    df = pd.concat(df)

    attendance = pd.pivot_table(df, index='rollno', values='att', aggfunc=np.sum)
    attendance['Percentage'] = attendance['att'] / z * 100

    print(attendance)
