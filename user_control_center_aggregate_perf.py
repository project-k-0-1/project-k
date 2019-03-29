# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors


db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_aggregate_perf():

    box_content = ''

    try:
        '''
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT "
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs:
            symbol = row[0]
        '''

        l_title_aggregate_perf = 'Your Performance'

        box_content = '' +\
        '            <div class="box-part rounded" style="height: 465px;">'+\
        '               <span class="sectiont"><i class="fas fa-chart-area"></i>&nbsp;'+ l_title_aggregate_perf +'</span>'+\
        '            </div>'

        '''
        cr.close()
        connection.close()
        '''

    except Exception as e: print(e)

    return box_content

def get_num_orders(t):
    r = 0
    try:

        query_condition = ''
        i = 0

        if t == 'open':
            query_condition = " "+\
            "trades.entry_date = @date_today AND instruments.owner = @portf_owner AND status = 'active' AND "+\
            "((portfolios.strategy_order_type = 'long' AND trades.order_type = 'buy') "+\
            "OR (portfolios.strategy_order_type = 'short' AND trades.order_type = 'sell') "+\
            "OR (portfolios.strategy_order_type = 'long/short') ) "
        if t == 'pending':
            query_condition = " "+\
            "trades.expiration_date <= @date_today AND instruments.owner = @portf_owner AND status = 'active' AND "+\
            "((portfolios.strategy_order_type = 'long' AND trades.order_type = 'buy') "+\
            "OR (portfolios.strategy_order_type = 'short' AND trades.order_type = 'sell') "+\
            "OR (portfolios.strategy_order_type = 'long/short') ) "
        if t == 'close':
            query_condition = " "+\
            "trades.expiration_date = @date_today AND instruments.owner = @portf_owner AND status = 'expired' AND "+\
            "((portfolios.strategy_order_type = 'long' AND trades.order_type = 'buy') "+\
            "OR (portfolios.strategy_order_type = 'short' AND trades.order_type = 'sell') "+\
            "OR (portfolios.strategy_order_type = 'long/short') )"

        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = ' '+\
        'SELECT '+\
        'trades.order_type, '+\
        'trades.fullname, '+\
        'trades.entry_date, '+\
        'trades.entry_price, '+\
        'trades.close_price, '+\
        'trades.expiration_date, '+\
        'trades.pnl_pct, '+\
        'trades.url, '+\
        'a_alloc.unit, '+\
        'trades.status, '+\
        'trades.uid '+\
        'FROM trades '+\
        'JOIN portfolios ON portfolios.symbol = trades.symbol '+\
        'JOIN instruments ON instruments.symbol = portfolios.portf_symbol '+\
        'JOIN instruments as a_alloc ON a_alloc.symbol = portfolios.symbol '+\
        'WHERE'+ query_condition
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs: i +=1
        r = i
        cr.close()
        connection.close()

    except Exception as e: print(e)
    return r

def get_control_center(burl):

    box_content = ''

    try:

        l_control_center_open_trade = 'You have {#} trade(s) to open today.'
        l_control_center_close_trade = 'You have to close {#} trade(s) at the best available price.'
        l_control_center_pending_trade = 'You have {#} trade(s) that you have to get ready to close at market open.'

        l_control_center_open_trade = l_control_center_open_trade.replace('{#}', str(get_num_orders('open')) )
        l_control_center_close_trade = l_control_center_close_trade.replace('{#}', str(get_num_orders('close')) )
        l_control_center_pending_trade = l_control_center_pending_trade.replace('{#}', str(get_num_orders('pending')) )

        control_center_content = ' '+\
        '<ul class="list-group">'+\
        '  <li class="list-group-item d-flex justify-content-between align-items-center">'+\
        l_control_center_open_trade +\
        '    <span class="badge badge-primary badge-pill">'+ str(get_num_orders('open')) +'</span>'+\
        '  </li>'+\
        '  <li class="list-group-item d-flex justify-content-between align-items-center">'+\
        l_control_center_close_trade +\
        '    <span class="badge badge-primary badge-pill">'+ str( get_num_orders('close') ) +'</span>'+\
        '  </li>'+\
        '  <li class="list-group-item d-flex justify-content-between align-items-center">'+\
        l_control_center_pending_trade +\
        '    <span class="badge badge-primary badge-pill">'+ str( get_num_orders('pending') ) +'</span>'+\
        '  </li>'+\
        '</ul>'

        l_title_control_center = 'Control Center'

        box_content = '' +\
        '            <div class="box-part rounded" style="height: 250px;">'+\
        '               <span class="sectiont"><i class="fas fa-tasks"></i>&nbsp;'+ l_title_control_center +'</span>'+\
        control_center_content+\
        '            </div>'

    except Exception as e: print(e)

    return box_content


def get_control_center_aggregate_perf(burl):
    r = ''
    try:
        r = '<div class="col-lg-6 col-md-12 col-sm-12 col-xs-12">'+\
        get_control_center(burl)+\
        get_aggregate_perf()+\
        '</div>'

    except Exception as e: print(e)
    return r
