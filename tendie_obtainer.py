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
               #print(i)
               print(k)
               for j in i:
                   #print(j)
                   if j=="." and k<4500:
                       self.csvimport2=self.csvimport.drop(self.csvimport.index[k], inplace=True)
                       #,inplace=True)
           print(self.csvimport2)
       WordSearch(self)
       
                        
   
c=MacroEco()
c.Exchange()

        
                            
            csvimport=csvimport[~csvimport['Symbol'.str.contains('.')]]
            
            
            csv3=pd.merge(csvimport,csvimport2[['Symbol','Name']],how='left',left_on=['Symbol'],right_on=['Symbol'])

def GetEarnings(self):
        #Finviz scrape earnings
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        print(csv3)
        count_ = 0
        for j,i in enumerate(ar_):
            url_ = r"https://finviz.com/quote.ashx?t={}&ty=c&ta=1&p=d".format(i)
            driver.get(url_)
            edate =driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/table/tbody/tr[7]/td/table/tbody/tr[11]/td[6]").text
            print(edate)
            beta = driver.find_element_by_xpath("/html/body/table[3]/tbody/tr[1]/td/table/tbody/tr[7]/td/table/tbody/tr[7]/td[12]").text
            csv3.loc[count_,'Earnings Date'] = edate
            csv3.loc[count_,'Beta'] = beta
            print(csv3['Earnings Date'])
            count_ = count_+1
            if j==5:
                break
        return csv3