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

def get_box_plan_selection(burl):

    box_content = ''

    try:

        l_button_trial = 'Get 1-month trial now<br />for only USD 5.00'
        l_title_join_now = 'Join Now! Thousands of beginners and professional traders that makes money with SmartAlpha. Don`t miss this unique opportunity.'

        box_content = '<div class="box-top">' +\
        '   <div class="row">'+\
        '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
        '            <div class="box-part rounded sa-center-content">'+\
        '<div>&nbsp;</div>'+\
        '<div>&nbsp;</div>'+\
        '<div style="text-align: center;"><h1>'+ l_title_join_now +'</h1></div>'+\
        '<div>&nbsp;</div>'+\
        '<button class="btn btn-lg btn-primary btn-block form-signin-btn" type="submit" style="font-size:x-large; font-weight:bolder;">'+ l_button_trial +'</button>'+\
        '<div>&nbsp;</div>'+\
        '<div>&nbsp;</div>'+\
        '<table class="table table-hover table-sm">'+\
        '  <thead>'+\
        '    <tr>'+\
        '      <th scope="col" style="vertical-align: top;">&nbsp;</th>'+\
        '      <th scope="col" style="vertical-align: top;"><h4>SmartAlpha Pro</h4></th>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <th scope="col" style="vertical-align: top;">Features</th>'+\
        '      <th scope="col" style="vertical-align: top;"><h2>*USD 28.00<sup>/month</sup></h2>*if paid annually</th>'+\
        '    </tr>'+\
        '  </thead>'+\
        '  <tbody>'+\
        '    <tr>'+\
        '      <td scope="row">User friendly dashboard with all your trading information.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Exclusive SmartAlpha portfolio pre-generated by artificial intelligence personalized for you.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Create unlimited number of portfolios.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Check out top traders and follow their trades.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Ability to monitor top trading signals.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Access to all trading signals with instant email notifications.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Backtest and simulate performance of portfolios.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
            '    <tr>'+\
            '      <td scope="row">Technical Analysis and chart patterns for all available assets.</td>'+\
            '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
            '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Clear entries and exits points defined.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Portfolio allocation automatically generated by algorithms for optimum performance.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Risk exposure and expected return of the asset/portfolio.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '    <tr>'+\
        '      <td scope="row">Transparent historical orders and performance.</td>'+\
        '      <td><h2 class="text-success"><i class="fas fa-check-circle"></i></h2></td>'+\
        '    </tr>'+\
        '  </tbody>'+\
        '</table>'+\
        '            </div>'+\
        '        </div>'+\
        '   </div>'+\
        '</div>'

    except Exception as e: print(e)

    return box_content


def get_plan_selection_page(appname,burl):
    r = ''
    try:
        r = get_head( get_loading_head() + get_googleanalytics() + get_title( appname ) + get_metatags(burl) + set_ogp(burl,1,'','') + get_bootstrap() + get_awesomplete() + get_tablesorter() + get_font_awesome() + get_stylesheet(burl) )
        r = r + get_body( get_loading_body(), navbar(burl) + get_box_plan_selection(burl) + get_page_footer(burl) )
        r = set_page(r)
    except Exception as e: print(e)

    return r
