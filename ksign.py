# Copyright (c) 2018-present, Project K
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from page import *
from head import *
from metatags import *
from title import *
from body import *
from bootstrap import *
from google_chart import *
from kloading import *
from kstylesheet import *
from awesomplete import *
from knavbar import *
from kdetails_header import *
from ksign_header import *
from ksign_ta_chart import *
from ksign_recommend import *

from kdb import *
access_obj = sa_db_access()
import pymysql.cursors


db_usr = access_obj.username()
db_pwd = access_obj.password()
db_name = access_obj.db_name()
db_srv = access_obj.db_server()

connection = pymysql.connect(host=db_srv,
                             user=db_usr,
                             password=db_pwd,
                             db=db_name,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def gen_sign_page(uid):

    cr = connection.cursor(pymysql.cursors.SSCursor)
    sql = "SELECT instruments.fullname FROM `symbol_list` JOIN instruments ON symbol_list.symbol = instruments.symbol "+\
        "WHERE symbol_list.uid = " + str(uid)

    cr.execute(sql)
    rs = cr.fetchall()
    for row in rs:
        instfullname = row[0]

    r = get_head(  get_loading_head() + get_title('Kahroo - Market intelligence - ' + instfullname ) + get_metatags() + get_bootstrap() + get_awesomplete() + get_google_chart_script() + get_stylesheet() )
    r = r + get_body( get_loading_body(), navbar() + '<div class="box"><div class="row">' + get_details_header(uid) + get_sign_header(uid) + get_sign_ta_chart(uid) + get_sign_recommend() + '</div></div>')
    r = set_page(r)

    return r
