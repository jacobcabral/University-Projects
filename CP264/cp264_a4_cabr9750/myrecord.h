/*
 -------------------------------------
 File:    myrecord.h
 Project: cabr9750_a04
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-10
 -------------------------------------
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define MAX_REC 100
#define MAX_LINE 100

typedef struct {
	int count;
	float mean;
	float stddev;
} REPORT;

typedef struct record {
	char name[20];
	float score;
} RECORD;

char letter_grade(float score);
int import_data(RECORD dataset[], char *filename);
REPORT report_data(RECORD dataset[], int n, char *filename);
