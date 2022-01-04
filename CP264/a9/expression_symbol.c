// your code signature

#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "queue.h"
#include "stack.h"
#include "expression_symbol.h"

QUEUE infix_to_postfix_symbol(char *infixstr, HASHTABLE *ht) {
	QUEUE queue = { 0 };
	STACK stack = { 0 };
	char *p = infixstr;
	int sign = 1;
	int num = 0;
	char symbol[20] = { };

	while (*p) {
		if (*p == '-' && (p == infixstr || *(p - 1) == '(')) {
			sign = -1;
		} else if (*p >= '0' && *p <= '9') {
			num = *p - '0';
			while ((*(p + 1) >= '0' && *(p + 1) <= '9')) {
				num = num * 10 + *(p + 1) - '0';
				p++;
			}
			enqueue(&queue, new_node(sign * num, 0));
			sign = 1;
		} else if (*p == '(') {
			push(&stack, new_node('(', 2));
		} else if (*p == ')') {
			while (stack.top) {
				if (stack.top->type == 2) {
					free(pop(&stack));
					break;
				}
				enqueue(&queue, pop(&stack));
			}
		} else if (type(*p) == 1) {
			while (stack.top && stack.top->type == 1
					&& get_priority(stack.top->data) >= get_priority(*p))
				enqueue(&queue, pop(&stack));
			push(&stack, new_node(*p, 1));
		} else if ((*p >= 'a' && *p <= 'z') || (*p >= 'A' && *p <= 'Z')) {

			char symbol[] = { *p, '\0' };
			HTNODE *tmp = search(ht, symbol);
			if (tmp)
				enqueue(&queue, new_node(tmp->value, 0));
		}

		p++;
	}

	while (stack.top) {
		enqueue(&queue, pop(&stack));
	}

	return queue;
}

int evaluate_infix_symbol(char *infixstr, HASHTABLE *ht) {
	return type(*infixstr) == 0 && *(infixstr + 1) == '\0' ?
			(*infixstr - '0') : evaluate_postfix(infix_to_postfix(infixstr, ht));
}

int evaluate_postfix(QUEUE queue) {
	NODE *p = queue.front;
	STACK stack = { 0 };
	int type = 0;
	int temp;
	while (p) {
		type = p->type;
		if (type == 0) {
			push(&stack, new_node(p->data, 0));
		} else if (type == 1) {
			int right = pop(&stack)->data;
			int left = pop(&stack)->data;
			temp = 0;
			if (p->data == '+')
				temp = left + right;
			else if (p->data == '-')
				temp = left - right;
			else if (p->data == '*')
				temp = left * right;
			else if (p->data == '/')
				temp = left / right;
			push(&stack, new_node(temp, 0));
		}
		p = p->next;
	}

	int result = stack.top->data;
	clean_stack(&stack);
	clean_queue(&queue);
	return result;
}

// you can use this function in your program
int resolve_symbol(char *statement, HASHTABLE *ht) {
	char name[10] = { 0 };
	char *dest = strstr(statement, "=");
	if (dest)
		*dest = '\0';
	else
		dest = statement;
	strcpy(name, statement);

	if ((name[0] >= 'a' && name[0] <= 'z')
			|| (name[0] >= 'A' && name[0] <= 'Z')) {

		int value = evaluate_infix_symbol(dest + 1, ht);

		if (value == 99999)  // escape value
			return 2;
		else {
			insert(ht, new_hashnode(name, value));
		}
		return 1;
	}
	return 0;
}
