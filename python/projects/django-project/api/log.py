import logging


logging.basicConfig(level=logging.DEBUG)


class MyLogger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)

        handler = logging.FileHandler(filename="error.log")
        formatter = logging.Formatter(
            fmt="%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        handler.setLevel(30)

        self.logger.addHandler(handler)

    def __call__(self) -> logging.Logger:
        return self.logger
