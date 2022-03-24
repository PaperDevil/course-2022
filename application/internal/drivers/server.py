from fastapi import FastAPI


class FastAPIServer:

    @staticmethod
    def get_app() -> FastAPI:
        app = FastAPI(debug=True)

        return app
