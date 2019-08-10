# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors

db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_tradingview_symbol_info(suid):
    r = ''
    url = 'http://smartalphatrade.com/s/'
    try:
        symbol = ''
        referral_id = 'smartalpha'
        label_not_available = 'Indicators are not available for this instrument'
        theme = 'light'

        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT tradingview FROM symbol_list WHERE uid ='"+ str(suid) +"'"
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs: symbol = row[0]

        if symbol != '':
            r = '' +\
'<div class="tradingview-widget-container">]'+\
'  <div class="tradingview-widget-container__widget"></div>'+\
'  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-symbol-info.js" async>'+\
'  {'+\
'  "symbol": "'+ symbol +'",'+\
'  "width": "100%",'+\
'  "locale": "en",'+\
'  "colorTheme": "'+ theme +'",'+\
'  "isTransparent": true'+\
'}'+\
'</div>'+\
'  </script>'
        else:
            r = label_not_available

    except Exception as e: print(e)
    return r
