from src.monitoring.monitoring_pc_utils import get_cpu, get_ram_total, get_ram_usage, get_ram_percent, get_disk_total, \
    get_disk_usage, get_disk_percent
from src.monitoring.RAM import RAM
from src.monitoring.Disk import Disk


def obtain_cpu_data():
    return get_cpu()


def obtain_ram_data():
    return RAM(get_ram_total(), get_ram_usage(), get_ram_percent())


def obtain_disk_data():
    return Disk(get_disk_total(), get_disk_usage(), get_disk_percent())
