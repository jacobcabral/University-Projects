/*
 * your program signature
 */

#include<stdio.h>
#include<math.h>

#define EPSILON 1e-6
//how are you today, IA? I'm having a time doing this late at night.
void display_polynomial(float p[], int n, float x) {
	int i;

	for (i = 0; i < n; i++) {
		printf("%.2f*%.2f^%d", p[i], x, (n - (i + 1)));

		if (i < n - 1) {
			printf("+");
		}

	}
}

float horner(float p[], int n, float x) {
	float eval_polynomial = p[0];
	for (int i = 1; i < n; i++) {
		eval_polynomial = eval_polynomial * x + p[i];
	}
	return eval_polynomial;
}

float bisection(float p[], int n, float a, float b) {
	float c, root;
	while (1) {
		c = (a + b) / 2; // find the midpoint
		if (fabs(horner(p, n, c)) == 0 && (c - a) < EPSILON) { //the function at the midpoint is now zero, a root has been found
			root = c;
			break;
		} else if (horner(p, n, c) * horner(p, n, a) < 0) { //perform some magicks that shall change some variables around in order to continue loopin
			b = c;
		} else {
			a = c;
		}
	}
	return root;
}
