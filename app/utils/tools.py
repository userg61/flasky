import sys
import os
from multiprocessing import current_process

from . import trace1
trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name)


from dotenv import load_dotenv
from flask import request as rq

dbg_user = "User for debug"

def field_value(index, name_field, records):
    index_requests_message = records['fields'][name_field]
    field = records['records'][index][index_requests_message]
    return field


def make_fields(join_req):
    ent = [entities.expr._label for entities in join_req._entities]
    fields = {join_req._entities[i].expr._label: i for i in range(len(join_req._entities))}
    return ent, fields

def make_full_telegram_name(telegram_member):
    full_name = " "
    if telegram_member.telegram_first_name is not None and len(telegram_member.telegram_first_name) > 0:
        full_name += f"{telegram_member.telegram_first_name} "
    if telegram_member.telegram_last_name is not None and len(telegram_member.telegram_last_name) > 0:
        full_name += f"{telegram_member.telegram_last_name} "
    if len(full_name) > 0:
        if telegram_member.telegram_username is not None and len(telegram_member.telegram_username) > 0:
            full_name += f" ({telegram_member.telegram_username})"
    else:
        full_name += f" ({telegram_member.telegram_username})"
    return full_name

if __name__ == '__main__':
    if True: print(f"@#$%| {__file__} {sys._getframe().f_lineno}\t{__name__}\tpid={os.getpid()}"
          f"\tparent pid={os.getppid()}\t{current_process().name} ")


def load_config(env_file_name):
    trace1(__file__, sys._getframe().f_lineno, __name__, os.getpid(), os.getppid(), current_process().name, f"sys: {sys.argv}")
    if "pytest" in sys.argv[0]:
        basedir = os.path.abspath(os.path.dirname(sys.argv[0]) + f"{os.sep}..{os.sep}..{os.sep}tests")
    else:
        basedir = os.path.abspath(os.path.dirname(sys.argv[0]))
    # print(f" {__file__} base dir: {basedir}")
    # print(f" app 2.0   file: {__file__} ")
    load_dotenv(os.path.join(basedir, env_file_name))
    return basedir


def is_remote_user():
    if rq.remote_user is None:
        #  tg.app.logger.info(f"remote_user - None")
        u = dbg_user
    else:
        #  tg.app.logger.info(f"{rq.remote_user} (ip: {rq.remote_addr})")
        u = rq.remote_user
    return u
