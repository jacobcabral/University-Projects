/*
 -------------------------------------
 File:    matrix.c
 Project: cabr9750_a02
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-01-27
 -------------------------------------
 */

#include<stdio.h>
#include "matrix.h"

void display_matrix(int *m, int n) {
	int *p = m, i, j;
	for (i = 0; i < n; i++) {
		printf("\n");
		for (j = 0; j < n; j++)
			printf("%4d", *p++);
	}
	printf("\n");
}

int sum(int *m, int n) {
	int *p = m, i, j;
	int sum = 0;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			sum += *p++;
		}
	}
	return sum;
}

int is_magic_square(int *m, int n) {
	int i, j, *p = m;
	int sum = 0;
	int result = 1;
	int colsum = 0, diagsum = 0;

	int rowsum = n * (n * n + 1) / 2;
	for (i = 0; i < n; i++) {
		for (j = 0; i < n; i++) { //row
			sum += *(p + i * n + j);
		}
		if (sum != rowsum) {
			result = 0;
		}
		sum = 0;
	}
	for (i = 0; j < n; j++) { // column
		for (i = 0; i < n; i++) {
			sum += *(p + i * n + j);
		}
		if (sum != rowsum) {
			result = 0;
		}
		sum = 0;
	}
	for (i = 0; i < n; i++) { //diagonal
		diagsum += *(p + i * n + 1);
	}
	if (diagsum != rowsum) {
		result = 0;
	}
	diagsum = 0;

	for (i = 0; i < n; i++) { //diagonal redux, udda side
		diagsum += *(p + i * (n - 1) - i);
	}
	if (diagsum != rowsum) {
		result = 0;
	}

	return result;
}

void transpose_matrix(int *m1, int *m2, int n) {
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			//*(*(m2 + i) + j) = *(*(m1 + j) + i);
			*(m2 + j * n + i) = *(m1 + i * n + j);
		}
}

void multiply_matrix(int *m1, int *m2, int *m3, int n) {
	int sum;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < 4; j++) {
			sum = 0;
			for (int k = 0; k < n; k++) {
				//*(*(m3 + i) + j) += *(*(m2 + i) + k) * *(*(m1 + k) + j);
				sum += *(m1 + i * n + k) * *(m2 + k * n + j);

			}
			*(m3 + i * n + j) = sum;

		}
	}
}
