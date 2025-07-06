import json
import hyperloglog


def load_ip_addresses(filepath: str) -> list[str]:
    ips = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            try:
                log_entry = json.loads(line)
                ip = log_entry.get("remote_addr")
                if ip:
                    ips.append(ip)
            except json.JSONDecodeError:
                continue  # пропустити некоректний JSON
    return ips


def count_unique_ips_exact(ips: list[str]) -> int:
    return len(set(ips))


def count_unique_ips_hll(ips: list[str]) -> float:
    hll = hyperloglog.HyperLogLog(0.01)
    for ip in ips:
        hll.add(ip)
    return len(hll)
