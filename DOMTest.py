from pathlib import Path
from pytest import mark
from subprocess import check_call, STDOUT

if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)

def getVHDLSources():
	thisFile = Path(__file__)
	group = thisFile.parent.name
	basePath = thisFile.parent.parent.parent.resolve() / group / thisFile.stem
	return [str(path) for path in basePath.glob("**/*.vhd*")]


@mark.xfail
@mark.parametrize("file", getVHDLSources())
def test_AllVHDLSources(file: str):
	check_call(['ghdl-dom', file], stderr=STDOUT)
