from src.server.instance import server

from src.controllers.recomendacoesRoutes import *

server.run()

#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 5000))
#    app.run(host='0.0.0.0', port = port)