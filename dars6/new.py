import time

class Logger:

    def log(self, message):
        self.prefix = time.localtime()
        print(f"{time.strftime('%Y-%B-%d %H-%M-%S',self.prefix)}")
    
logger = Logger()
logger.log("Hello world!")