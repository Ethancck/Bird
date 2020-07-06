from core.colors import green,red,yellow
import time
import sys
import threading
class logger():
    def __init__(self):
        self.lock = threading.Lock()

    def INFO(self,msg):
        self.lock.acquire()
        sys.stdout.write(green + '[+] ' + time.strftime('%H:%M:%S', time.localtime()) +' [INFO] '+ msg + '\n')
        self.lock.release()
    def ERROR(self,msg):
        self.lock.acquire()
        sys.stdout.write(red + '[!] ' + time.strftime('%H:%M:%S', time.localtime()) +' [ERROR] '+ msg + '\n')
        self.lock.release()
    def WARNING(self,msg):
        self.lock.acquire()
        sys.stdout.write(yellow + '[!] ' + time.strftime('%H:%M:%S', time.localtime()) + ' [WARN] '+ msg + '\n')
        self.lock.release()
    
if __name__ == '__main__':
    logger = logger()
    str = "insert [1] row"
    logger.ERROR(str)
    logger.INFO(str)
    logger.WARNING(str)