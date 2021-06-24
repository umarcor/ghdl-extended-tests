from subprocess import check_call, STDOUT
from pathlib import Path
from pytest import mark

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)

def getVHDLSources():
	basePath = Path(__file__).resolve().parent
	return [str(path) for path in basePath.glob("**/*.vhd*")]


@mark.xfail
@mark.parametrize("file", getVHDLSources())
def test_AllVHDLSources(file):
	check_call(['ghdl-dom', str(file)], stderr=STDOUT)
