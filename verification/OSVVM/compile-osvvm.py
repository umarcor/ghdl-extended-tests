#!/usr/bin/env python3

# Script to compile the OSVVM libraries and verification models for GHDL.
#
# (1) creates a subdirectory in the current working directory
# (2) compiles all OSVVM packages

from pathlib import Path
from subprocess import check_call

ROOT = Path(__file__).parent

FileSets = {}

def processProFile(cdir: Path, file: str):
    proFile = cdir / file
    proDir = proFile.parent

    with proFile.open('r') as fptr:
        content = fptr.read().splitlines()

    library = 'work'
    skipIf = True

    def addFile(library: str, file: Path):
        if library not in FileSets:
            FileSets[library] = []
        FileSets[library].append(file)

    for item in content:
        if len(item) == 0 or item[0] in ['#','}']:
            continue

        parts = item.split(' ')

        if parts[0] == 'include':
            processProFile(proDir, parts[1])
            continue

        if parts[0] == 'library':
            library = parts[1]
            continue

        if parts[0] == 'analyze':
            addFile(library, proDir / parts[1])
            continue

        if len(parts) > 2 and parts[2] == 'analyze':
            if 'Aldec' in parts[3]:
                continue
            addFile(library, proDir / parts[3])
            continue

        if parts[0] != 'if':
            raise Exception('Unknown line <{}>'.format(item))


processProFile(
    ROOT / 'OsvvmLibraries',
    'OsvvmLibraries.pro'
)

DESTINATION = ROOT / 'precompiled'

DESTINATION.mkdir(exist_ok=True)

for key, val in FileSets.items():
    for item in val:
        check_call([
        'ghdl',
        '-a',
        '--std=08',
        '-P={}'.format(str(DESTINATION)),
        '--workdir={}'.format(str(DESTINATION)),
        "--work={}".format(key),
        str(item)
    ])
