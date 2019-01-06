'''
定义红图类
'''

class RedPrint():
    def __init__(self,name):
        self.name = name
        self.mount = []

    def route(self,rule,**options):
        def decorator(f):
            self.mount.append((f,rule,options))
            return f
        return decorator

    def register(self,blueprint,url_prefix=None):
        # 注册时不加url_prefix参数，则取红图名
        if not url_prefix:
            url_prefix = '/'+self.name  # ‘/’可以不加，见blueprints.py68~70 有rule的话，会自动加‘/’
        for f,rule,options in self.mount:
            endpoint = options.pop("endpoint", f.__name__)
            blueprint.add_url_rule(url_prefix+rule, endpoint, f, **options)