
import tornado.web
import tornado.ioloop
import dbUtil

class IndexHandler(tornado.web.RequestHandler):

    async def get(self):
        db = self.settings['db']
        arguments = self.get_arguments('name')
        #默认
        menu_name = "user"
        entity = {}
        if len(arguments) > 0:
            menu_name = self.get_arguments('name')[0]

        sub_menu = ""
        if menu_name == 'user':
            sub_menu = "用户管理"
            entitys = dbUtil.findUserList(db)

        elif menu_name == 'car':
            sub_menu = "车流量管理"
            entitys = dbUtil.findCarList(db)

        elif menu_name == 'rule':
            sub_menu = "知识管理"

        #默认
        else:
            sub_menu = "用户管理"

        self.render("index.html",sub_menu=sub_menu,menu_name=menu_name,entitys=entitys)

default_handlers = [
    (r"/", IndexHandler),
]
