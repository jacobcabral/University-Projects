/*
 -------------------------------------
 File:    myrecord.c
 Project: cabr9750_a04
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-09
 -------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "myrecord.h"

#define MAX_LINE 100

char letter_grade(float s) {
	char grade;

	// determine letter grade with good 'ol if else
	if (s >= 90)
		grade = 'S';
	else if (s >= 80)
		grade = 'A';
	else if (s >= 70)
		grade = 'B';
	else if (s >= 60)
		grade = 'C';
	else if (s >= 50)
		grade = 'D';
	else
		grade = 'F';
	return grade;
}

int import_data(RECORD dataset[], char *filename) {
	FILE *fp;
	char delimiters[] = ",\n\r";
	char line[100];
	int i = 0;  // record counter
	char *token = NULL;
	if ((fp = fopen(filename, "r")) == NULL) {
		perror("Unable to open file");
		return -1;
	} else {
		// Read all lines of the file
		while (fgets(line, sizeof(line), fp) != NULL) {
			token = (char*) strtok(line, delimiters);

			strcpy(dataset[i].name, token); // Copy string to char array
			token = (char*) strtok(NULL, delimiters);

			dataset[i].score = atof(token); // Convert string to float
			i++;
		}
	}
	fclose(fp);
	return i;   // Return number of records
}

REPORT report_data(RECORD dataset[], int n, char *filename) {
	REPORT report = { };
	if (n < 1)
		return report;
	FILE *fp;
	fp = fopen(filename, "w");
	int i;
	float mean = 0;
	float sttdev = 0;

	//print to the file
	for (i = 0; i < n; i++) {
		fprintf(fp, "%-15s%c\n", dataset[i].name,
				letter_grade(dataset[i].score));
	}

	for (i = 0; i < n; i++) {
		mean += dataset[i].score;
		sttdev += dataset[i].score * dataset[i].score;
	}

	mean /= n;
	sttdev = sqrt(sttdev / n - mean * mean);

	report.mean = mean;
	report.stddev = sttdev;
	report.count = n;

	return report;
}
