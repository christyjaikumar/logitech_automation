from datetime import datetime
import logging
import time
import getpass
import os

def get_logger(
        LOG_FORMAT     = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        LOG_NAME       = '',
        LOG_FILE_INFO  = 'file.log',
        LOG_FILE_ERROR = 'file.err',
        LOG_FILE_DEBUG = 'debug.log'):

    user_name = getpass.getuser()
    path = os.path.join("C:\\","Users",user_name, "PycharmProjects","logitech_automation")
    result = os.path.join(path, "results")
    ts_now = str(time.time())
    ts = str(ts_now).split('.')[0]
    rd_ts = datetime.fromtimestamp(float(ts_now)).strftime('%Y-%m-%d_%H-%M-%S')
    result_dir = os.path.join(result, 'LOGS_' + rd_ts)
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    result_dir = os.path.join(result, 'LOGS_' + rd_ts)
    debug_file = os.path.join(result_dir, "Debug_" + ts + ".log")
    info_log  = os.path.join(result_dir, "Info_" + ts + ".log")
    error_log = os.path.join(result_dir, "Error_" + ts + ".err")
    if LOG_FILE_INFO == 'file.log':
        LOG_FILE_INFO = info_log
    if LOG_FILE_ERROR == 'file.err':
        LOG_FILE_ERROR = error_log
    if LOG_FILE_DEBUG == 'debug.log':
        LOG_FILE_DEBUG = debug_file

    log           = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)

    # comment this to suppress console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    log.addHandler(stream_handler)

    file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='w')
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    log.addHandler(file_handler_info)

    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.ERROR)
    log.addHandler(file_handler_error)

    log.setLevel(logging.INFO)

    file_handler_debug = logging.FileHandler(LOG_FILE_DEBUG, mode='w')
    file_handler_debug.setFormatter(log_formatter)
    file_handler_debug.setLevel(logging.DEBUG)
    log.addHandler(file_handler_debug)

    log.setLevel(logging.INFO)

    return log