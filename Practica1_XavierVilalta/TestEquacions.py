import unittest
from Equacio1 import EquacioPrimerGrau

class TestEquacions(unittest.TestCase):

    def test_eq(self):
        self.assertEqual(EquacioPrimerGrau("2x + 3 = 7").calcula(), 2.0)
        self.assertEqual(EquacioPrimerGrau("2x - 3 = 1").calcula(), 2.0)
        self.assertEqual(EquacioPrimerGrau("2x * 3 = 7").calcula(), 2.0)


if __name__ == "__main__":
    unittest.main()
