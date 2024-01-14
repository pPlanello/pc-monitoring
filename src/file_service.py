import datetime
import os

__PATH = 'monitoring'


def save_data_logs_in_file(date: datetime, message: str):
    date_day = date.strftime('%Y-%m-%d')
    full_path = __get_full_path(date_day)

    # Create directory if it does not exist
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, 'a') as file:
        file.write(message + '\n')


def __get_full_path(date: str):
    file_name = 'data_monitoring_from_' + date + '.txt'
    return os.path.join(__get_root_dir(), __PATH, date, file_name)


def __get_root_dir():
    return os.path.expanduser('~')
