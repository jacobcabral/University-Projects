/*
 -------------------------------------
 File:    quadratic.c
 Project: cp264_a1
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-01-13
 -------------------------------------
 */

#include <stdio.h>
#include <math.h>  // need this library for maths functions fabs() and sqrt()

#define EPSILON 0.000001
// or #define EPSILON 1e-6

int main() {
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

	float a, b, c, d, x1, x2;
	int inn;
	char temp;

	do {  // do-while for new input problem
		  // do-while loop to get correct input of three floating numbers,
		do {
			printf("Please enter the coefficients a,b,c\n");
			inn = scanf("%f,%f,%f", &a, &b, &c);

			if (inn != 3) {
				printf("input:Invalid input\n");
			} else
				break;

			do {  // flush the input buffer
				scanf("%c", &temp);
				if (temp == '\n')
					break;
			} while (1);

		} while (1);

		if (fabs(a) < EPSILON && fabs(b) < EPSILON && fabs(c) < EPSILON) {
			printf("input:quit\n");
			break;
		} else if (fabs(a) < EPSILON) {
			printf("input:not a quadratic equation\n");
		} else {

			d = b * b - 4 * a * c;  // compute the discriminant

			if (d > 0) {
				x1 = (-b + sqrt(d)) / (2 * a);
				x2 = (-b - sqrt(d)) / (2 * a);
				printf(
						"The equation has two distinct real roots\nx1:%f\nx2:%f\n",
						x1, x2);
			} else if (d == 0) {
				x1 = -b / (2 * a);
				x2 = x1;
				printf("The equation has two equal real roots\nx:%.6f\n", x1);
			} else {
				x1 = -b / (2 * a);
				float imaginaryroot = (sqrt(fabs(d)) / (2 * a));
				printf(
						"The equation has two complex roots:\nreal:%f\nimaginary:%f\n",
						x1, imaginaryroot);
			}

		}
	} while (1);
	return 0;
}
