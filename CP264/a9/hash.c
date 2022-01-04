/*
 -------------------------------------
 File:    hash.c
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
#include <string.h>
#include <stdlib.h>
#include "hash.h"

int hash(char *word) {
	unsigned int hash = 0, i;
	for (i = 0; word[i] != '\0'; i++) {
		hash = 31 * hash + word[i];
	}
	return hash % htsize;
}

HTNODE* new_hashnode(char *name, int value) {
	HTNODE *hnode = (HTNODE*) malloc(sizeof(HTNODE));
	strcpy(hnode->name, name);
	hnode->value = value;
	hnode->next = NULL;
	return hnode;
}

HASHTABLE* new_hashtable(int size) {
	HASHTABLE *htable = (HASHTABLE*) malloc(sizeof(HASHTABLE));
	htable->size = size;
	htable->count = 0;
	htable->hnp = (HTNODE**) malloc(sizeof(HTNODE) * size);
	for (int i = 0; i < size; i++)
		htable->hnp[i] = NULL;
	return htable;
}

HTNODE* search(HASHTABLE *ht, char *name) {
	// Get hash of key
	int index = hash(name);
	//exists at index
	if (ht->hnp[index]) {

		HTNODE *temp = ht->hnp[index];
		while (temp) {

			if (strcmp(temp->name, name) == 0)
				return temp;
			temp = temp->next;
		}
	}
	return NULL;
}

int insert(HASHTABLE *ht, HTNODE *np) {
	int index = hash(np->name);
	// Hash exists
	if (ht->hnp[index]) {

		HTNODE *temp = ht->hnp[index];
		while (temp) {
			if (strcmp(temp->name, np->name) == 0) {
				temp->value = np->value;
				return 0;
			}
			temp = temp->next;
		}
		temp = np;
		ht->count++;
		return 1;
	}

	ht->hnp[index] = np;
	ht->count++;

	return 1;
}

int delete(HASHTABLE *ht, char *name) {
	int index = hash(name);
	if (ht->hnp[index]) {
		HTNODE *temp = ht->hnp[index];
		HTNODE *prev = NULL;

		while (temp) {

			if (strcmp(temp->name, name) == 0) {
				if (prev)
					prev->next = temp->next;
				if (temp == ht->hnp[index])
					ht->hnp[index] = NULL;
				free(temp);
				ht->count--;
				return 1;
			}
		}
		prev = temp;
		temp = temp->next;
	}
	return 0;
}

// you can use this function in your program
void clean_hash(HASHTABLE **htp) {
	if (*htp == NULL)
		return;
	HASHTABLE *ht = *htp;
	HTNODE *sp = ht->hnp[0], *ptr, *temp;
	int i;
	for (i = 0; i < ht->size; i++) {
		ptr = ht->hnp[i];
		while (ptr) {
			temp = ptr;
			ptr = ptr->next;
			free(temp);
		}
		ht->hnp[i] = NULL;
	}
	free(ht->hnp);
	ht->hnp = NULL;
	*htp = NULL;
}

// you can use this function in your program
void display_hashtable(HASHTABLE *ht, int option) {
	int i = 0;
	HTNODE *ptr;
	if (option == 0) {
		printf("size:  %d\n", ht->size);
		printf("count: %d\n", ht->count);
		printf("hash data:\nindex: list of the data elements");
		for (i = 0; i < ht->size; i++) {
			ptr = *(ht->hnp + i);
			if (ptr)
				printf("\n%2d: ", i);

			while (ptr) {
				printf("(%s, %d) ", ptr->name, ptr->value);
				ptr = ptr->next;
			}
		}
		printf("\n");
	} else {

		for (i = 0; i < ht->size; i++) {
			ptr = *(ht->hnp + i);
			while (ptr) {
				printf("%s=%d\n", ptr->name, ptr->value);
				ptr = ptr->next;
			}
		}

	}

}
