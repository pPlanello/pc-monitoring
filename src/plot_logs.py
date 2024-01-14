from datetime import datetime

from src.file_service import save_data_logs_in_file
from src.monitoring.RAM import RAM
from src.monitoring.Disk import Disk


def save_logs_stats_in_file(date=datetime.now(), cpu=None, ram: RAM = None, disk: Disk = None):
    dateFormat = __format_date(date)
    monitoring_data_message = __print_logs_data(dateFormat, cpu, ram_percent=ram.percent, disk_percent=disk.percent)

    save_data_logs_in_file(date, monitoring_data_message)
    return


def __print_logs_data(dateFormat: str, cpu_percent: str = None, ram_percent: str = None, disk_percent: str = None):
    return '[{}] - CPU usage: {} %  RAM usage: {} %  DISK usage: {} %'.format(dateFormat, cpu_percent, ram_percent, disk_percent)


def __format_date(date: datetime):
    return date.strftime('%Y-%m-%d %H:%M:%S')
