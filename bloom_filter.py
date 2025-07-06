import hashlib
import bitarray


class BloomFilter:
    def __init__(self, size: int, num_hashes: int):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray.bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item: str):
        for i in range(self.num_hashes):
            hash_value = int(hashlib.sha256(f"{item}_{i}".encode()).hexdigest(), 16)
            yield hash_value % self.size

    def add(self, item: str):
        for hash_index in self._hashes(item):
            self.bit_array[hash_index] = 1

    def __contains__(self, item: str) -> bool:
        return all(self.bit_array[hash_index] for hash_index in self._hashes(item))


def check_password_uniqueness(bloom_filter: BloomFilter, passwords: list[str]) -> dict[str, str]:
    results = {}
    for pwd in passwords:
        if not isinstance(pwd, str) or not pwd:
            results[str(pwd)] = "некоректний пароль"
            continue

        if pwd in bloom_filter:
            results[pwd] = "вже використаний"
        else:
            results[pwd] = "унікальний"
            bloom_filter.add(pwd)
    return results
