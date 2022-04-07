import logging
import threading
import time


from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

def thread_function(name):
    print("Thread %s: starting" %(name))
    time.sleep(2)
    print("Thread %s: finishing" %(name))

@app.route('/')
def index():
   print('Request for index page received')
   return ""


@app.route('/api/', methods=['GET'])
def hello():

    threads = list()
    for index in range(10):
        print("Main    : create and start thread %d." %(index))
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print("Thread count : %d" %(threading.active_count()))
        print("Main    : before joining thread %d." %(index))
        thread.join()        
        print("Main    : thread %d done" %(index))
    
    return ""



if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    app.run()