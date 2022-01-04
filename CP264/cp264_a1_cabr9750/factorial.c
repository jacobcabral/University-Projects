/*
 -------------------------------------
 File:    factorial.c
 Project: cp264_a1
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-01-14
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *args[]) {
	int i, n = 0, f = 1, prev, is_overflow = 0;

	if (argc > 1) {
		n = atoi(args[1]);  // convert command line argument to an integer

		if (n >= 1) {         // the conversion is successful
			i = 1;
			int result = 1;
			for (; i <= n; i++) {
				result *= i;
				if (i == 13) {
					printf("overflow:13!");
					break;
				}
				printf("%11d ", result);
				if (i % 4 == 0) {
					printf("\n");
				}
				if (n < 13) {
					if (n % 4 != 0) {
						printf("\n");
					}
					printf("%i!:%i!", n, result);
				}
			}

		} else {
			printf("%s:invalid argument\n", args[1]);
		}
	} else {
		printf("no argument");
	}
	return 0;
}
