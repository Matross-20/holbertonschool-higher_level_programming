import pytest
from task_01_duck_typing import Circle

def test_circle_negative():
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        Circle(radius=-5)

if __name__ == "__main__":
    pytest.main()

