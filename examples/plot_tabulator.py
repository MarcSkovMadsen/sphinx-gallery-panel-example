import datetime as dt
import numpy as np
import pandas as pd
import panel as pn

np.random.seed(7)
pn.extension('tabulator')

df = pd.DataFrame({
    'int': [1, 2, 3],
    'float': [3.14, 6.28, 9.42],
    'str': ['A', 'B', 'C'],
    'bool': [True, False, True],
    'date': [dt.date(2019, 1, 1), dt.date(2020, 1, 1), dt.date(2020, 1, 10)],
    'datetime': [dt.datetime(2019, 1, 1, 10), dt.datetime(2020, 1, 1, 12), dt.datetime(2020, 1, 10, 13)]
}, index=[1, 2, 3])

df_widget = pn.widgets.Tabulator(df, buttons={'Print': "<i class='fa fa-print'></i>"})
df_widget