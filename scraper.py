
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup as bs

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import pyodbc 
conn = pyodbc.connect()

cursor = conn.cursor()    



#def getmoly():
#    path = "c:/users/20315168/downloads/SS316_2.xlsx"
#    data = pd.read_excel(path)
#    rows = []
#    for i in range(len(data)):
#        rows.append(("SS 316" ,data["High"][i] , data["Low"][i]  , "USD/KG", parse(data["Date"][i]).date().isoformat() , parse(data["Date"][i]).strftime('%Y-%m-%d %H:%M:%S') , "fastmarket" , "https://dashboard.fastmarkets.com/w/uHzSfrneruQyZcUjmeCU3M/ss-316-scrap-dashboard", 1  ))
#    print(rows)
     
#    for i in rows: 
#        query = """
#        insert into [dbo].[rpamaterialprice]
#                    ([material]
#                    ,[pricehigh]
#                    ,[pricelow]
#                    ,[unit]
#                    ,[asofdate]
#                    ,[dateadded]
#                    ,[site]
#                    ,[url]
#                    ,[isauthreq])
#                values
#                    {} """.format(i)
        
#        print(query)
#        try:
#            results = cursor.execute(query)
#            print(results)
#        except:
#            print("not added query")
#    cursor.commit()
#getmoly()


#def getIron():
#    path = "C:/Users/20315168/Downloads/Iron.csv"
#    data = pd.read_csv(path,sep='\t')
#    rows = []
#    for i in range(len(data)):
#        rows.append(("Iron" ,data["High"][i] , data["Low"][i]  , "USD/TONNE", parse(data["Date"][i]).date().isoformat() , parse(data["Date"][i]).strftime('%Y-%m-%d %H:%M:%S') , "fastmarket" , "fastmarket.com", 1  ))
#    print(rows)
     
#    for i in rows: 
#        query = """
#        INSERT INTO [dbo].[rpaMaterialPrice]
#                    ([Material]
#                    ,[PriceHigh]
#                    ,[PriceLow]
#                    ,[Unit]
#                    ,[AsOfDate]
#                    ,[DateAdded]
#                    ,[Site]
#                    ,[URL]
#                    ,[isAuthReq])
#                VALUES
#                    {} """.format(i)
        
