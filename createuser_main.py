# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from app_page import *
from app_head import *
from app_metatags import *
from app_title import *
from app_body import *
from bootstrap import *
from app_loading import *
from app_stylesheet import *
from awesomplete import *
from app_navbar import *
from font_awesome import *
from createuser_form import *
import pymysql.cursors
from sa_db import *
access_obj = sa_db_access()
db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def gen_createuser_page(uid,appname,burl):
    r = ''
    if uid == '0':
        r = get_head( get_loading_head() + get_title( appname ) + get_metatags(burl) + get_bootstrap() + get_awesomplete() + get_font_awesome() + get_stylesheet(burl) )
        r = r + get_body( get_loading_body(), navbar(burl) + get_user_creation_form(burl) )
        r = set_page(r)
    else:
        connection = pymysql.connect(host=db_srv, user=db_usr, password=db_pwd, db=db_name, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT username FROM users WHERE uid = '"+ str(uid) +"' "
        cr.execute(sql)
        rs = cr.fetchall()
        username = ''
        for row in rs: username = row[0]
        if not username == '':
            r = 'No user found'
        else:
            r = 'user exists'

    return r
