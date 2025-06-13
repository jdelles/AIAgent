import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

class TestCalculator(unittest.TestCase):

#     def test_current_directory(self):
#         expected = f'- main.py: file_size=564 bytes, is_dir=False\n- pkg: file_size=160 bytes, is_dir=True\n- tests.py: file_size=1330 bytes, is_dir=False'
#         result = get_files_info("calculator", ".")
#         self.assertEqual(result, expected)

#     def test_pkg_directory(self):
#         expected = "- __pycache__: file_size=128 bytes, is_dir=True\n- calculator.py: file_size=1720 bytes, is_dir=False\n- render.py: file_size=753 bytes, is_dir=False"
#         result = get_files_info("calculator", "pkg")
#         self.assertEqual(result, expected)

#     def test_invalid_bin_directory(self):
#         actual = get_files_info("calculator", "/bin")
#         self.assertEqual(actual, 'Error: Cannot list "/bin" as it is outside the working directory.')

#     def test_invalid_parent_directory(self):
#         actual = get_files_info("calculator", "../")
#         self.assertEqual(actual, 'Error: Cannot list "../" as it is outside the working directory.')

#     def test_get_file_content_main(self):
#         expected = """import sys
# from pkg.calculator import Calculator
# from pkg.render import render


# def main():
#     calculator = Calculator()
#     if len(sys.argv) <= 1:
#         print("Calculator App")
#         print('Usage: python main.py "<expression>"')
#         print('Example: python main.py "3 + 5"')
#         return

#     expression = " ".join(sys.argv[1:])
#     try:
#         result = calculator.evaluate(expression)
#         to_print = render(expression, result)
#         print(to_print)
#     except Exception as e:
#         print(f"Error: {e}")


# if __name__ == "__main__":
#     main()"""
    
#         actual = get_file_content("calculator", "main.py")
#         print(expected)
#         print(actual)
#         self.assertEqual(expected, actual)  # Note: using assertEqual instead of assertEquals

#     def test_get_file_content_calculator(self):
#         expected = """class Calculator:
#     def __init__(self):
#         self.operators = {
#             "+": lambda a, b: a + b,
#             "-": lambda a, b: a - b,
#             "*": lambda a, b: a * b,
#             "/": lambda a, b: a / b,
#         }
#         self.precedence = {
#             "+": 1,
#             "-": 1,
#             "*": 2,
#             "/": 2,
#         }

#     def evaluate(self, expression):
#         if not expression or expression.isspace():
#             return None
#         tokens = expression.strip().split()
#         return self._evaluate_infix(tokens)

#     def _evaluate_infix(self, tokens):
#         values = []
#         operators = []

#         for token in tokens:
#             if token in self.operators:
#                 while (
#                     operators
#                     and operators[-1] in self.operators
#                     and self.precedence[operators[-1]] >= self.precedence[token]
#                 ):
#                     self._apply_operator(operators, values)
#                 operators.append(token)
#             else:
#                 try:
#                     values.append(float(token))
#                 except ValueError:
#                     raise ValueError(f"invalid token: {token}")

#         while operators:
#             self._apply_operator(operators, values)

#         if len(values) != 1:
#             raise ValueError("invalid expression")

#         return values[0]

#     def _apply_operator(self, operators, values):
#         if not operators:
#             return

#         operator = operators.pop()
#         if len(values) < 2:
#             raise ValueError(f"not enough operands for operator {operator}")

#         b = values.pop()
#         a = values.pop()
#         values.append(self.operators[operator](a, b))"""
#         actual = get_file_content("calculator", "pkg/calculator.py")
#         print(expected)
#         print(actual)
#         self.assertEquals(expected, actual)

#     def test_main(self):
#         expected = 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory'
#         actual = get_file_content("calculator", "/bin/cat")
#         print(expected)
#         print(actual)
#         self.assertEquals(expected, actual)

#     def test_write_file_root(self):
#         content = "wait, this isn't lorem ipsum"
#         result = write_file("calculator", "lorem.txt", content)
#         self.assertEqual(result, f'Successfully wrote to "lorem.txt" ({len(content)} characters written)')
#         print(content)
#         print(result)
#         self.assertEqual(get_file_content("calculator", "lorem.txt"), content)

#     def test_write_file_subdirectory(self):
#         content = "lorem ipsum dolor sit amet"
#         result = write_file("calculator", "pkg/morelorem.txt", content)
#         self.assertEqual(result, f'Successfully wrote to "pkg/morelorem.txt" ({len(content)} characters written)')
#         print(content)
#         print(result)
#         self.assertEqual(get_file_content("calculator", "pkg/morelorem.txt"), content)

#     def test_write_file_outside_working_directory(self):
#         content = "this should not be allowed"
#         result = write_file("calculator", "/tmp/temp.txt", content)
#         print(content)
#         print(result)
#         self.assertEqual(result, 'Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory')

    def test_run_main_py(self):
        result = run_python_file("calculator", "main.py")
        self.assertIn("Calculator App", result)
        self.assertIn("Usage: python main.py \"<expression>\"", result)
        self.assertIn("Example: python main.py \"3 + 5\"", result)
        print(result)

    def test_run_tests_py(self):
        result = run_python_file("calculator", "tests.py")
        self.assertIn("OK", result)  
        print(result)
        

    def test_run_file_outside_directory(self):
        result = run_python_file("calculator", "../main.py")
        self.assertEqual(
            result,
            'Error: Cannot execute "../main.py" as it is outside the permitted working directory'
        )
        print(result)

    def test_run_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        self.assertEqual(
            result,
            'Error: File "nonexistent.py" not found.'
        )
        print(result)

if __name__ == "__main__":
    unittest.main()