import datetime
import os
import pandas as pd

__PATH = 'monitoring'


def save_data_logs_in_file(date: datetime, message: str):
    full_path = __get_full_path(date.strftime('%Y-%m-%d'), '.txt')

    # Create directory if it does not exist
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, 'a') as file:
        file.write(message + '\n')


def save_data_in_excel(date: datetime, cpu_percent: str = None, ram_percent: str = None, disk_percent: str = None):
    full_path = __get_full_path(date.strftime('%Y-%m-%d'), '.xlsx')

    df = __get_excel_or_create_if_not_exist(full_path)
    # Create data
    row_data = {'timestamp': date, 'cpu_usage': cpu_percent, 'ram_usage': ram_percent, 'disk_usage': disk_percent}
    # Append data
    df = pd.concat([df, pd.DataFrame([row_data])], ignore_index=True)

    df.to_excel(full_path, index=False)


def __get_excel_or_create_if_not_exist(full_path):
    if os.path.isfile(full_path):
        return pd.read_excel(full_path)

    return pd.DataFrame()

def __get_full_path(date: str, format: str):
    file_name = 'data_monitoring_from_' + date + format
    return os.path.join(__get_root_dir(), __PATH, date, file_name)


def __get_root_dir():
    return os.path.expanduser('~')
