from pathlib import Path
from pytest import mark
from subprocess import check_call, STDOUT

if __name__ == "__main__":
    print("ERROR: you called a testcase declaration file as an executable module.")
    print("Use: 'python -m unitest <testcase module>'")
    exit(1)


def pytest_generate_tests(metafunc):
    testParameters = metafunc.cls.parameters[metafunc.function.__name__]

    thisFile = Path(__file__)
    basePath = thisFile.parent.resolve() / testParameters["directory"]

    metafunc.parametrize(["file"], [[str(path)] for path in basePath.glob("**/*.vhd*")])


class AllVHDLFiles:
    parameters = {
        "test_OSVVM": {"directory": "verification/OSVVM"},
        "test_UVVM": {"directory": "verification/UVVM"},
        "test_VUnit": {"directory": "verification/VUnit"},
    }

    def _runDOM(self, file: str):
        check_call(["ghdl-dom", file], stderr=STDOUT)

    @mark.xfail
    def test_OSVVM(self, file: str):
        self._runDOM(file)

    @mark.xfail
    def test_UVVM(self, file: str):
        self._runDOM(file)

    @mark.xfail
    def test_VUnit(self, file: str):
        self._runDOM(file)
