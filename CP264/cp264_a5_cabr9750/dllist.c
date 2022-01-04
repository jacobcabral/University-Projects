/*
 -------------------------------------
 File:    dllist.c
 Project: cabr9750_a05
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-24
 -------------------------------------
 */
#include "dllist.h"

NODE* new_node(char data) {
	NODE *p = (NODE*) malloc(sizeof(NODE));
	p->data = data;
	p->next = NULL;
	p->prev = NULL;

	return p;
}

void display_forward(NODE *np) {
	NODE *p = np;
	while (p != NULL) {
		printf("%c ", p->data);
		p = p->next;
	}
}

void display_backward(NODE *np) {
	NODE *p = np;
	while (p != NULL) {
		printf("%c ", p->data);
		p = p->prev;
	}
}

void insert_start(NODE **startp, NODE **endp, NODE *new_np) {
	if (*startp == NULL && *endp == NULL) {
		*startp = new_np;
		*endp = new_np;
	} else {
		(*startp)->prev = new_np;
		new_np->next = *startp;
		*startp = new_np;
	}
}

void insert_end(NODE **startp, NODE **endp, NODE *new_np) {
	if (*startp == NULL && *endp == NULL) {
		*startp = new_np;
		*endp = new_np;
	} else {
		(*endp)->next = new_np;
		new_np->prev = *endp;
		*endp = new_np;
	}
}

void delete_start(NODE **startp, NODE **endp) {
	if (*startp != NULL && *endp != NULL) {
		NODE *temp = *startp;
		free(startp);

		*startp = temp->next;
		(*startp)->prev = NULL;

	}
}

void delete_end(NODE **startp, NODE **endp) {
	if (*startp != NULL && *endp != NULL) {
		NODE *temp = *endp;
		free(endp);

		*endp = temp->prev;
		(*endp)->next = NULL;

	}
}

void clean(NODE **startp, NODE **endp) {
	NODE *curr = *startp;
	NODE *prev = NULL;

	while (curr != NULL) {
		prev = curr;
		curr = curr->next;
		free(prev);
	}

	*startp = NULL;
	*endp = NULL;
}
