/*
 -------------------------------------
 File:    myword.c
 Project: cabr9750_a03
 file description
 -------------------------------------
 Author:  Jacob Cabral
 ID:      190689750
 Email:   cabr9750@mylaurier.ca
 Version  2021-02-03
 -------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include "mystring.h"
#include "myword.h"

void set_stopword(char *filename, char *stopwords[]) {
	char line[1000];
	char delimeters[] = " .,\n\t\r";
	char *token;
	int i;
	FILE *fp = fopen(filename, "r");

	while (fgets(line, 1000, fp) != NULL) {
		token = (char*) strtok(line, delimeters);
		while (token != NULL) {
			i = (int) (*token - 'a');
			strcat(stopwords[i], token);
			strcat(stopwords[i], ",");

			token = (char*) strtok(NULL, delimeters);
		}
	}

}

// this function check if word is a word in string str,
// returns 1 if yes, 0 otherwise
int contain_word(char *str, char *word) {
	if (str == NULL || word == NULL)
		return 0;
	char temp[20] = { 0 };
	strcat(temp, ",");
	strcat(temp, word);
	strcat(temp, ",");

	if (strstr(str, temp))
		return 1;
	else
		return 0;

}

// this function check if the word is contained in directory stopwords[]
// returns 1 if yes, 0 otherwise. It use function contain_word()
int is_stopword(char *stopwords[], char *word) {
	if (word == NULL || *word == '\0')
		return 0;
	else
		return contain_word(stopwords[*word - 'a'], word);
}

int process_word(char *filename, WORDSUMMARY *ws, char *stopwords[]) {
	FILE *fp = fopen(filename, "r");
	if (fp != NULL) {
		char line[1000];
		const char delimiters[] = " .,;:!()&?-\n\t\r\"\'";
		char *token;

		while (fgets(line, MAX_LINE_LEN, fp) != NULL) {
			ws->line_count++;

			lower_case(line);
			trim(line);
			token = (char*) strtok(line, delimiters);
			while (token != NULL) {
				int found_temp = 0;
				ws->word_count++;

				if (is_stopword(stopwords, token) == 0) {
					if (is_stopword(stopwords, token)) {
						int i = 0;

						while (i < ws->keyword_count) {
							if (strcmp(token, ws->word_array[i].word) == 0) {
								found_temp = 1;
								ws->word_array[i].frequency++;

							}
							i += 1;
						}
						if (found_temp == 0) {
							int end = ws->keyword_count;
							strcpy(ws->word_array[end].word, token);
							ws->word_array[end].frequency = 1;
							ws->keyword_count++;
						}
					}
				}
				token = (char*) strtok(NULL, delimiters);

			}
		}
	} else {
		printf("File not read");
		return -1;
	}
	fclose(fp);

	return 0;

}

int save_to_file(char *filename, WORDSUMMARY *ws) {
	int i = 0;
	FILE *fp = fopen(filename, "w");

	fprintf(fp, "Line count: %d\n", ws->line_count);
	fprintf(fp, "Word count: %d\n", ws->word_count);
	fprintf(fp, "non common word count: %d\n", ws->keyword_count);

	while (i < ws->keyword_count) {
		fprintf(fp, "%s:%d\n", ws->word_array[i].word,
				ws->word_array[i].frequency);
		i++;
	}
	fclose(fp);
	return 0;
}
