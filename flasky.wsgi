import os
import sys
from multiprocessing import current_process

def trace1(file, lineno, name, pid, ppid, pr_name, dop=""):
    print(f"\t\t\t@#$%| {file} {lineno}\t{name}\tpid={pid} \tparent pid={ppid}\t{pr_name} | {dop}")
    ...


trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name)
sys.path.insert(0, '/var/www/html/flasky')
os.chdir("/var/www/html/flasky")

trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name)
from app import create_app
trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name)
#import nitiservices
#trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name, "after import flasky")
application= create_app(config_name="production")
trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name)
