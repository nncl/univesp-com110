import unittest

def is_prime(number: int) -> bool:
    i = 2

    while i < number:
        if number % i == 0:
            break
        i += 1

    return i == number

# For academic purposes, in real life we would just print if it's prime
#   instead (for better reading for god's sake).
for number in range(2, 100):
    if not is_prime(number):
        continue
    print(number)

class TestPrimeFunction(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_large_prime(self):
        self.assertTrue(is_prime(7919))

    def test_large_non_prime(self):
        self.assertFalse(is_prime(8000))

if __name__ == "__main__":
    unittest.main()
