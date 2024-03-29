import unittest
import hashlib
from blockchain import Block

class TestBlock(unittest.TestCase):
    def test_calculate_hash(self):
        # Create a block with some data
        block = Block(1, '2022-01-01 00:00:00', 'Hello, world!', '0')

        # Calculate the expected hash manually
        expected_hash = hashlib.sha256()
        expected_hash.update(str(block.index).encode('utf-8') +
                             str(block.timestamp).encode('utf-8') +
                             str(block.data).encode('utf-8') +
                             str(block.previous_hash).encode('utf-8'))
        expected_hash = expected_hash.hexdigest()

        # Check if the calculated hash matches the expected hash
        self.assertEqual(block.hash, expected_hash)

if __name__ == '__main__':
    unittest.main()