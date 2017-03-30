from comp_organization_tools import *

def test_success():
    assert True

def test_decToBin():
    for k in range(1000):
        assert (binToDec(decToBin(k)) == k)
def test_hexToDec():
    for k in range(1, 1000):
        assert (hexToDec(decToHex(k, verbose=False), verbose=False) == k)