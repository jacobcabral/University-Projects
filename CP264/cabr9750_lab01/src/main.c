/*
 -------------------------------------
 File:    main.c
 Project: cabr9750_lab01
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-01-13
 -------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
	setbuf(stdout, NULL); // turns standard output buffering off
	int number = 0;
	printf("Enter a number: ");
	scanf("%d", &number);
	printf("The number you entered is %d\n", number);
	return (0);
}
