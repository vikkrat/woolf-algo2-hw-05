from bloom_filter import BloomFilter, check_password_uniqueness

if __name__ == "__main__":
    bloom = BloomFilter(size=1000, num_hashes=3)

    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    new_passwords = ["password123", "newpassword", "admin123", "guest", "", None]
    results = check_password_uniqueness(bloom, new_passwords)

    for pwd, status in results.items():
        print(f"Пароль '{pwd}' — {status}.")
