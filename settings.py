# -*- coding: utf-8 -*-
import sys

TIMEZONE = 'Asia/Shanghai'

DATE_FORMATS = {
    'en' : u'%a, %d %b %Y',
    'zh' : u'%Y-%m-%d',
    'zhs': u'%Y-%m-%d',
}
# windows locale: http://msdn.microsoft.com/en-us/library/cdax410z%28VS.71%29.aspx
#~ LOCALE = ['usa', 'cht', 'chs', 'jpn',        # windows
          #~ 'en_US', 'zh_CN', 'ja_JP']  # Unix/Linux
DEFAULT_LANG = 'zhs'

SITENAME = "X. Wei's Blog"
AUTHOR = 'X.Wei'

DISQUS_SITENAME = 'xwsblog'
GITHUB_URL = 'https://github.com/X-Wei'
SITEURL = 'http://x-wei.github.com'
#~ GOOGLE_ANALYTICS = 'UA-29540705-1'
TAG_FEED  = 'feeds/%s.atom.xml'


SOCIAL = (
          ('github', 'https://github.com/x-wei'),
          )
          #('twitter', 'http://twitter.com/farseerfc'),
          #~ ('facebook', 'http://www.facebook.com/farseerfc'),
          #~ ('weibo', 'http://weibo.com/farseerfc'),
          #~ ('renren', 'http://www.renren.com/farseer'),
          
          

#~ TWITTER_USERNAME = 'farseerfc'
#~ SIDEBAR_CUSTOM = r"""
#~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
#~ src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1">
#~ </iframe>
#~ """

#~ GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
#~ GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"

#THEME='bootstrap2'
THEME='notmyidea'
#CSS_FILE = "wide.css"

DEFAULT_CATEGORY ='MISC'
OUTPUT_PATH = '.'
PATH = 'posts'

#PDF_GENERATOR = True
