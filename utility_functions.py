import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
from fastnumbers import fast_float, isfloat
import requests


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def get_diff_list(arr):
    lst = []
    for i in range(len(arr)-1):
        lst.append(arr[i] - arr[i+1])
        
    return lst


def str_to_float_list(arr):
    lst = []
    for i in range(len(arr)):
        lst.append(fast_float(arr[i].replace(',',''), default=np.nan))
    return lst


def get_point_value(arr, avg = False):
    
    arr = str_to_float_list(arr)
    
    if(avg == True):
        point = sum(get_diff_list(arr/abs(np.average(arr))))
    else:
        point = sum(get_diff_list(arr))
        
    return point


def get_peer_comparison_score(pc):
    mrk = []
    prf = []
    mrk_to_prf = []
    
    mrk_val = fast_float(pc[5].replace(',',''))
    prf_val = fast_float(pc[7].replace(',',''))
    
    for i in range(8, len(pc), 8):
        mrk.append(fast_float(pc[i+5].replace(',','')))
        prf.append(fast_float(pc[i+7].replace(',','')))
  
    for i in prf:
        if(i < 0):
            return 0.8
        
    for i in mrk:
        if(i < mrk_val):
            return 0.8

    for i, j in zip(mrk, prf):
        mrk_to_prf.append((i/mrk_val)/(j/prf_val))
        
    return np.average(mrk_to_prf)


def get_score(url):
    r, _, pl, pc, fi, _ = get_everything(url)
    p1 = get_point_value(pl[1:], avg = True)
    p2 = get_point_value(fi[1:], avg = False)
    p3 = get_point_value(r[1:], avg = True)
    p4 = get_peer_comparison_score(pc)
    p5 = fast_float(fi[1].replace(',',''))/10
    
    p1 = sigmoid(p1)
    p2 = sigmoid(p2)
    p3 = sigmoid(p3)
    p4 = sigmoid(p4)
    p5 = sigmoid(p5)
    
    score = (p1 + p2 + p3 + p4 + p5)*20
    
    return int(round(score, 0))


def get_company_details_and_rating(url):
    response = requests.get(url, timeout=240)
    content = BeautifulSoup(response.content, 'html.parser')
    
    lst = []

    rating = content.find("table", attrs = {"class" : "mctable1"}).find_all("td")
    
    info = content.find("div", attrs = {"class":"morepls_cnt"}).string
    
    lst_price = content.find("tbody", attrs = {"id" : "BSE_history_tbody"}).find_all("td")

    cmp_name = content.find("h1").string
    
    # [last year price, current price, gain]
    last_yr_info = [lst_price[5].string, lst_price[6].string, lst_price[7].string]
    
    if(rating[0].string != 'Moving Averages'):
        rat_val = "Rating Not found"
    else:
        rat_val = rating[1].string
        
    return cmp_name, rat_val, info, last_yr_info


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
