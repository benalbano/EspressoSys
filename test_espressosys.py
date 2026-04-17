# test_espressosys.py
"""
Tests for EspressoSys module.
"""

import unittest
from espressosys import EspressoSys

class TestEspressoSys(unittest.TestCase):
    """Test cases for EspressoSys class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EspressoSys()
        self.assertIsInstance(instance, EspressoSys)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EspressoSys()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
