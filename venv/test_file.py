import sys
sys.path.append('/home/deveng/Documents/GitHub/PythonManualPart1')
import f1
import pytest
import unittest
import exe1



@pytest.mark.parametrize(
    ('input_n','excepted'),
    (
        (4,5),
        (6,7),
    )
)

def test_answer(input_n, excepted):
    assert f1.func(input_n) == excepted

def test_answer1():
    assert f1.func(5) == 6

class TestLegacy(unittest.TestCase):
    def test(self):
        self.assertEqual(f1.func(4),5)





def test_solution():
   # exe1.solution([1,2,3])
    #assert exe1.solution([9,9,9])==[1,0,0,0]
    assert exe1.solution([1, 2, 3])==[1,2,4]
    assert exe1.solution([9,9,9])==[0,0,2]








