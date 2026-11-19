import unittest

import app


class CensusAppTests(unittest.TestCase):
    def test_census_data_loads(self):
        data = app.load_data()
        self.assertGreater(len(data), 30)
        self.assertEqual(
            set(data.columns),
            {"state", "population", "literacy_rate", "sex_ratio", "growth_rate"},
        )

    def test_population_values_are_valid(self):
        data = app.load_data()
        self.assertTrue((data["population"] > 0).all())
        self.assertTrue((data["literacy_rate"] >= 0).all())
        self.assertTrue((data["sex_ratio"] > 0).all())


if __name__ == "__main__":
    unittest.main()
