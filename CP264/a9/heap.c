/*
 -------------------------------------
 File:    heap.c
 Project: cabr9750_a07
 file description

 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version
 -------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "heap.h"

HEAP* new_heap(int capacity) {
	//allocate the memory for the heap
	HEAP *nheap = (HEAP*) malloc(sizeof(HEAP));
	nheap->capacity = capacity;
	nheap->size = 0;
	nheap->hnap = (HNODE*) malloc(sizeof(HNODE) * capacity);

	return nheap;
}

void insert(HEAP *heap, HNODE new_node) {
	if (!heap)
		return;

	if (heap->size == heap->capacity) {
		HNODE *temp;

		heap->capacity *= 2;
		temp = realloc(heap->hnap, sizeof(HNODE) * heap->capacity);
		if (temp) {
			heap->hnap = temp;
			display_heap(heap);
		} else {
			temp = malloc(sizeof(HNODE) * heap->capacity);
			if (temp) {
				memcpy(temp, heap->hnap, sizeof(HNODE) * heap->size);
				free(heap->hnap);
				heap->hnap = temp;
			} else {
				printf("Array resize failed\n");
			}
		}
	}
	heap->hnap[heap->size] = new_node;
	heap->size++;

	int curr_index = heap->size - 1;
	int parent_index = (curr_index - 1) / 2;
	while (cmp(heap->hnap[curr_index].key, heap->hnap[parent_index].key) == -1) {
		HNODE temp = heap->hnap[curr_index];
		heap->hnap[curr_index] = heap->hnap[parent_index];
		heap->hnap[parent_index] = temp;
		curr_index = parent_index;
		parent_index = (curr_index - 1) / 2;
	}
}

HNODE extract_min(HEAP *heap) {
	HNODE extraction = heap->hnap[0];
	heap->hnap[0] = heap->hnap[heap->size - 1];
	heap->hnap[heap->size - 1].data = 0;
	heap->hnap[heap->size - 1].key = 0;
	heap->size--;

	if (heap->size > 0) {
		//step2: heapify_down.
		if ((cmp(heap->hnap[0].key, heap->hnap[1].key) == 1)
				|| cmp(heap->hnap[0].key, heap->hnap[2].key) == 1)
			heapify_down(heap);

		//step3: remove extra capacity if the size of the array is less than 1/4
		if ((float) ((float) heap->size / (float) heap->capacity) * 100 <= 25)
			heap->capacity = heap->capacity / 4;

	}
	return extraction;
}

void decrease_key(HEAP *heap, int node_index, KEYTYPE key_value) {
	if (!heap)
		return;
	if (node_index > heap->size)
		return;

	heap->hnap[node_index].key = key_value;

// Heapify as needed
	int curr_index = heap->size - 1;
	int parent_index = (curr_index - 1) / 2;
	while (cmp(heap->hnap[curr_index].key, heap->hnap[parent_index].key) == -1) {
		// Swap curr node and parent node
		HNODE temp = heap->hnap[curr_index];
		heap->hnap[curr_index] = heap->hnap[parent_index];
		heap->hnap[parent_index] = temp;
		curr_index = parent_index;
		parent_index = (curr_index - 1) / 2;
	}
}

int find_index(HEAP *heap, DATA value) {
	if (!heap)
		return -1;

	int index = 0;
	HNODE *curr = &(heap->hnap[index]);

	while (curr && index < heap->size) {
		if (curr->data == value)
			return index;
		index++;
		curr = &(heap->hnap[index]);
	}

	return -1;
}

void display_heap(HEAP *hp) {
	printf("\nsize:%d\ncapacity:%d\n", hp->size, hp->capacity);
	printf("(index, key, data):\n");
	int i;
	for (i = 0; i < hp->size; i++) {
		printf("(%d %d %d) ", i, hp->hnap[i].key, hp->hnap[i].data);
		if (i % 10 == 9)
			printf("\n");
	}
	printf("\n");
}

int cmp(KEYTYPE a, KEYTYPE b) {
	if (a < b)
		return -1;
	else if (a == b)
		return 0;
	else
		return 1;
}
