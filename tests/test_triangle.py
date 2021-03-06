from typing import List
import pytest

@pytest.fixture(scope="function")
def run_triangles(script_runner):

    def do_run(sides:List):
        arglist = [str(side) for side in sides]
        return script_runner.run('triangles', *arglist)
    return do_run

@pytest.fixture(scope="function")
def help_message():
    return """usage: triangles [-h] sidex sidey sidez

Create your own triangle

positional arguments:
  sidex       Triangle x side
  sidey       Triangle y side
  sidez       Triangle z side

optional arguments:
  -h, --help  show this help message and exit
"""

class TestTriangle:

    def test_triangles_help_output(self, run_triangles, help_message):
        """
        Test Case: Check programs help output
        Steps:
        1. Run triangles program with --help param
        2. Check program's output
        Expected result:
        * Program outputs usage hint and available parameters sidex, sidey, sidez
        """
        ret = run_triangles(["--help"])

        assert ret.success, "Program executed with errors"
        assert ret.stdout == help_message, f"Invalid help present in program output"
        assert ret.stderr == '', f"Error thrown {ret.stderr}"


    @pytest.mark.parametrize("sides, results", 
        [
            ([7, 4, 4], ["isosceles"]),
            ([8, 5, 4], ["scalene"]),
            ([2, 8, 8], ["isosceles"]),
            ([4, 4, 4], ["isosceles", "equilateral"]),
        ],
    )
    def test_triangles_run_with_valid_params(self, run_triangles, sides, results):
        """
        Test Case: triangles output triangle type for valid input parameters
        Steps:
        1. Run triangles program with valid sides parameters (eg 1, 3, 123)
        2. Check program's output
        Expected result:
        * For each valid parameters set program outputs triangle type according to side length
        """
        ret = run_triangles(sides)
        
        assert ret.success, "Program executed with errors"
        assert all(result in ret.stdout for result in results), f"{results} not present in program output"
        assert ret.stderr == '', f"Error thrown {ret.stderr}"


    @pytest.mark.parametrize("sides, error_text", 
        [
            ([1.7, 3, 123], "invalid int value"),
            ([1, 2, 132], "Invalid triangle sides lenght!"),
            (["gfhfg", 4.5, 5.7], "invalid int value"),
            ([0, 3, 6], "Triangle has invalid sides!"),
            ([-7, -2, 1], "Triangle has invalid sides!"),
            ([4, 5], "error: the following arguments are required: sidez"),
            ([], "error: the following arguments are required: sidex, sidey, sidez")
        ],
    )
    def test_triangles_run_with_invalid_params_outputs_error_message(self, run_triangles, sides, error_text):
        """
        Test Case: Triangles output error for invalid parameters
        Steps:
        1. Run triangles program with invalid parameters (for example float values or invalid number of params)
        2. Check program's output
        Expected result:
        * Program outputs error message informing about invalid input parameter
        """
        ret = run_triangles(sides)
        
        assert not ret.success, "Program executed with no error"
        assert error_text in ret.stderr, f"{error_text} not present in program output"
        assert ret.stdout == '', f"Error not thrown for invalid param"