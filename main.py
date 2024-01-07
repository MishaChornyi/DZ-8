import time
import unittest

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функція {func.__name__} виконалася за {execution_time} секунд")
        return result
    return wrapper


@measure_execution_time
def example_function():
    time.sleep(2)
    return "Виконано"


class TestExecutionTimeMeasurement(unittest.TestCase):
    def test_execution_time(self):
        result = example_function()
        self.assertEqual(result, "Виконано")

if __name__ == "__main__":
    unittest.main()
