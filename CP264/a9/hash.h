/*
 -------------------------------------
 File:    hash.h
 Project: cabr9750_a07
 file description
 
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version
 -------------------------------------
 */

#ifndef HASH_H
#define HASH_H

extern int htsize;

typedef struct hashnode {
	char name[10];  // used as key variable
	int value;
	struct hashnode *next;
} HTNODE;

typedef struct hashtable {
	HTNODE **hnp;    // pointer pointing to the array of hashnode pointers 
	int size;          // hash table size, maximum number of different indices
	int count;         // number of data elements in the hash table
} HASHTABLE;

// add your code documentation
int hash(char *name);

// add your code documentation
HTNODE* new_hashnode(char *name, int vale);

// add your code documentation
HASHTABLE* new_hashtable(int size);

// add your code documentation
HTNODE* search(HASHTABLE *ht, char *name);

// add your code documentation
int insert(HASHTABLE *ht, HTNODE *np);

// add your code documentation
int delete(HASHTABLE *ht, char *name);

void clean_hash(HASHTABLE **htp);

void display_hashtable(HASHTABLE *ht, int option);

#endif
