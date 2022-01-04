/*
 -------------------------------------
 File:    queue.c
 Project:
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mywlu.ca
 Version  2021-03-02
 -------------------------------------
 */


#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "queue.h"

void enqueue(QUEUE *qp, NODE *np) {
	if(qp->front == NULL || qp->rear == NULL){
		qp->front = np;
		qp->rear = np;
	}else{
		qp->rear->next = np;
		qp->rear = np;
	}
}

NODE *dequeue(QUEUE *qp) {
	if (qp->front == NULL || qp->rear == NULL) return NULL;
	    NODE *np = qp->front;
	    qp->front = qp->front->next;
	    np->next = NULL;
	    return np;

}

void clean_queue(QUEUE *qp) {
	NODE *curr = qp->front;
	    NODE *prev = NULL;

	    while (curr != NULL)
	    {
	        prev = curr;
	        curr = curr->next;
	        free(prev);
	    }
	    qp = NULL;
}
