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
    ram_total = __parse_bytes_to_gibibyte(__get_ram().total)
    print('Ram total: ' + str(ram_total) + ' GiB')
    return ram_total


def get_ram_usage():
    ram_usage = __parse_bytes_to_gibibyte(__get_ram().used)
    print('Ram usage: ' + str(ram_usage) + ' GiB')
    return ram_usage


def get_disk_percent():
    disk_percent = __get_disk().percent
    print('Disk percent: ' + str(disk_percent) + ' %')
    return disk_percent


def get_disk_total():
    disk_total = __parse_bytes_to_gigabyte(__get_disk().total)
    print('Disk total: ' + str(disk_total) + ' GB')
    return disk_total


def get_disk_usage():
    disk_usage = __parse_bytes_to_gigabyte(__get_disk().used)
    print('Disk usage: ' + str(disk_usage) + ' GB')
    return disk_usage


def __get_ram():
    return psutil.virtual_memory()


def __get_disk():
    return psutil.disk_usage('/')


def __parse_bytes_to_gibibyte(bytes_value):
    return bytes_value / (1024 * 1024 * 1024)


def __parse_bytes_to_gigabyte(bytes_value):
    return bytes_value / (1000 * 1000 * 1000)
