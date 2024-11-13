from src.math_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(1,2)==3
    
def test_sub():
    assert sub(2,5)==-3
    assert sub(1,2)==-1
    
    
    