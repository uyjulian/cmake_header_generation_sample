

import sys

s = ""
with open(sys.argv[1], "r") as f:
	s = f.read()

with open(sys.argv[2], "w") as wf:
	wf.write("\n#include \"genconfig.h\"\nconst char *configured_string = \"%s\";\n" % s)
