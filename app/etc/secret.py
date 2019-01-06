"""
敏感配置内容
"""
# DATABASE
DB_TYPE     =''
DB_DRIVER   =''
DB_USER     =''
DB_PASSD    =''
DB_HOST     =''
DB_PORT     =''
DB_DATABASE =''
DB_URI      ='{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DB_TYPE,DB_DRIVER,DB_USER,DB_PASSD,DB_HOST,DB_PORT,DB_DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI