// your program signature

#include "mysort.h"

BOOLEAN is_sorted(int *a, int left, int right) {
	BOOLEAN result = false;
	for (int i = left; i < right - 1; i++) {
		if (a[i] > a[i + 1]) {
			result = false;
		} else {
			result = true;
		}
	}
	return result;
}

void select_sort(int *a, int left, int right) {
	int i, j, k;
	for (i = 0; i <= right; ++i) {

		k = i;
		for (j = i + 1; j <= right; ++j) {
			if (*(a + j) < *(a + k)) {
				k = j;
			}
		}
		if (i != k) {
			swap((a + k), (a + i));
		}
	}

	return;
}

void quick_sort(int *a, int left, int right) {
// your implementation
	int i, j, pivot;
	if (left < right) {
		pivot = left;
		i = left;
		j = right;

		while (i < j) {
			while (*(a + i) <= *(a + pivot) && i < right)
				i++;
			while (*(a + j) > *(a + pivot))
				j--;
			if (i < j)
				swap(a + i, a + j);
		}
		swap(a + j, a + pivot);
		quick_sort(a, left, j - 1);
		quick_sort(a, j + 1, right);
	}
}

void swap(int *first, int *second) {
	int temp = *first;
	*first = *second;
	*second = temp;
}

