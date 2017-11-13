# Config
# 前端节点管理增加一个节点，增加的节点ID为多少就修改为多少
NODE_ID = 1


# hour,set 0 to disable
SPEEDTEST = 6
CLOUDSAFE = 1
ANTISSATTACK = 0
AUTOEXEC = 0

MU_SUFFIX = 'zhaoj.in'
MU_REGEX = '%5m%id.%suffix'

SERVER_PUB_ADDR = '127.0.0.1'  # mujson_mgr need this to generate ssr link
API_INTERFACE = 'glzjinmod'  # glzjinmod, modwebapi  --默认为modwebapi 需要修改为glzjinmod

WEBAPI_URL = 'https://zhaoj.in' # 自己网站的域名
WEBAPI_TOKEN = 'glzjin'

# mudb
MUDB_FILE = 'mudb.json'

# Mysql
# 前端服务器所用的数据库配置
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'ss'
MYSQL_PASS = 'ss'
MYSQL_DB = 'shadowsocks'

MYSQL_SSL_ENABLE = 0
MYSQL_SSL_CA = ''
MYSQL_SSL_CERT = ''
MYSQL_SSL_KEY = ''

# API
# 填写服务器域名
API_HOST = '127.0.0.1'
API_PORT = 80
API_PATH = '/mu/v2/'
# 填写前端配置对应的TOKEN
API_TOKEN = 'abcdef'
API_UPDATE_TIME = 60

# Manager (ignore this)
MANAGE_PASS = 'ss233333333'
# if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
# make sure this port is idle
MANAGE_PORT = 23333
