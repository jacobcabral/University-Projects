#include <stdio.h>
#include "stack.h"

void push(STACK *sp, NODE *np) {
if(sp->top == NULL){
	sp->top = np;
} else {
	np->next = sp->top;
	sp->top = np;
}
}

NODE *pop(STACK *sp) {
    if (sp->top == NULL) return NULL;

    NODE *np = sp->top;
    sp->top = sp->top->next;
    np->next = NULL;
    return np;
}


void clean_stack(STACK *sp) {
	NODE *curr = sp->top;
	NODE *prev = NULL;

	while(curr != NULL){
		clean(curr);
	}
}