#        print(query)
#        try:
#            results = cursor.execute(query)
#            print(results)
#        except:
#            print("not added query")
#    cursor.commit()
#getIron()
#def getChromium():
    #path = 'C:/Users/20315168/Desktop/MaterailPriceBot/chromedriver'
    #driver = webdriver.Chrome(path)	
    #driver.get("https://auth.fastmarkets.com/?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dfastmarkets.dashboard.implicit%26redirect_uri%3Dhttps%253A%252F%252Fdashboard.fastmarkets.com%252Fsign-in.html%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520fusion.ui.api%2520fastmarkets.preference.api%2520mindtricks.api.mb_prices%2520fastmarkets.physicalprices.api%2520fusion.search.api%2520fastmarkets.search.api%2520fastmarkets.news.api%2520fastmarkets.alertconfig.api%2520fastmarkets.alertdelivery.api%2520fastmarkets.marketdata.api%2520fastmarkets.newsletter.api%26state%3D524511bc674d4149a3523f2a2b9e8262%26nonce%3Df23765322eb54aca8908bf445e2e7b91%26reqroleany%3Dtrue%26reqrole%3Drole%253A%252F%252Fdashboard,role%253A%252F%252Fplatform%252Fweb-dashboard%26client_version%3DDashboardWeb%252F2.1.8873%26host_app_version%3DChrome%252F93.0.4577.82%26operating_system%3DWindows%252Fwindows-10")

    #search = driver.find_element_by_name('username')
   
    #search.send_keys(Keys.RETURN)


    #password = driver.find_element_by_name('password')
 
    #password.send_keys(Keys.RETURN)


    #time.sleep(5)

    #print(driver.title)

    #time.sleep(5)

    #driver.get('https://dashboard.fastmarkets.com/w/gVhKUnZviiGCRZdYnRw7Gy/chromium-dashboard?widget=r781bppm1GX4MAy5eWj4sj')

    #chromiumhtml = str = """                <div class="ag-center-cols-viewport" ref="eViewport" role="presentation" style="height: 100%;">
    #                <div class="ag-center-cols-container" ref="eContainer" role="rowgroup" unselectable="on" style="width: 294px; height: 3900px;"><div role="row" row-index="0" aria-rowindex="3" row-id="0" comp-id="61" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute ag-row-first" style="height: 30px; transform: translateY(0px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="62" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="63" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="64" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="1" aria-rowindex="4" row-id="1" comp-id="65" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(30px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="66" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="67" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="68" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="2" aria-rowindex="5" row-id="2" comp-id="69" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(60px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="70" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="71" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="72" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="3" aria-rowindex="6" row-id="3" comp-id="73" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(90px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="74" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="75" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="76" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="4" aria-rowindex="7" row-id="4" comp-id="77" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(120px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="78" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="79" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="80" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="5" aria-rowindex="8" row-id="5" comp-id="81" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(150px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="82" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="83" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="84" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="6" aria-rowindex="9" row-id="6" comp-id="85" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(180px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="86" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="87" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="88" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="7" aria-rowindex="10" row-id="7" comp-id="89" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(210px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="90" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="91" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="92" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="8" aria-rowindex="11" row-id="8" comp-id="93" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(240px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="94" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="95" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="96" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="9" aria-rowindex="12" row-id="9" comp-id="97" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(270px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="98" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="99" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="100" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="10" aria-rowindex="13" row-id="10" comp-id="101" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(300px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="102" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="103" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="104" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;">10,550.00</div></div><div role="row" row-index="11" aria-rowindex="14" row-id="11" comp-id="125" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(330px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="144" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="145" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="146" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,550.00</div></div><div role="row" row-index="12" aria-rowindex="15" row-id="12" comp-id="126" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(360px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="148" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="149" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="150" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,550.00</div></div><div role="row" row-index="13" aria-rowindex="16" row-id="13" comp-id="127" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(390px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="152" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="153" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="154" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,550.00</div></div><div role="row" row-index="14" aria-rowindex="17" row-id="14" comp-id="128" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(420px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="156" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="157" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 98px;  ">10,400.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="158" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 196px;  ">10,550.00</div></div><div role="row" row-index="15" aria-rowindex="18" row-id="15" comp-id="129" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(450px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="160" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="161" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,375.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="162" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,500.00</div></div><div role="row" row-index="16" aria-rowindex="19" row-id="16" comp-id="130" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(480px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="164" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="165" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,375.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="166" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,500.00</div></div><div role="row" row-index="17" aria-rowindex="20" row-id="17" comp-id="131" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(510px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="168" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="169" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,375.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="170" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,500.00</div></div><div role="row" row-index="18" aria-rowindex="21" row-id="18" comp-id="132" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(540px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="172" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="173" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 98px;  ">10,375.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="174" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right ag-cell-value" style="width: 98px; left: 196px;  ">10,500.00</div></div><div role="row" row-index="19" aria-rowindex="22" row-id="19" comp-id="133" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(570px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="2" comp-id="176" col-id="MB-CR-0001-low" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 0px;  ">10,250.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="3" comp-id="177" col-id="MB-CR-0001-mid" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 98px;  ">10,375.00</div><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="4" comp-id="178" col-id="MB-CR-0001-high" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height text-align-right published-value ag-cell-value" style="width: 98px; left: 196px;  ">10,500.00</div></div></div>
    #            </div>"""
    #a = bs(chromiumhtml,'html.parser')

    #econtainer = a.find('div',{'ref' : 'eContainer'})

    #Pricerow = econtainer.find_all('div', {'role' : 'row'})   

    #datesQuery = """ <div role="row" row-index="0" aria-rowindex="3" row-id="0" comp-id="39" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute ag-row-first" style="height: 30px; transform: translateY(0px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="40" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">7 Oct 2021</div></div><div role="row" row-index="1" aria-rowindex="4" row-id="1" comp-id="41" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(30px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="42" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">6 Oct 2021</div></div><div role="row" row-index="2" aria-rowindex="5" row-id="2" comp-id="43" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(60px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="44" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">5 Oct 2021</div></div><div role="row" row-index="3" aria-rowindex="6" row-id="3" comp-id="45" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(90px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="46" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">4 Oct 2021</div></div><div role="row" row-index="4" aria-rowindex="7" row-id="4" comp-id="47" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(120px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="48" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">1 Oct 2021</div></div><div role="row" row-index="5" aria-rowindex="8" row-id="5" comp-id="49" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(150px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="50" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">30 Sept 2021</div></div><div role="row" row-index="6" aria-rowindex="9" row-id="6" comp-id="51" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(180px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="52" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">29 Sept 2021</div></div><div role="row" row-index="7" aria-rowindex="10" row-id="7" comp-id="53" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(210px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="54" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">28 Sept 2021</div></div><div role="row" row-index="8" aria-rowindex="11" row-id="8" comp-id="55" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(240px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="56" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">27 Sept 2021</div></div><div role="row" row-index="9" aria-rowindex="12" row-id="9" comp-id="57" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(270px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="58" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">24 Sept 2021</div></div><div role="row" row-index="10" aria-rowindex="13" row-id="10" comp-id="59" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0 ag-row-position-absolute" style="height: 30px; transform: translateY(300px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="60" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;">23 Sept 2021</div></div><div role="row" row-index="11" aria-rowindex="14" row-id="11" comp-id="116" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(330px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="143" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">22 Sept 2021</div></div><div role="row" row-index="12" aria-rowindex="15" row-id="12" comp-id="117" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(360px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="147" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">21 Sept 2021</div></div><div role="row" row-index="13" aria-rowindex="16" row-id="13" comp-id="118" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(390px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="151" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">20 Sept 2021</div></div><div role="row" row-index="14" aria-rowindex="17" row-id="14" comp-id="119" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(420px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="155" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">17 Sept 2021</div></div><div role="row" row-index="15" aria-rowindex="18" row-id="15" comp-id="120" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(450px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="159" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">16 Sept 2021</div></div><div role="row" row-index="16" aria-rowindex="19" row-id="16" comp-id="121" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(480px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="163" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">15 Sept 2021</div></div><div role="row" row-index="17" aria-rowindex="20" row-id="17" comp-id="122" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(510px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="167" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">14 Sept 2021</div></div><div role="row" row-index="18" aria-rowindex="21" row-id="18" comp-id="123" class="ag-row ag-row-no-focus ag-row-even ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(540px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="171" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">13 Sept 2021</div></div><div role="row" row-index="19" aria-rowindex="22" row-id="19" comp-id="124" class="ag-row ag-row-no-focus ag-row-odd ag-row-level-0  ag-row-position-absolute" style="height: 30px; transform: translateY(570px); " aria-label="Press SPACE to select this row."><div tabindex="-1" unselectable="on" role="gridcell" aria-colindex="1" comp-id="175" col-id="date" class="ag-cell ag-cell-not-inline-editing ag-cell-auto-height ag-cell-last-left-pinned text-align-left ag-cell-value" style="width: 150px; left: 0px;  ">10 Sept 2021</div></div> """

    #b = bs(datesQuery,'html.parser')

    #Daterow = b.find_all('div',{'role' : 'row'})
    #rows = []
    #for i in range(len(Daterow)):
    #  li = [Daterow[i].text]
    #  for j in Pricerow[i].find_all('div'):
    #      li.append(j.text)
    #  #rows.append(("Chromium" , float("".join(map(str,li[1].split(',')))), float("".join(map(str,li[3].split(',')))), "USD/TONNE", parse(li[0]).date().isoformat() ,datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "fastmarket" , "fastmarket.com",1))
    #  rows.append(("Chromium" ,float("".join(li[3].split(','))), float("".join(li[1].split(','))) , "USD/TONNE", parse(li[0]).date().isoformat() , parse(li[0]).strftime('%Y-%m-%d %H:%M:%S') , "fastmarket" , "fastmarket.com", 1  ))
    
    #for i in rows: 
    #    query = """
    #    INSERT INTO [dbo].[rpaMaterialPrice]
    #                ([Material]
    #                ,[PriceHigh]
    #                ,[PriceLow]
    #                ,[Unit]
    #                ,[AsOfDate]
    #                ,[DateAdded]
    #                ,[Site]
    #                ,[URL]
    #                ,[isAuthReq])
    #            VALUES
    #                {} """.format(i)
        
    #    print(query)
    #    try:
    #        results = cursor.execute(query)
    #        print(results)
    #    except:
    #        print("not added query")
    #cursor.commit()
    
    #try:
    #    time.sleep(20)
    #    element1 = WebDriverWait(driver, 20).until(
    #    EC.presence_of_element_located((By.XPATH, "//div[@ref='leftContainer']"))
    #    )
    #    print(element1.get_attribute("innerHTML"))
    #except:
        #print("wrror")
