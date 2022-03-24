import uvicorn
from application.internal.drivers.server import FastAPIServer

app = FastAPIServer.get_app()

if __name__ == '__main__':
    uvicorn.run("manage:app")
