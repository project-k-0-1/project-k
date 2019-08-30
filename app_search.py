# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from app_head import *; from app_body import *; from app_page import *; from app_loading import *
from app_footer import *
from app_ogp import *
from app_title import *; from app_metatags import *; from bootstrap import *
from awesomplete import *; from font_awesome import *; from app_navbar import *
from googleanalytics import *; from tablesorter import *
from app_stylesheet import *
from sa_db import *
from sa_func import *
from app_cookie import *
access_obj = sa_db_access()
import pymysql.cursors


db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_search_table_content(burl):
    r = ''
    try:
        r = ' '+\
        '<script>$(document).ready(function($) {'+\
        '$(".sa-table-click-row").click(function() {'+\
        'window.document.location = $(this).data("href");'+\
        '});'+\
        '});</script>'

        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = 'SELECT feed.search, feed.content, markets.market_label, feed.url FROM feed LEFT JOIN markets ON markets.market_id = feed.market WHERE feed.type<>9 ORDER BY feed.search'
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs:
            search_text = row[0]
            content_details = row[1]
            scope_text = row[2]
            url = row[3].replace('{burl}',burl)
            r = r +\
            '<tr class="sa-table-click-row" data-href="'+ str(url) +'">'+\
            '    <td style="text-align: left" scope="row"><strong>'+ str(search_text) +'</strong></td>'+\
            '    <td style="text-align: left">'+ str(content_details) +'</td>'+\
            '    <td style="text-align: left">'+ str(scope_text) +'</td>'+\
            '</tr>'
        cr.close()
        connection.close()

    except Exception as e: print(e)
    return r

def gen_search_table(burl):

    r = ''
    try:
        r =  ' ' +\
        '<table id="table_search" class="table table-hover table-sm">'+\
        '  <thead>'+\
        '    <tr>'+\
        '       <th scope="col" style="text-align: left">Instruments / Functions</th>'+\
        '       <th scope="col" style="text-align: left"></th>'+\
        '       <th scope="col" style="text-align: left"></th>'+\
        '    </tr>'+\
        ' </thead>'+\
        '  <tbody>'+\
        get_search_table_content(burl) +\
        '  </tbody>'+\
        '</table>'

    except Exception as e:
        print(e)
    return r

def get_box_search(burl):

    box_content = ''

    try:
        col_id = 0
        sid = get_random_str(9)
        l_placeholder = "Enter function, ticker or search. Hit <enter> to go."
        list_class = 'sa-center-content sa-list-select-100pct sa-instr-n-portf-list'
        search_box = ' '+\
        '  <form class="" action="'+ burl +'" method="get" >'+\
        '       <div class="input-group input-group-lg">'+\
        '       <div class="input-group-prepend"><span class="input-group-text" id="inputGroup-sizing-lg"><i class="fas fa-search" style="font-size: xx-large;"></i></span></div><input type="text" id="filterInput" name="'+ str(sid) +'" onkeyup="filterTable()" class="form-control" aria-label="Large" aria-describedby="inputGroup-sizing-sm" placeholder="'+ l_placeholder +'" autofocus></div><div>&nbsp;'+\
        '       </div>'+\
        '     <input type="hidden" name="sid" value="'+ str(sid) +'">'+\
        '  </form>'

        box_content = '' +\
        '<script>'+\
        'function filterTable() {'+\
        '  var input, filter, table, tr, td, i, txtValue;'+\
        '  input = document.getElementById("filterInput");'+\
        '  filter = input.value.toUpperCase();'+\
        '  table = document.getElementById("table_search");'+\
        '  tr = table.getElementsByTagName("tr");'+\
        '  for (i = 0; i < tr.length; i++) {'+\
        '    td = tr[i].getElementsByTagName("td")['+ str(col_id) +'];'+\
        '    if (td) {'+\
        '      txtValue = td.textContent || td.innerText;'+\
        '      if (txtValue.toUpperCase().indexOf(filter) > -1) {'+\
        '        tr[i].style.display = "";'+\
        '      } else {'+\
        '        tr[i].style.display = "none";'+\
        '      }'+\
        '    }'+\
        '  }'+\
        '}'+\
        '</script>'

        box_content = box_content +\
        search_box +\
        gen_search_table(burl)

    except Exception as e: print(e)
    return box_content


def get_search_page_content(burl):
    box_content = ''
    try:

        box_content = ' '+\
        '<div class="box-top">' +\
        '   <div class="row">'+\
        '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
        '            <div class="box-part rounded sa-center-content" style="'+ theme_return_this('','border-style:solid; border-width:thin; border-color:#343a40;') +'">'+\
        get_box_search(burl) +\
        '            </div>'+\
        '        </div>'+\
        '   </div>'+\
        '</div>'

    except Exception as e: print(e)
    return box_content

def get_search_page(appname,burl):
    r = ''
    try:
        r = get_head( get_loading_head() + get_googleanalytics() + get_title( appname ) + get_metatags(burl) + set_ogp(burl,1,'','') + get_bootstrap( get_sa_theme(),burl ) + get_awesomplete() + get_tablesorter() + get_font_awesome() + get_stylesheet(burl) )
        r = r + get_body( get_loading_body(), navbar(burl,1) + get_search_page_content(burl) + get_page_footer(burl) )
        r = set_page(r)
    except Exception as e: print(e)

    return r
