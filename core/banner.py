
from  core.colors import yellow,green
from core import VERSION
from core.cmdline import args
from core.log import logger
logger=logger()
def banner():
    _ = r'''
     ___   wW  Ww()_()  _        By Ethan~
    (___)__(O)(O)(O o) /||_   
    (O)(O)  (..)  |^_\  /o_)     
    /  _\    ||   |(_))/ |(\  
    | |_))  _||_  |  / | | )) 
    | |_)) (_/\_) )|\\ | |//  
    (.'-'        (/  \)\__/      Version:{version}        

'''

    print(yellow+ _.format(version=VERSION,))


def _init_stdout():
    banner()
    # threads
    if args.threads:
        logger.INFO("Staring {0} threads".format(args.threads))

