# test_functioncalling.py
"""
Tests for FunctionCalling module.
"""

import unittest
from functioncalling import FunctionCalling

class TestFunctionCalling(unittest.TestCase):
    """Test cases for FunctionCalling class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FunctionCalling()
        self.assertIsInstance(instance, FunctionCalling)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FunctionCalling()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
