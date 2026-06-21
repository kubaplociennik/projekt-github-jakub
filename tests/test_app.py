import unittest

from app import app, load_profile


class AppTestCase(unittest.TestCase):
    def test_profile_has_expected_student(self):
        profile = load_profile()

        self.assertEqual(profile["student"]["first_name"], "Jakub")
        self.assertEqual(profile["student"]["last_name"], "Plociennik")
        self.assertEqual(profile["student"]["album_number"], "102182")

    def test_index_returns_hello_world_message(self):
        client = app.test_client()

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["message"],
            "Hello World from Jakub!",
        )


if __name__ == "__main__":
    unittest.main()
