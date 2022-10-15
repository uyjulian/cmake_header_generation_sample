
#include "genconfig.h"
#include <stdio.h>

int main(int ac, char** av)
{
	fprintf(stdout, "%s\n", configured_string);
	return 0;
}