#getChromium()
def getData():
    path = 'C:/Users/20315168/Desktop/MaterailPriceBot/chromedriver'

    driver = webdriver.Chrome(path)	

    driver.get("https://auth.fastmarkets.com/?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dfastmarkets.dashboard.implicit%26redirect_uri%3Dhttps%253A%252F%252Fdashboard.fastmarkets.com%252Fsign-in.html%26response_type%3Did_token%2520token%26scope%3Dopenid%2520profile%2520fusion.ui.api%2520fastmarkets.preference.api%2520mindtricks.api.mb_prices%2520fastmarkets.physicalprices.api%2520fusion.search.api%2520fastmarkets.search.api%2520fastmarkets.news.api%2520fastmarkets.alertconfig.api%2520fastmarkets.alertdelivery.api%2520fastmarkets.marketdata.api%2520fastmarkets.newsletter.api%26state%3D524511bc674d4149a3523f2a2b9e8262%26nonce%3Df23765322eb54aca8908bf445e2e7b91%26reqroleany%3Dtrue%26reqrole%3Drole%253A%252F%252Fdashboard,role%253A%252F%252Fplatform%252Fweb-dashboard%26client_version%3DDashboardWeb%252F2.1.8873%26host_app_version%3DChrome%252F93.0.4577.82%26operating_system%3DWindows%252Fwindows-10")

    search = driver.find_element_by_name('username')

    search.send_keys(Keys.RETURN)


    password = driver.find_element_by_name('password')

    password.send_keys(Keys.RETURN)


    time.sleep(5)

    print(driver.title)

    time.sleep(5)

    driver.get('https://dashboard.fastmarkets.com/w/7yVq17rM2AqrUQRmfyFuHV/dashboard-for-moly-chromium-iron-nickel')



    try:
    
        # element1 = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[@title='Ferro-molybdenum 65% Mo min, in-whs Rotterdam, $/kg Mo']"))
        # )
        
        # Iron ore 58% Fe fines, cfr Qingdao, $/tonne
        #
        #
        time.sleep(30)   
        element2  = WebDriverWait(driver,30).until(
            EC.presence_of_element_located((By.TAG_NAME,'ag-grid-angular'))
        )

        bodyDiv = element2.find_element_by_xpath('//div[@ref="eRootWrapper"]')
        #print(bodyDiv.get_attribute("ref"))
        table = bodyDiv.find_element_by_xpath('//div[@ref="eBodyViewport"]')
        #print(table.get_attribute("ref"))
        CenterTable = table.find_element_by_xpath('//div[@ref="centerContainer"]')
        #print(CenterTable.get_attribute("ref"))
        InnerCenterTable = CenterTable.find_element_by_xpath('//div[@ref="eViewport"]')
        #eContainer = InnerCenterTable.find_element_by_xpath('//div[@ref="eContainer"]')
        #print(InnerCenterTable.get_attribute("ref"))

        website = bs(InnerCenterTable.get_attribute('innerHTML'),'html.parser')
    
        #print(website.text)
    
        econtainer = website.find('div',{'ref' : 'eContainer'})
        row = econtainer.find_all('div', {'role' : 'row'})
        li = []
        #print(row)
        for i in row:
          title = i.find('div',{'aria-colindex': '7'}).get('title')
          
          midAnimate = i.find('div',{"col-id" : 'low'})
          lid = midAnimate.find('span').text 
          mid = i.find('div',{'col-id' : 'mid'}).get('title')
          
          highAnimate = i.find('div' , {'col-id' : 'high'})
          high = highAnimate.find('span').text
          
          if(high=='-' and lid=='-' and mid=='-' and title=='-'):
              return None
          else:
              li.append([high ,lid , title])#print(title,lid,mid,high) 
        driver.quit()
        return li
        # eContainer = InnerCenterTable.find_element_by_css_selector('div.ag-center-cols-container')
        #eContainer = InnerCenterTable.find_element_by_xpath('//div[@role="rowgroup"]')
        # # eContainert
        # # for i in InnerCenterTable:
        # #     print(i)
        # Comp = eContainer.find_element_by_xpath('//div[@row-id="MB-FEO-0001"]')
   
        #divs = eContainer.find_elements_by_tag_name('div')
    
        # date = divs[0].find_elements_by_tag_name('div')  print(a.prettify())

        # print(eContainer.get_attribute('innerHTML'))
    except:
        print("exception")
        driver.quit()
        return None

