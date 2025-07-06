import time
from ip_counter import load_ip_addresses, count_unique_ips_exact, count_unique_ips_hll
from tabulate import tabulate

if __name__ == "__main__":
    file_path = "lms-stage-access.log"
    ip_list = load_ip_addresses(file_path)

    # Точний підрахунок
    start_exact = time.perf_counter()
    exact_count = count_unique_ips_exact(ip_list)
    time_exact = (time.perf_counter() - start_exact) * 1000  # мілісекунди

    # HyperLogLog
    start_hll = time.perf_counter()
    hll_count = count_unique_ips_hll(ip_list)
    time_hll = (time.perf_counter() - start_hll) * 1000  # мілісекунди

    # Формування таблиці
    headers = ["", "Точний підрахунок", "HyperLogLog"]
    table = [
        ["Унікальні елементи", f"{exact_count:.1f}", f"{hll_count:.1f}"],
        ["Час виконання (мс)", f"{time_exact:.2f}", f"{time_hll:.2f}"],
    ]

    print("Результати порівняння:")
    print(tabulate(table, headers=headers, tablefmt="github"))
