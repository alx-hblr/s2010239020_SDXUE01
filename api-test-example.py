import unittest
import requests
import time

class TestRecipeAPI(unittest.TestCase):
    API_URL = "http://127.0.0.1:8080/recipes"

    def test_get_all_recipes(self):
        response = requests.get(self.API_URL)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_create_recipe(self):
        # Define a recipe to create
        recipe = {
            "name": "Test Recipe",
            "description": "This is a test recipe.",
            "ingredients": ["Ingredient 1", "Ingredient 2"],
            "instructions": "Test instructions."
        }

        # Send a POST request to create the recipe
        response = requests.post(self.API_URL, json=recipe)

        # Check that the response has a success status code and contains the created recipe
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), recipe)

if __name__ == '__main__':
    time.sleep(15)
    unittest.main()
