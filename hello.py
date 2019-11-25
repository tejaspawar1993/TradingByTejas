from nsepy import get_history
from datetime import date
data = get_history(symbol="SBIN", start=date(2015,1,1), end=date(2015,1,31))
data[['Close']].plot()
#print(data)
import pandas as pd
volume = data['Volume']
df = pd.DataFrame(volume)
df = df.sort_values(by='Volume')
#print(df)
#print('data.mean')
#print(data['Close'].mean())
meanVolume = data['Volume'].mean()
#print(meanVolume)
import numpy as np

#print(np.median(data['Volume']))
from nsetools import Nse
nse = Nse()
#print(nse)
q = nse.get_quote('infy')
var = nse.get_index_list()
print(var)
from pprint import pprint
pprint(q)
#pprint(q['symbol'])

all_stocks = nse.get_stock_codes()
#print(all_stocks)


final_data = {'SYMBOL':0}
import time
all_stocks = {'3MINDIA': '3M India Limited', 'AARTIIND': 'Aarti Industries Limited', 'ABB': 'ABB India Limited', 'ABBOTINDIA': 'Abbott India Limited', 'ABCAPITAL': 'Aditya Birla Capital Limited', 'ABFRL': 'Aditya Birla Fashion and Retail Limited', 'ACC': 'ACC Limited', 'ADANIENT': 'Adani Enterprises Limited', 'ADANIGAS': 'Adani Gas Limited', 'ADANIGREEN': 'Adani Green Energy Limited', 'ADANIPORTS': 'Adani Ports and Special Economic Zone Limited', 'ADANIPOWER': 'Adani Power Limited', 'ADANITRANS': 'Adani Transmission Limited',
'ASIANPAINT': 'Asian Paints Limited',
              'AUBANK': 'AU Small Finance Bank Limited',
              'AVANTIFEED': 'Avanti Feeds Limited', 'AVTNPL': 'AVT Natural Products Limited',
              'AXISBANK': 'Axis Bank Limited',
'BAJAJ-AUTO': 'Bajaj Auto Limited', 'BAJAJCON': 'Bajaj Consumer Care Limited', 'BAJAJELEC': 'Bajaj Electricals Limited', 'BAJAJFINSV': 'Bajaj Finserv Limited', 'BAJAJHIND': 'Bajaj Hindusthan Sugar Limited', 'BAJAJHLDNG': 'Bajaj Holdings & Investment Limited', 'BAJFINANCE': 'Bajaj Finance Limited',
'BALKRISIND': 'Balkrishna Industries Limited',
'BANDHANBNK': 'Bandhan Bank Limited', 'BANKBARODA': 'Bank of Baroda', 'BANKINDIA': 'Bank of India', 'BANSWRAS': 'Banswara Syntex Limited',
'BATAINDIA': 'Bata India Limited',
'BEL': 'Bharat Electronics Limited', 'BEML': 'BEML Limited',
'BPCL': 'Bharat Petroleum Corporation Limited',
'CADILAHC': 'Cadila Healthcare Limited',
'BHARTIARTL': 'Bharti Airtel Limited',
'CGPOWER': 'CG Power and Industrial Solutions Limited',
'COALINDIA': 'Coal India Limited', 'DRREDDY': "Dr. Reddy's Laboratories Limited",
'EICHERMOT': 'Eicher Motors Limited', 'EQUITAS': 'Equitas Holdings Limited',
'GAIL': 'GAIL (India) Limited', 'GRAPHITE': 'Graphite India Limited', 'GRASIM': 'Grasim Industries Limited',
'HCLTECH': 'HCL Technologies Limited', 'HDFC': 'Housing Development Finance Corporation Limited', 'HDFCAMC': 'HDFC Asset Management Company Limited', 'HDFCBANK': 'HDFC Bank Limited', 'HDFCLIFE': 'HDFC Life Insurance Company Limited', 'HDIL': 'Housing Development and Infrastructure Limited', 'HEG': 'HEG Limited'
    
}

