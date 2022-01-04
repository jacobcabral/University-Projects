/*
 -------------------------------------
 File:    bigint.h
 Project: cabr9750_a05
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-24
 -------------------------------------
 */
#ifndef BIGINT_H
#define BIGINT_H

#include "dllist.h"

typedef struct bigint {
	NODE *start;
	NODE *end;
} BIGINT;

BIGINT add(BIGINT oprand1, BIGINT oprand2);
BIGINT Fibonacci(int n);

BIGINT bigint(char *digitstr);
void display_bigint(BIGINT bignumber);
void clean_bigint(BIGINT *bignumberp);
#endif
