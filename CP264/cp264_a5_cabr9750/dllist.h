/*
 -------------------------------------
 File:    dllist.h
 Project: cabr9750_a05
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-24
 -------------------------------------
 */

#ifndef DLLIST
#define DLLIST

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
	char data;
	struct node *prev;
	struct node *next;
} NODE;

#endif
