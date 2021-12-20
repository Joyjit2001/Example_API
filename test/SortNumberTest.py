import unittest
import sys
#from importlib.machinery import SourceFileLoader

sys.path.append('/Users/joyjitchatterjee/ExampleAPI/src')
import SortNumber

#mymodule = SourceFileLoader('SortNumber.py','/Users/joyjitchatterjee/ExampleAPI/src/SortNumber.py').load_module();


class TestStringMethods(unittest.TestCase):

    def test_numberSort(self):
        x = [1,4,3,2]
        y = [1,2,3,4]
        self.assertEqual(SortNumber.Sort_Number(x),y)


if __name__ == '__main__':
    unittest.main()