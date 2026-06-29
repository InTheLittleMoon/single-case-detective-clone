import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("main", MODULE_PATH)
main = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(main)


class MainDispatchTests(unittest.TestCase):
    def test_dispatch_for_police_station_locations(self):
        self.assertEqual(
            main.get_location_handler("Police Station - Lobby"),
            main.police_station_actions,
        )
        self.assertEqual(
            main.get_location_handler("Police Station - My Desk"),
            main.police_station_actions,
        )


if __name__ == "__main__":
    unittest.main()
