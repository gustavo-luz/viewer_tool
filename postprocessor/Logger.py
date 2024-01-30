from pathlib import Path
from datetime import datetime

class Logger:
    @staticmethod
    def log_error(path, msg):
        log_file = 'err.log'

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        msg = f"{current_time} {msg}"
        print(msg)

        file_object = open(path + log_file, 'a+')
        file_object.write("LOG: " + msg + "\n")
        file_object.close()

    @staticmethod
    def log(msg):
        path = Path(__file__).parent.resolve()
        log_file = str(path) + '/log_post.out'

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        msg = f"{current_time} {msg}"
        print(msg)

        file_object = open(log_file, 'a+')
        file_object.write(msg + "\n")
        file_object.close()