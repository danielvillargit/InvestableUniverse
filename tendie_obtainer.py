# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:15:52 2020

@author: Daniel
"""





class MacroEco:

    def Exchange(self):
       global csvimport
       import pandas as pd
       pd.set_option('display.max_rows',400)
       pd.set_option('display.max_columns',400)
       df2=pd.read_csv(r'C:\Users\Daniel\Downloads\companylist.csv')
       self.csvimport=pd.DataFrame(df2)
       self.csvimport=df2.drop_duplicates(subset='Name',keep='last')
       self.csvimport=self.csvimport[self.csvimport['Exchange'].isin(['AMEX','NYSE','NQNM'])]
       self.csvimport.reset_index(inplace=True)
       print(self.csvimport.index)
       def WordSearch(self):
           self.csvimport2=self.csvimport['Symbol']
           for k,i in enumerate(self.csvimport['Symbol']):
               print(i)
               
               for j in i:
                   print(j)
                   if "." in j:
                       self.csvimport2=self.csvimport.drop(self.csvimport.index[k], inplace=True)
                       self.csvimport2.reset_index(inplace=True)
                       #,inplace=True)
           print(self.csvimport2)
       WordSearch(self)
       
                        
   
c=MacroEco()
c.Exchange()

        
    def AmerConnect():
        #Connecting to TDAmeritradeAPI
        api_key=str(input("Enter TD Ameritrade API Key: "))
        #0 Starts on Monday
        ticker = 'ET'
        baseurl = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(ticker)
        par_=['Company','description','bid','ask','volatility','openInterest','strikePrice','daysToExpiration']
        sendparam = {'apikey':api_key,'periodType': 'day', 'period': '2', 'frequencyType':'day','frequency':'1','needExtendedHoursData':'false'}
        content_ = requests.get(url = baseurl, params = sendparam)
        dat = content_.json()
        print(dat)
        
    AmerConnect()
    
        
        
        
        
 
def GetEarnings(self):
        #Finviz scrape earnings
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        print(csv3)
        count_ = 0
        
        #i needs to be csvimport from Exchange in this case
        for j,i in enumerate(ar_):
            url_ = r"https://finviz.com/quote.ashx?t={}&ty=c&ta=1&p=d".format(i)
            driver.get(url_)
            marketcap =driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/table/tbody/tr[7]/td/table/tbody/tr[2]/td[2]").text
            print(marketcap)
            
            industry = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/table/tbody/tr[6]/td/table/tbody/tr[2]/td/table/tbody/tr[3]/td/a[1]").text
            csv3.loc[count_,'Industry'] = industry
            csv3.loc[count_,'MarketCap'] = marketcap
            print(csv3['Industry'])
            count_ = count_+1
            if j==5:
                break
        return csv3