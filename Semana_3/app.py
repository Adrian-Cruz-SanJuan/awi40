from web.template import ALLOWED_AST_NODES
ALLOWED_AST_NODES.append('Constant')
import web

urls = (
    '/(.*)', 'application.controllers.main.Main'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()