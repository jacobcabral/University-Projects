/*
 -------------------------------------
 File:    stack.h
 Project:
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mywlu.ca
 Version  2021-03-02
 -------------------------------------
 */



#ifndef STACK_H
#define STACK_H

#include "common.h"

typedef struct stack {
  NODE *top;
} STACK;

void push(STACK *sp, NODE *np);
NODE *pop(STACK *sp);
void clean_stack(STACK *sp);

#endif
