# test_deployscript.py
"""
Tests for DeployScript module.
"""

import unittest
from deployscript import DeployScript

class TestDeployScript(unittest.TestCase):
    """Test cases for DeployScript class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeployScript()
        self.assertIsInstance(instance, DeployScript)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeployScript()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
