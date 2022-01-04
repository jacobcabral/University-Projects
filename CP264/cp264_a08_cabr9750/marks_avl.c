/*
 -------------------------------------
 File:    marks_avl.c
 Project: cabr9750_a07
 file description
 marks_avl
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version
 -------------------------------------
 */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "marks_avl.h"

void merge_tree(TNODE **rootp1, TNODE **rootp2) {
	if (!*rootp1 || !*rootp2)
		return;

	insert(rootp1, (*rootp2)->data.name, (*rootp2)->data.score);

	merge_tree(rootp1, &(*rootp2)->left);
	merge_tree(rootp1, &(*rootp2)->right);

	delete(rootp2, (*rootp2)->data.name);
}

void merge_data(MARKS *ds1, MARKS *ds2) {
	int count = ds1->count + ds2->count;
	float mean = (ds1->mean * ds1->count + ds2->mean * ds2->count) / count;
	float stddev = sqrt(
			((ds1->stddev * ds1->stddev * ds1->count
					+ ds1->mean * ds1->mean * ds1->count)
					+ (ds2->stddev * ds2->stddev * ds2->count
							+ ds2->mean * ds2->mean * ds2->count)) / count
					- mean * mean);

	merge_tree(&ds1->bst, &ds2->bst);

	ds1->count = count;
	ds1->mean = mean;
	ds1->stddev = stddev;
}

// the following are adapted from marks_bst.c of A7Q2

void display_stats(MARKS *sd) {
	printf("\nStatistics summary\n");
	printf("%s:%d\n", "count", sd->count);
	printf("%s:%.1f\n", "mean", sd->mean);
	printf("%s:%.1f\n", "stddev", sd->stddev);
}

void add_data(MARKS *sd, char *name, float score) {
	if (search(sd->bst, name) == NULL) {
		insert(&sd->bst, name, score);

		//recompute statistics summary by adding new one
		int count = sd->count;
		float mean = sd->mean;
		float stddev = sd->stddev;
		sd->count = count + 1;
		sd->mean = (mean * count + score) / (count + 1);
		sd->stddev = sqrt(
				score * score / (count + 1.0)
						+ (stddev * stddev + mean * mean)
								* (count / (count + 1.0))
						- sd->mean * sd->mean);

	} else
		printf("record exit");

}

void remove_data(MARKS *sd, char *name) {
	TNODE *np = NULL;
	if ((np = search(sd->bst, name)) != NULL) {
		float score = np->data.score;
		delete(&sd->bst, name);

		//recompute statistics summary by removing an old one
		int count = sd->count;
		float mean = sd->mean;
		float stddev = sd->stddev;
		sd->count = count - 1;
		sd->mean = (mean * count - score) / (count - 1.0);
		sd->stddev = sqrt(
				(stddev * stddev + mean * mean) * (count / (count - 1.0))
						- score * score / (count - 1.0) - sd->mean * sd->mean);

	} else
		printf("record not exit");
}

void display_marks(MARKS *dsp) {
	display_inorder_lines(dsp->bst);
	printf("\nstatistics summary\n");
	printf("%s:%d\n", "count", dsp->count);
	printf("%s:%.1f\n", "mean", dsp->mean);
	printf("%s:%.1f\n", "stddev", dsp->stddev);
}

void clean_marks(MARKS *dsp) {
	clean_tree(&dsp->bst);
	dsp->count = 0;
	dsp->mean = 0;
	dsp->stddev = 0;
}

void import_data(MARKS *ds, char *filename) {
	char line[40], name[20];
	FILE *fp = fopen(filename, "r");
	char *result = NULL;
	char delimiters[] = ",\n";
	float score = 0;
	int count = 0;
	float mean = 0, stddev = 0;

	if (fp == NULL) {
		perror("Error while opening the file.\n");
		exit(EXIT_FAILURE);
	}

	while (fgets(line, sizeof(line), fp) != NULL) {
		result = strtok(line, delimiters);
		if (result) {
			strcpy(name, result);
			result = strtok(NULL, delimiters);
			score = atof(result);
			count++;
			mean += score;
			stddev += score * score;
			insert(&ds->bst, name, score);
		}
	}

	ds->count = count;
	mean /= count;
	ds->mean = mean;
	ds->stddev = sqrt(stddev / count - mean * mean);

	fclose(fp);
}

void report_data(MARKS *sd, char *filename) {
	FILE *fp = fopen(filename, "w");

	print_to_file_inorder(sd->bst, fp);

	fprintf(fp, "\nStatistics summary\n");
	fprintf(fp, "%s:%d\n", "count", sd->count);
	fprintf(fp, "%s:%.1f\n", "mean", sd->mean);
	fprintf(fp, "%s:%.1f\n", "stddev", sd->stddev);
	fclose(fp);
}

void print_to_file_inorder(TNODE *root, FILE *fp) {
	if (root) {
		if (root->left)
			print_to_file_inorder(root->left, fp);
		fprintf(fp, "%s,%.1f,%c\n", root->data.name, root->data.score,
				letter_grade(root->data.score));
		if (root->right)
			print_to_file_inorder(root->right, fp);
	}
}

char letter_grade(float s) {
	char r = 'F';
	if (s >= 90)
		r = 'S';
	else if (s >= 80)
		r = 'A';
	else if (s >= 70)
		r = 'B';
	else if (s >= 60)
		r = 'C';
	else if (s >= 50)
		r = 'D';
	else
		r = 'F';
	return r;
}
