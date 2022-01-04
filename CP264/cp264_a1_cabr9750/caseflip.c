/*
 -------------------------------------
 File:    caseflip.c
 Project: cp264_a1
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-01-12
 -------------------------------------
 */

#include <stdio.h>
int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	char c = 0, temp;
	do {
		printf("Please enter a character\n");
		scanf("%c", &c);
		do {
			scanf("%c", &temp);
			if (temp == '\n')
				break;
		} while (1);
		if (c >= 'A' && c <= 'Z') { // big print smol
			printf("%c:%d,%c\n", c, c, c + 32);
		} else if (c >= 'a' && c <= 'z') { // smol print big
			printf("%c:%d,%c\n", c, c, c - 32);
		} else if (c == '*') {
			break;
		} else {
			printf("%c:invalid\n", c);
		}

	} while (1);
	printf("%c:quit\n", c);
	return 0;
}