all_stocks1 = {'ABBOTINDIA': 'Abbott India Limited',
'ABFRL': 'Aditya Birla Fashion and Retail Limited',
'ACC': 'ACC Limited',
'ADANIENT': 'Adani Enterprises Limited',
'ADANIGAS': 'Adani Gas Limited',
'ADANIGREEN': 'Adani Green Energy Limited',
'ADANIPORTS': 'Adani Ports and Special Economic Zone Limited',
'ADANIPOWER': 'Adani Power Limited',
'ADANITRANS': 'Adani Transmission Limited',
'AJANTPHARM': 'Ajanta Pharma Limited',
'AMBUJACEM': 'Ambuja Cements Limited',
'ASHOKLEY': 'Ashok Leyland Limited',
'ASIANPAINT': 'Asian Paints Limited',
'AUBANK': 'AU Small Finance Bank Limited',
'AUROPHARMA': 'Aurobindo Pharma Limited',
'AVANTIFEED': 'Avanti Feeds Limited',
'AXISBANK': 'Axis Bank Limited',
'BAJAJ-AUTO': 'Bajaj Auto Limited',
'BAJAJCON': 'Bajaj Consumer Care Limited',
'BAJAJELEC': 'Bajaj Electricals Limited',
'BAJAJFINSV': 'Bajaj Finserv Limited',
'BAJFINANCE': 'Bajaj Finance Limited',
'BANDHANBNK': 'Bandhan Bank Limited',
'BANKBARODA': 'Bank of Baroda',
'BANKINDIA': 'Bank of India',
'BATAINDIA': 'Bata India Limited',
'BEML': 'BEML Limited',
'BERGEPAINT': 'Berger Paints (I) Limited',
'BHARTIARTL': 'Bharti Airtel Limited',
'BHEL': 'Bharat Heavy Electricals Limited',
'BIOCON': 'Biocon Limited',
'BLUEDART': 'Blue Dart Express Limited',
'BOROSIL': 'Borosil Glass Works Limited',
'BOSCHLTD': 'Bosch Limited',
'BPCL': 'Bharat Petroleum Corporation Limited',
'CADILAHC': 'Cadila Healthcare Limited',
'CANBK': 'Canara Bank',
'CANFINHOME': 'Can Fin Homes Limited',
'CAPACITE': "Capacit'e Infraprojects Limited",
'CGPOWER': 'CG Power and Industrial Solutions Limited',
'CIPLA': 'Cipla Limited',
'CONCOR': 'Container Corporation of India Limited',
'CROMPTON': 'Crompton Greaves Consumer Electricals Limited',
'CUMMINSIND': 'Cummins India Limited',
'DABUR': 'Dabur India Limited',
'DBL': 'Dilip Buildcon Limited',
'DHFL': 'Dewan Housing Finance Corporation Limited',
'DIXON': 'Dixon Technologies (India) Limited',
'DLF': 'DLF Limited',
'DMART': 'Avenue Supermarts Limited',
'EDELWEISS': 'Edelweiss Financial Services Limited',
'EICHERMOT': 'Eicher Motors Limited',
'EQUITAS': 'Equitas Holdings Limited',
'FORCEMOT': 'FORCE MOTORS LTD',
'FORTIS': 'Fortis Healthcare Limited',
'GAIL': 'GAIL (India) Limited',
'GLENMARK': 'Glenmark Pharmaceuticals Limited',
'GRAPHITE': 'Graphite India Limited',
'GRASIM': 'Grasim Industries Limited',
'GRAVITA': 'Gravita India Limited',
'HDFC': 'Housing Development Finance Corporation Limited',
'HDFCAMC': 'HDFC Asset Management Company Limited',
'HDFCBANK': 'HDFC Bank Limited',
'HDFCLIFE': 'HDFC Life Insurance Company Limited',
'HDIL': 'Housing Development and Infrastructure Limited',
'HEG': 'HEG Limited',
'HEROMOTOCO': 'Hero MotoCorp Limited',
'HINDALCO': 'Hindalco Industries Limited',
'HINDCOPPER': 'Hindustan Copper Limited',
'HINDMOTORS': 'Hindustan Motors Limited',
'HUDCO': 'Housing & Urban Development Corporation Limited',
'IBULHSGFIN': 'Indiabulls Housing Finance Limited',
'ICICIBANK': 'ICICI Bank Limited',
'ICICIGI': 'ICICI Lombard General Insurance Company Limited',
'ICICIPRULI': 'ICICI Prudential Life Insurance Company Limited',
'ICIL': 'Indo Count Industries Limited',
'IDBI': 'IDBI Bank Limited',
'IDEA': 'Vodafone Idea Limited',
'IDFC': 'IDFC Limited',
'IDFCFIRSTB': 'IDFC First Bank Limited',
'INDUSINDBK': 'IndusInd Bank Limited',
'INFIBEAM': 'Infibeam Avenues Limited',
'INFRATEL': 'Bharti Infratel Limited',
'INFY': 'Infosys Limited',
'IRB': 'IRB Infrastructure Developers Limited',
'IRCTC': 'Indian Railway Catering And Tourism Corporation Limited',
'JETAIRWAYS': 'Jet Airways (India) Limited',
'JINDALSTEL': 'Jindal Steel & Power Limited',
'JSWSTEEL': 'JSW Steel Limited',
'JTEKTINDIA': 'Jtekt India Limited',
'JUBILANT': 'Jubilant Life Sciences Limited',
'JUBLFOOD': 'Jubilant Foodworks Limited',
'JUBLINDS': 'Jubilant Industries Limited',
'JUMPNET': 'Jump Networks Limited',
'JUSTDIAL': 'Just Dial Limited',
'KOTAKBANK': 'Kotak Mahindra Bank Limited',
'LAURUSLABS': 'Laurus Labs Limited',
'LICHSGFIN': 'LIC Housing Finance Limited',
'LT': 'Larsen & Toubro Limited',
'LTI': 'Larsen & Toubro Infotech Limited',
'LTTS': 'L&T Technology Services Limited',
'LUPIN': 'Lupin Limited',
'M&M': 'Mahindra & Mahindra Limited',
'M&MFIN': 'Mahindra & Mahindra Financial Services Limited',
'MAHABANK': 'Bank of Maharashtra',
'MANAPPURAM': 'Manappuram Finance Limited',
'MANPASAND': 'Manpasand Beverages Limited',
'MARICO': 'Marico Limited',
'MARUTI': 'Maruti Suzuki India Limited',
'MASFIN': 'MAS Financial Services Limited',
'MGL': 'Mahanagar Gas Limited',
'MHRIL': 'Mahindra Holidays & Resorts India Limited',
'MINDTREE': 'MindTree Limited',
'MPHASIS': 'MphasiS Limited',
'MRF': 'MRF Limited',
'MTNL': 'Mahanagar Telephone Nigam Limited',
'MUTHOOTCAP': 'Muthoot Capital Services Limited',
'MUTHOOTFIN': 'Muthoot Finance Limited',
'NAUKRI': 'Info Edge (India) Limited',
'NBCC': 'NBCC (India) Limited',
'NCC': 'NCC Limited',
'NESCO': 'Nesco Limited',
'NESTLEIND': 'Nestle India Limited',
'NETWORK18': 'Network18 Media & Investments Limited',
'NILKAMAL': 'Nilkamal Limited',
'NITCO': 'Nitco Limited',
'ONGC': 'Oil & Natural Gas Corporation Limited',
'ORIENTBANK': 'Oriental Bank of Commerce',
'PAGEIND': 'Page Industries Limited',
'PCJEWELLER': 'PC Jeweller Limited',
'PERSISTENT': 'Persistent Systems Limited',
'PNB': 'Punjab National Bank',
'PNBHOUSING': 'PNB Housing Finance Limited',
'RAIN': 'Rain Industries Limited',
'RAYMOND': 'Raymond Limited',
'RBLBANK': 'RBL Bank Limited',
'RELCAPITAL': 'Reliance Capital Limited',
'RELIANCE': 'Reliance Industries Limited',
'RELIGARE': 'Religare Enterprises Limited',
'RELINFRA': 'Reliance Infrastructure Limited',
'ROLTA': 'Rolta India Limited',
'RPOWER': 'Reliance Power Limited',
'SBILIFE': 'SBI Life Insurance Company Limited',
'SBIN': 'State Bank of India',
'SCHAND': 'S Chand And Company Limited',
'SCHNEIDER': 'Schneider Electric Infrastructure Limited',
'SHANKARA': 'Shankara Building Products Limited',
'SHARDAMOTR': 'Sharda Motor Industries Limited',
'SIEMENS': 'Siemens Limited',
'SUNDARAM': 'Sundaram Multi Pap Limited',
'SUNDARMFIN': 'Sundaram Finance Limited',
'SUNDARMHLD': 'Sundaram Finance Holdings Limited',
'TATACHEM': 'Tata Chemicals Limited',
'TATACOFFEE': 'Tata Coffee Limited',
'TATACOMM': 'Tata Communications Limited',
'TATAELXSI': 'Tata Elxsi Limited',
'TATAGLOBAL': 'Tata Global Beverages Limited',
'TATAINVEST': 'Tata Investment Corporation Limited',
'TATAMETALI': 'Tata Metaliks Limited',
'TATAMOTORS': 'Tata Motors Limited',
'TATAMTRDVR': 'Tata Motors Limited',
'TATAPOWER': 'Tata Power Company Limited',
'TATASTEEL': 'Tata Steel Limited',
'TATASTLBSL': 'Tata Steel Bsl Limited',
'TATASTLLP': 'Tata Steel Long Products Limited',
'TBZ': 'Tribhovandas Bhimji Zaveri Limited',
'TCI': 'Transport Corporation of India Limited',
'TCS': 'Tata Consultancy Services Limited',
'TV18BRDCST': 'TV18 Broadcast Limited',
'TVSELECT': 'TVS Electronics Limited',
'TVSMOTOR': 'TVS Motor Company Limited',
'TVSSRICHAK': 'TVS Srichakra Limited',
'UPL': 'UPL Limited',
'VMART': 'V-Mart Retail Limited',
'VOLTAS': 'Voltas Limited',
'YESBANK': 'Yes Bank Limited',
'ZEEL': 'Zee Entertainment Enterprises Limited',
'ZEELEARN': 'Zee Learn Limited',
'ZEEMEDIA': 'Zee Media Corporation Limited'
}

def process():
    for stock in all_stocks1:
        print('process called')
        print(stock)
        if nse.is_valid_code(stock) and stock != 'SYMBOL':
            #print(stock)
            #time.sleep(1)
            stock_info = nse.get_quote(stock)
            buyQ = 0
            if stock_info['totalBuyQuantity']:
                buyQ = stock_info['totalBuyQuantity']
            sellQ = 0
            if stock_info['totalSellQuantity']:
                sellQ = stock_info['totalSellQuantity']
            #buyQ = tmp['totalBuyQuantity']
            #sellQ = tmp['totalSellQuantity']
            buyP = 0
            if (buyQ+sellQ):
                buyP = ((buyQ)/(buyQ+sellQ))*100
            val = (buyP-50)*2
            final_data[stock]=val
            print(final_data[stock])


def getFinalData():
    print('getFinalData called')
    process()
    return final_data

getFinalData()
#print(final_data)
#import argparse
#parser = argparse.ArgumentParser()
#args = parser.parse_args(q)
#print(args)
