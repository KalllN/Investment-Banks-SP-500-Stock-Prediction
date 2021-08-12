import pandas as pd
from pandas import DataFrame

#Loading data

#from google.colab import files #opens files in computer

#uploaded = files.upload()

JPM = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/JPM_data.csv')

BOA = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/BAC_data.csv')

CITI = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/C_data.csv')

GS = pd.read_csv('../input/sandp500/individual_stocks_5yr/individual_stocks_5yr/GS_data.csv')

JPM['date'] = pd.to_datetime(JPM['date'])
BOA['date'] = pd.to_datetime(BOA['date'])
CITI['date'] = pd.to_datetime(CITI['date'])
GS['date'] = pd.to_datetime(GS['date'])
