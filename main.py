# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def panda_series():
    s = pd.Series([1,2,3,4,5,6,np.NaN,8,9])
    print(s)
    
    d = pd.date_range('20220101',periods=10)
    df = pd.DataFrame(np.random.randn(10,4),index=d,columns=['A','B','C','D'])
    print(df)
    print(df.dtypes)

def pandas_exampl_dict_to_df():
    df1 = pd.DataFrame({'A':[1,2,3,4],
                        'B':pd.Timestamp('20220101'),
                        'C':pd.Series(1,index=list(range(4)), dtype='int32'),
                        'D':np.array([5]*4, dtype='int32'),
                        'E':pd.Categorical(['True','False','False','True']),
                        'F':'Edureka'
    })
    print(df1)
    print(df1.dtypes)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    panda_series()
    pandas_exampl_dict_to_df()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
