from Bloom_Filter import BloomFilter

# Instantiate Bloom Filter
bloom = BloomFilter()

# List of passwords
passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon"]

# Add each password to the Bloom Filter
for p in passwords:
    bloom.add(p)

# Check
print(bloom.check("dragon"))
print(bloom.check("sha"))