while(True):
    #result = True
    result = getData()
    if(result):
        elements = ["Molybdenum" , "Iron Ore", "Chromium" , "Titanium" , "Vanadium" , "SS 316" , "Nickel"]
        urls = ["https://dashboard.fastmarkets.com/w/2MBSqKgXZYmcuL4UTXZuiJ/ferro-moly-dashboard","https://dashboard.fastmarkets.com/w/4m5sjVSUjj7iFtUdCzke9Y/iron-dashboard","https://dashboard.fastmarkets.com/w/gVhKUnZviiGCRZdYnRw7Gy/chromium-dashboard","https://dashboard.fastmarkets.com/w/ixGe43yY5BRjcP1BhciYCL/titanium-dashboard","https://dashboard.fastmarkets.com/w/i86x4aEji2rjpgWUmLhzMF/vandium-dashboard" , "https://dashboard.fastmarkets.com/w/uHzSfrneruQyZcUjmeCU3M/ss-316-scrap-dashboard" , "https://dashboard.fastmarkets.com/w/fhgXpMBeXV1yi234USWJ7o/lme-nickel-dashboard" ]
        rows = []
        print("adding to database")
        for i in result:
            #print(elements[result.index(i)] , i[0],i[1], i[2], i[3])
            rows.append((elements[result.index(i)] , float("".join(map(str,i[0].split(',')))), float("".join(map(str,i[1].split(',')))), "USD/TONNE", parse(i[2]).date().isoformat() ,datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "fastmarket" , urls[result.index(i)],1))
        print(rows)      
        for i in rows: 
            query = """
            INSERT INTO [dbo].[rpaMaterialPrice]
                        ([Material]
                        ,[PriceHigh]
                        ,[PriceLow]
                        ,[Unit]
                        ,[AsOfDate]
                        ,[DateAdded]
                        ,[Site]
                        ,[URL]
                        ,[isAuthReq])
                    VALUES
                        {} """.format(i)
        
            print(query)
            try:
                results = cursor.execute(query)
                print(results)
            except:
                print("not added query")
        cursor.commit()

#        values = ", ".join(map(str,rows))
#        query2 = """ select top 10 mkaterial from  [dbo].[rpaMaterialPrice]"""
#        query = """
#INSERT INTO [dbo].[rpaMaterialPrice]
#           ([Material]
#           ,[PriceHigh]
#           ,[PriceLow]
#           ,[Unit]
#           ,[AsOfDate]
#           ,[DateAdded]
#           ,[Site]
#           ,[URL]
#           ,[isAuthReq])
#     VALUES
#           {} """.format(values)
#        print(query)
#        try:
#            rows = cursor.execute(query)
#            cursor.commit()
#            print(rows)
#        except:
#            print("database error")
#    else:
#        print("Dont add")
    time.sleep(120)


##time.sleep(5)