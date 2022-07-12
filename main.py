

import pandas as pd
import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

#pdr.get_data_fred('GS10')

#plt.plot([2, 4, 8, 16, 32, 100])
#plt.ylabel('O meu por voce')
#plt.show()


#start = "01/20/2000"
#google = pdr.DataReader(name ="GOOGL",data_source='yahoo',start=start)
#tesla = pdr.DataReader(name ="TSLA",data_source='yahoo',start=start)
#tesla['Close'].plot(figsize=(8,8), label = 'Tesla')
#google['Open'].plot(figsize=(10,10), label = 'Google')


var = pd.read_excel("cdi_dados.xlsm")
ANO = list(var['Data'])
SELIC = list(var['SELIC Anualizada'])
IBOV = list(var['IBOV'])

X = ['2000', '2001', '2002', '2003','2004', '2005', '2006', '2007','2008', '2009','2010','2011','2012',
     '2013','2014','2015','2016','2017','2018','2019','2020','2021']


X_axis = np.arange(len(X))

plt.bar(X_axis - 0.1, SELIC, 0.4, label='SELIC')
plt.bar(X_axis + 0.1, IBOV, 0.4, label='Ibovespa')

plt.xticks(X_axis, X)
plt.xlabel("Ano")
plt.ylabel("Retorno Anual")
plt.title("Selic X Ibovespa")
plt.legend()
plt.show()




