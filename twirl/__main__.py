from twirl.errors import IncorrectArgumentFormatError
from twirl.core.download import pkg
from sys import argv

args = argv[1:]

flags = [
    "install",
    "remove",
    "purge",
    "search"
]

count = 0
prettyargs = ', '.join(flags)
for arg in args: 
    if args[count] not in flags and count != 1:
        raise IncorrectArgumentFormatError(f"Unknown argument '{args[count]}'. (Valid arguments are {prettyargs})")
    count += 1

if count != 2:
    raise IncorrectArgumentFormatError(f"Incorrect amount of operations provided. (Expected 2, got {count})")

pkg(argv[2])