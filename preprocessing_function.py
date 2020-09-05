import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur

# For input, use this url : https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI

def get_everything(url):
    stock_name = url.split('/')[-2]
    stock_code = url.split('/')[-1]
    
    pl_url = "https://www.moneycontrol.com/financials/" + stock_name + "/consolidated-profit-lossVI/" + stock_code
    
    read_data_financials = ur.urlopen(pl_url).read()
    financials_soup= BeautifulSoup(read_data_financials, features = "lxml")

    financials = []
    for l in financials_soup.find_all('td'):
        financials.append(l.string)

    for i in range(len(financials)):
        if(financials[i] == 'Total Revenue'):
            idx_rv = i
        if(financials[i] == 'Total Expenses'):
            idx_ex = i
        if(financials[i] == 'Profit/Loss For The Period'):
            idx_pl = i

    revenue = financials[idx_rv:idx_rv + 6]
    expenses = financials[idx_ex:idx_ex + 6]
    profit_loss = financials[idx_pl:idx_pl + 6]

    read_data_company = ur.urlopen(url).read()
    company_soup = BeautifulSoup(read_data_company, "lxml")

    company = []
    for items in company_soup.find_all('td'):
        company.append(items.string)

    for i in range(len(company)):
        if(company[i] == 'Total'):
            cidx_pr = i
        if(company[i] == 'FII/FPI'):
            cidx_fi = i
        if(company[i] == ' High Price '):
            cidx_hp = i

    peer_cmp = company[-40:]
    fii = company[cidx_fi:cidx_fi + 5]
    high_price = company[cidx_hp:cidx_hp + 4]
    
    return revenue, expenses, profit_loss, peer_cmp, fii, high_price
