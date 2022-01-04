/*
 -------------------------------------
 File:    bigint.c
 Project: cabr9750_a05
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-24
 -------------------------------------
 */

#include "bigint.h"

BIGINT bigint(char *p) {
	BIGINT bn = { 0 };
	if (p == NULL)
		return bn;
	else if (!(*p >= '0' && *p <= '9')) {
		return bn;
	} else if (*p == '0' && *(p + 1) == '\0') {
		insert_end(&bn.start, &bn.end, new_node(*p - '0'));
		return bn;
	} else {
		while (*p) {
			if (*p >= '0' && *p <= '9') {
				insert_end(&bn.start, &bn.end, new_node(*p - '0'));
			} else {
				clean_bigint(&bn);
				break;
			}
			p++;
		}
		return bn;
	}
}

void display_bigint(BIGINT bignumber) {
	NODE *ptr = bignumber.start;
	while (ptr != NULL) {
		printf("%d", ptr->data);
		ptr = ptr->next;
	}
}

void clean_bigint(BIGINT *bignumberp) {
	clean(&bignumberp->start, &bignumberp->end);
}

BIGINT add(BIGINT op1, BIGINT op2) {
	BIGINT sum = bigint(NULL);

	BIGINT sum = bigint(NULL);

	if (op1.start == NULL || op2.start == NULL)
		return sum;

	NODE *curr1 = op1.end;
	NODE *curr2 = op2.end;

	int temp_sum = 0;
	int carry = 0;

	while (curr1 != NULL || curr2 != NULL) {

		temp_sum = carry + (curr1 != NULL ? curr1->data : 0)
				+ (curr2 != NULL ? curr2->data : 0);
		carry = temp_sum;
		carry = (carry >= 10) ? 1 : 0;
		temp_sum = (carry == 1) ? temp_sum - 10 : temp_sum;

		insert_start(&sum.start, &sum.end, new_node(temp_sum));
		// Move backwards in lists if they have remaining elements
		curr1 = (curr1 != NULL) ? curr1->prev : curr1;
		curr2 = (curr2 != NULL) ? curr2->prev : curr2;
	}

	if (carry > 0)
		insert_start(&sum.start, &sum.end, new_node(1));

	return sum;
}

BIGINT Fibonacci(int n) {
	if (n <= 2) {
		return bigint("1");
	} else {
		BIGINT temp = bigint(NULL);
		BIGINT f1 = bigint("1");
		BIGINT f2 = bigint("1");

		BIGINT *temp_prev = &temp;
		BIGINT *f1_prev = &f1;

		for (int i = 3; i <= n; i++) {
			temp = f2;
			f2 = add(f1, f2);
			f1 = temp;

		}

		return f2;
	}
