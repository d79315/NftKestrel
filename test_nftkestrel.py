# test_nftkestrel.py
"""
Tests for NftKestrel module.
"""

import unittest
from nftkestrel import NftKestrel

class TestNftKestrel(unittest.TestCase):
    """Test cases for NftKestrel class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftKestrel()
        self.assertIsInstance(instance, NftKestrel)

    def test_run_method(self):
        """Test the run method."""
        instance = NftKestrel()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
