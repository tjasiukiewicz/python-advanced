#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void) {
	FILE * file = fopen("example_data.txt", "w");

	fputs("Example message", file);
	
	fclose(file);

	return 0;
}

