import pytest
import itertools

# Cartesian product of file names and extensions
# e.g. README.txt, README.md, CHANGELOG.txt, CHANGELOG.md ...
file_extensions = ['txt', 'md']
names = ['README', 'CHANGELOG', 'CONTRIBUTING', 'LICENSE']
exempt_files = [('.'.join(x)) for x in itertools.product(names, file_extensions)]

def test_filename(md_filepaths):
    if any(e in md_filepaths for e in exempt_files):
        assert True
    else:
        assert md_filepaths.islower() == True,'Filename should be lowercase'
