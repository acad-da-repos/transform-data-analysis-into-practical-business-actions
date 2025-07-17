
import unittest
import pandas as pd
from assignment import generate_recommendations

class TestBusinessActions(unittest.TestCase):
    def test_generate_recommendations(self):
        data = {'Product': ['A', 'B', 'C', 'D', 'E'],
                'Sales': [200, 50, 300, 80, 150]}
        df = pd.DataFrame(data)

        recommendations = generate_recommendations(df)

        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        self.assertIn("Promote C as it is a top-selling product with 300 sales.", recommendations)
        self.assertIn("Investigate B as its sales are low (50). Consider marketing changes or discontinuation.", recommendations)

if __name__ == '__main__':
    unittest.main()
