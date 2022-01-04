/*
 -------------------------------------
 File:    myrecord_llist.h
 Project: cabr9750_a05
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-24
 -------------------------------------
 */
// program signature
#ifndef LLIST
#define LLIST

/**
 * RECORD structure
 * name  - char array for person's name
 * score - float score of record
 */
typedef struct {
	char name[40];
	float score;
} RECORD;

/**
 * Define NODE structure
 * data  - RECORD data
 * next  - pointer pointing to the next node of linked list
 */

typedef struct node {
	RECORD data;
	struct NODE *next;
} NODE;

/**
 * Display linked list.
 * @param start Pointer to the first node of linked list.
 */
void display(NODE *start);

/**
 * Search linked list for name key.
 * @param start Pointer to the first node of linked list.
 * @param name Key to search
 * @return Pointer to found node if found; otherwise NULL
 */
NODE* search(NODE *start, char *name);

/**
 * Insert new record to linked list at the sorted position.
 * @param startp Pointer pointing to the start pointer of linked list, used to update the start node address in case of change.
 * @param name The name data of new record.
 * @param score The score data of new record
 */
void insert(NODE **startp, char *name, float score);

/**
 * Delete a record by name from linked list, the first one matched.
 * @param startp Pointer pointing to the start pointer of linked list, used to update the start node address in case of change.
 * @param name  The key used to find the node for deletion.
 */
int delete(NODE **startp, char *name);

/**
 * Clean linked list.
 * @param startp Pointer pointing to the start pointer of linked list, used to update the start node address in case of change.
 */
void clean(NODE **startp);

// The following are adapted/modified from previous assignments
typedef struct {
	int count;
	float mean;
	float stddev;
} REPORT;
char letter_grade(float score);
int import_data(NODE **startp, char *filename);
REPORT report_data(NODE *start, char *filename);
