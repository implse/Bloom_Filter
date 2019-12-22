from Bloom_Filter import BloomFilter

bloom = BloomFilter()
passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon"]

for p in passwords:
    bloom.add(p)

print(bloom.check("dragon"))
print(bloom.check("sha"))
