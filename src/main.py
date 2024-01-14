from plot_logs import save_logs_stats_in_file
from src.monitoring.monitoring_service import obtain_cpu_data, obtain_disk_data, obtain_ram_data

if __name__ == '__main__':
    save_logs_stats_in_file(cpu=obtain_cpu_data(), ram=obtain_ram_data(), disk=obtain_disk_data())
