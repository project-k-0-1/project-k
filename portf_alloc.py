# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors

db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()


def get_portf_alloc(uid):

    signal_box = ''; pie_chart = ''

    try:

        signal_box = '' +\
        '        <div class="col-lg-8 col-md-8 col-sm-6 col-xs-12">'+\
        '            <div class="box-part">'+\
        '               <table class="table table-hover table-sm sa-table-sm">'+\
        '                   <thead>'+\
        '                       <tr>'+\
        '                          <th scope="col">Order</th>'+\
        '                          <th scope="col">Quantity</th>'+\
        '                          <th scope="col">Ticker</th>'+\
        '                          <th scope="col">Entry @</th>'+\
        '                          <th scope="col">Expires on</th>'+\
        '                       </tr>'+\
        '                   </thead>'+\
        '                   <tbody>'

        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT portfolios.order_type, portfolios.quantity, portfolios.symbol, portfolios.entry_level, portfolios.expiration, "+\
        "symbol_list.uid FROM portfolios JOIN symbol_list ON portfolios.portf_symbol = symbol_list.symbol "+\
        "WHERE symbol_list.uid=" + str(uid) + " ORDER BY portfolios.symbol"

        print(sql)

        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs:
            order_type = row[0]
            quantity = row[1]
            symbol = row[2]
            entry_price = row[3]
            trade_expiration = row[4]

            if order_type == 'buy':
                badge = 'badge-success'
            else:
                badge = 'badge-danger'

            signal_box = signal_box + '' +\
            '                       <tr>'+\
            '                          <th scope="row"><span class="badge '+ badge +'">'+ order_type +'</span></th>'+\
            '                          <td>'+ str(quantity)  +'</td>'+\
            '                          <td>'+ symbol +'</td>'+\
            '                          <td>'+ str(entry_price) +'</td>'+\
            '                          <td>'+ str(trade_expiration) +'</td>'+\
            '                       </tr>'
        signal_box = signal_box + '' +\
        '                   </tbody>'+\
        '               </table>'+\
        '            </div>'+\
        '        </div>'
        cr.close()
        connection.close()

        pie_chart_title = 'Portfolio Allocation'
        pie_chart = '' +\
        '        <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12">'+\
        '            <div class="box-part">'+\
        '    <script type="text/javascript">'+\
        '      google.charts.load("current", {packages:["corechart"]});'+\
        '      google.charts.setOnLoadCallback(drawChart);'+\
        '      function drawChart() {'+\
        '        var data = google.visualization.arrayToDataTable(['+\
        '          ["Language", "Speakers (in millions)"],'+\
        '          ["Assamese", 13], ["Bengali", 83], ["Bodo", 1.4],'+\
        '        ]);'+\
        '        var options = {'+\
        '          title: "'+ pie_chart_title +'",'+\
        '          pieHole: 0.4,'+\
        '          legend: "none",'+\
        '          pieSliceText: "label",'+\
        '          slices: {  2: {offset: 0.2},'+\
        '          },'+\
        '        };'+\
        '        var chart = new google.visualization.PieChart(document.getElementById("piechart"));'+\
        '        chart.draw(data, options);'+\
        '      }'+\
        '    </script>'+\
        '            </div>'+\
        '        </div>'


    except Exception as e: print(e)


    return signal_box + pie_chart
