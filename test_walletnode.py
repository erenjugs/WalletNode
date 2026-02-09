# test_walletnode.py
"""
Tests for WalletNode module.
"""

import unittest
from walletnode import WalletNode

class TestWalletNode(unittest.TestCase):
    """Test cases for WalletNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WalletNode()
        self.assertIsInstance(instance, WalletNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WalletNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
