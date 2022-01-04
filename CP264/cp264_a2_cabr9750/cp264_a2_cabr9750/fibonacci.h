/*
 * your program signature
 */

extern int *la;  // global pointer variable to get local variable address

int iterative_fibonacci(int n) {
	int first_term = 0, second_term = 1, next_term;
	if (&n < la)
		la = &n;
	if (&n < la)
		la = &first_term;
	if (&n < la)
		la = &second_term;
	if (&n < la)
		la = &next_term;
	for (int i = 1; i < n; i++) {

		next_term = first_term;
		first_term = second_term;
		second_term = first_term + next_term;
	}

	return second_term;
}

int recursive_fibonacci(int n) {
	if (&n < la)
		la = &n;
	if (n == 0)
		return 0;
	else if (n == 1)
		return 1;
	else
		return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2));
}
