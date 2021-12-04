import pandas as pd

def getDataFrame(filename):
    df = pd.read_html(open("{}.html".format(filename)),header=0)
    df = df[0]

    # remove any exempted module
    df = df[df.Status != 'EXEMPTED']
    df.reset_index(inplace=True)
    return df