import imp
from multiprocessing.spawn import import_main_path
import threading
from app import app
import view


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
