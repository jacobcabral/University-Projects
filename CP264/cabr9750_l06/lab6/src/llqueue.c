/*
 -------------------------------------
 File:    llqueue.c
 Project: stack_queue
 file description
 -------------------------------------
 Author:  Chandler Mayberry
 ID:      190688910
 Email:   heali@wlu.ca
 Version  2020-10-29
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <assert.h>
#include <limits.h>

#include "llqueue.h"

Queue_t qCreate() {
	return llCreate();
}

void qDestroy(Queue_t *q) {
	llDestroy(q);
}

void qPrint(const Queue_t q) {
	llPrint(q);
}

bool qIsEmpty(const Queue_t q) {
	return llIsEmpty(q);
}

void qClear(Queue_t *q) {
	llDelete(q);
}

int qLength(const Queue_t q) {
	return llLength(q);
}

void qEnqueue(Queue_t *q, ItemType value) {
	llAppend(q, value);
}

ItemType qFront(const Queue_t q) {

	ItemType peek = NULL;
	peek = llHead(q);
	return peek;
}

ItemType qDequeue(Queue_t *q) {
	ItemType removed = NULL;

	removed = llPop(q);

	return removed;
}
