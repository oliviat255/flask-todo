from src.app import create_app

class TestApp: 
    """Test class for Flask app creation"""
    def test_dev_app(self): 
        """Test creation of the local flask app"""
        create_app("testing")