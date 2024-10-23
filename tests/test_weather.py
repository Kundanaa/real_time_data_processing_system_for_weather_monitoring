from src.data.processing import kelvin_to_celsius

def test_kelvin_to_celsius():
    assert kelvin_to_celsius(300) == 26.85