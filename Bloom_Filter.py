import hashlib

class BloomFilter:
    def __init__(self, n=1000, k=3):
        self.array = [False for _ in range(n)]
        self.hash_algorithms = [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha384, hashlib.sha512]
        self.hashes = [self._get_hash(f) for f in self.hash_algorithms[:k]]

    def _get_hash(self, f):
        def hash_function(value):
            h = f(str(value).encode('utf-8')).hexdigest()
            return int(h, 16) % len(self.array)
        return hash_function

    def add(self, value):
        for f in self.hashes:
            v = h(value)
            self.array[v] = True

    def check(self, value):
        for h in self.hashes:
            v == h(value)
            if not self.array[v]:
                return False
        return True

# Test
bloom = BloomFilter()
passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon"]
for p in passwords:
    bloom.add(p)

bloom.check("dragon")
