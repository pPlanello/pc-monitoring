import psutil


def get_cpu():
    cpu_percent = psutil.cpu_percent(interval=0.1)
    print('CPU percent: ' + str(cpu_percent) + ' %')
    return cpu_percent


def get_ram_percent():
    ram_percent = __get_ram().percent
    print('Ram percent: ' + str(ram_percent) + ' %')
    return ram_percent


def get_ram_total():
    print(__get_ram())
    ram_total = __parse_bytes_to_gigabyte(__get_ram().total)
    print('Ram total: ' + str(ram_total) + ' GB')
    return ram_total


def get_disk_percent():
    disk_percent = __get_disk().percent
    print('Disk percent: ' + str(disk_percent) + ' %')
    return disk_percent


def get_disk_total():
    disk_total = __parse_bytes_to_gigabyte(__get_disk().total)
    print('Disk total: ' + str(disk_total) + ' GB')
    return disk_total


def __get_ram():
    return psutil.virtual_memory()


def __get_disk():
    return psutil.disk_usage('/')


def __parse_bytes_to_gigabyte(bytes_value):
    return bytes_value / (1000 * 1000 * 1000)
