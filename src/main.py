from monitoring_pc import get_ram_total, get_ram_percent, get_ram_usage, get_cpu, get_disk_percent, get_disk_total, \
    get_disk_usage


def print_hi():
    get_ram_percent()
    get_ram_total()
    get_ram_usage()
    get_cpu()
    get_disk_percent()
    get_disk_total()
    get_disk_usage()


if __name__ == '__main__':
    print_hi()
