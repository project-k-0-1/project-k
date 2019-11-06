
from sa_func import get_random_num

def set_ogp(burl,type,title,desc):
    if int(type) == 1:
        return_data = '' +\
        '<meta property="og:title" content="A.I. Powered Trading Insights">'+\
        '<meta property="og:site_name" content="SmartAlpha Trade">'+\
        '<meta property="og:url" content="http://smartalphatrade.com">'+\
        '<meta property="og:description" content="SmartAlpha will help you to turn any trading portfolio into a profitable one.">'+\
        '<meta property="og:type" content="article">'+\
        '<meta property="og:image" content="'+ burl +'static/ogp.png?'+ str(get_random_num(9) ) +'">'

    if int(type) == 2:
        return_data = '' +\
        '<meta property="og:title" content="'+ title +'">'+\
        '<meta property="og:site_name" content="SmartAlpha Trade">'+\
        '<meta property="og:url" content="http://smartalphatrade.com">'+\
        '<meta property="og:description" content="'+ desc +'">'+\
        '<meta property="og:type" content="article">'+\
        '<meta property="og:image" content="'+ burl +'static/ogp.png?'+ str(get_random_num(9) ) +'">'
    return return_data
