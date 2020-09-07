# Stock-Buddy

Stock Buddy determines if the company stock is worth buying or not. It generates a score for the company's stock to determine how good the stock is for investement

## What it solves ? 
There are millions of companies in the stock market. How to determine which are the good companies to invest in? If you end up investing in a poor performing company, then its more likely that you are just going to lose your money. That's why investing in the stock market is risky if you don't analyse the company you are investing in.

But analysing the company is only an expert's cup of tea! That's why Stock Buddy has made it simple. All the expert knowledge combined with the algorithmic capabilities, the Stock Buddy analyse the company for normal investors who don't have much knowledge on stock marketing. All they need to do is, just pass the stock url from moneycontrol.com and get the score showing if the company is good for investment or not.

No need to study all those scary numbers on the balance sheet of the company. No need to have expert knowledge to find good companies to invest in. No need to spend alot of time studying a poor performing company. Just enter the url and hit the button. Everything is done for you !

## How the company is analysed in stock market ?
The company's balance sheet and income statement plays a major role in determining the performance of the company. Following are the characteristics of the good performing companies in stock market :
- Revenue increasing every year
- Profit increasing every year
- Share price increasing every year
- high % of foreign investors in the company

Other Analysis includes :
- Comparing its performance with its peer companies in the same sector
- The profit and the market capital of the company is compared with some of the largest companies in the same sector. This way, an idea can be generalised how the company will perform if its market capital increases in the future
- Knowing if the company too large ? Or it can make significant amount of growth in the future ?

***All/some of the above factors are extracted and are properly computed in a formula, to generate the score for the company.***

[Note : The knownledge of analysing the company is learned from one of the stock market expert and from other few resources]

## How to use the app ?
Anyone who is investing in stock market or is keen to invest in the stock market, knows about moneycontrol.com . It is the place, where all the required information about the company and it's share price is available.

Simple steps to generate the score of the company :

#### Step 1 : Go to Moneycontrol.com
#### Step 2 : Search for the company you want to analyse
#### Step 3 : Copy the link on top of the moneycontrol window
#### Step 4 : Paste it on the stock buddy
#### Step 5 : Get the Score !!!

![demo](https://github.com/Jaimin09/Stock-Buddy/blob/master/Images/sbtut.gif?raw=true)

## Technologies Used :
- Python, Flask
- Web Scraping
- Front-end and Back-end technology
- HTML, CSS
- The formula is generated to calculate the score, based on the above mentioned factors

## Files :
- Images (folder) : contains required images for the README.md file
- static/main_page.html : generates the front page of the web-application. It then pass the information (url) to the backend, which is processed in python to generate the score
- templates/analyse_stock.html : prints the score and other information passed by the backend. The score determines the performance of the company. The other information give more info about the company to the user.
- static/error.html : This page is called when any error is generated. Error can be caused by entering invalid url.
