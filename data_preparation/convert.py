import pandas as pd 
import datetime
from datetime import timedelta, date 
import warnings
import calendar
warnings.filterwarnings('ignore')

# Helper functions
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def date_to_month(date): 
    month_val = date.month
    if int(month_val) < 10: 
        month_val = '0' + str(month_val)
    return month_val

def month_descr(month): 
    month_d = calendar.month_abbr[int(month)]
    return month_d

def ico_on_date(date): 
    ico_active = ico[ico['start'] <= date][ico['end'] >= date]
    num = ico_active['name'].nunique()
    return num

# Read information on Ethereum transactions
transactions = pd.read_csv('tx.csv')
transactions['date'] = pd.to_datetime(transactions['timestamp'], unit='s')
transactions['month'] = transactions['date'].apply(date_to_month)
transactions['month_descr'] = transactions['month'].apply(month_descr)
transactions['year'] = transactions['date'].dt.year 
transactions['period_n'] = transactions['year'].map(str) + '-' + transactions['month'].map(str)
transactions['period'] = transactions['month_descr'] + '-' + transactions['year'].map(str)

# Get a subset of transactions since Mar 2016
transactions_filtered = transactions[transactions['date'] >= datetime.date(2016, 3, 1)]
# print transactions_filtered.head()

transactions_filtered = transactions_filtered[transactions_filtered['date'] < datetime.date(2017, 10, 1)]

# Read information on ICO statistics
ico = pd.read_csv('ICO_stats_initial_cleanup.csv')
ico['start'] = pd.to_datetime(ico['start'], format='%d-%b-%y')
ico['end'] = pd.to_datetime(ico['end'], format='%d-%b-%y')
ico['name'] = ico.name.str.replace('[^A-Za-z()\s]+', '')

transactions_filtered['ico_run'] = transactions['date'].apply(ico_on_date)

# Grouping by weeks as daily is too detailed to show on one graph
grouped_transactions = transactions_filtered.groupby(["period_n", 'period'])[['period_n','transactions', 'ico_run']].sum()
grouped_transactions = grouped_transactions.reset_index()
grouped_transactions = grouped_transactions.sort_values('period_n', ascending=True)
del grouped_transactions['period_n']

grouped_transactions.to_csv('tx_final.csv')