/*
 -------------------------------------
 File:    hashing_int.c
 Project: 202001_CP264_Lab09_Hashing
 Hashing Source Code
 -------------------------------------
 Author:  Rick Magnotta
 ID:      xxxxxxxxx
 Email:   rmagnotta@wlu.ca
 Version: 2019-11-14
  ------------------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include "My_Definitions.h"
#include "hashing_int.h"

void initialize_hash_table(int hash_table[],             // The integer 1D array implementing the Hash Table.
                           int MAX_HASH_TABLE_SIZE)      // Max. number of slots defined for the Hash Table.
//=================================================
// Fill the hash table array with NULLS casted to "int"!
{
	for (int i=0; i<MAX_HASH_TABLE_SIZE; i++) {
	    hash_table[i] = (int)NULL;
	}
	return;
}

bool insert_hash_table(int hash_table[],                  // The integer 1D array implementing the Hash Table.
                       int MAX_HASH_TABLE_SIZE)           // Max. number of slots defined for the Hash Table.
//=============================================
// "hash_table" is a 1D-array of size "HASH_TABLE_SIZE"
//
// Algorithm to insert a value in linear probing:
// =============================================
// Step 1: Read the key/value to be inserted.
// Step 2: Let i = 0
// Step 3: Compute the index at which the key/value has to be inserted in hash table, as follows:
//                 index = ((key% MAX_HASH_TABLE_SIZE) + i) % MAX_HASH_TABLE_SIZE
// Step 4: If there is no element at that index, then insert the key/value at index and STOP!
// Step 5: If there is already an element at that index, then:
//         5.1 repeat Step-3 with (i+1), that is, re-hash (i.e. re-calculate index) with "i+1"
// step 6: Repeat Step-3, 4, and 5 for:
//           - as long as (i < MAX_HASH_TABLE_SIZE), and
//           - have not yet found an empty slot.
{
	bool INSERTED;            // TRUE if key/value is inserted, FALSE otherwise.
	int  key;                 // The input Key/Value to insert/store into the Hash Table/Array.
	int i;
	int index;

	printf("Enter an integer key/value to insert into Hash table: \n");
	scanf("%d", &key);
	while ( getchar() != '\n' );

	printf("\n");
	printf("Slot  Collision?  Value Inserted\n");
	printf("====  ==========  ==============\n");

	INSERTED = FALSE;

	//****************************************************************************************
	// NOTE: Move the following two print lines to the appropriate location in your code
	//       in order to print the contents of the "Slot  Collision?  Value Inserted" table.
	//                                             "====  ==========  =============="
	//
	//printf("%4d      no      %14d\n", index, key);
   	//printf("%4d      Yes\n", index);
	//
	//****************************************************************************************

    // <<<< Your Code >>>>
	i = 0;
	index = ((key % MAX_HASH_TABLE_SIZE) + i) % MAX_HASH_TABLE_SIZE;

	// Start linear probing
	// re-hash until no collision
	// this is skipped if there isn't a collision
	while (i < MAX_HASH_TABLE_SIZE && hash_table[index])
	{
		printf("%4d      Yes\n", index);
		i++;
		index = ((key % MAX_HASH_TABLE_SIZE) + i) % MAX_HASH_TABLE_SIZE;
	}

	// Insert if i < MAX_HASH_TABLE_SIZE
	if (i < MAX_HASH_TABLE_SIZE)
	{
		hash_table[index] = key;
		printf("%4d      no      %14d\n", index, key);
		INSERTED = TRUE;
	}
	else



	if ( !INSERTED ) printf("Element [%d] cannot be inserted.\n", key);

	return ( INSERTED );
}

bool search_hash_table(int hash_table[],                          // The integer 1D array implementing the Hash Table.
                       int MAX_HASH_TABLE_SIZE)                   // Max. number of slots defined for the Hash Table.
//=============================================
// Ask user to input the "key" value of interest, and use it's hash value
// to search for its presence/absence from the "hash_table".
// Prints appropriate search-result message, and
// returns TRUE if key is found in hash_table, FALSE otherwise.
{
	bool FOUND;                     // TRUE if input key is found in hash_table, false otherwise.
	int  key;                       // Input key value to search!
	int index;
	int i;

	FOUND = FALSE;
	printf("\n");
	printf("Enter integer key/value to search:\n");
	scanf("%d", &key);
	while ( getchar() != '\n' );

	//****************************************************************************************
	// NOTE: Move the following print line to the appropriate location in your code
	//
	// printf("Key/Value [%d] is found at index/slot [%d]\n", key, index);
	//
	//****************************************************************************************

    // <<<< Your Code >>>> DO NOT USE a LINEAR SEARCH Algorithm to find the location
	//                >>>>            of the Key in the Hash Table.
	//                >>>>            Use the same HASHING Algorithm used in the
	//                >>>>            "insert_hash_table()" function.
	i = 0;

	while (!FOUND && i < MAX_HASH_TABLE_SIZE)
	{
		index = ((key % MAX_HASH_TABLE_SIZE) + i) % MAX_HASH_TABLE_SIZE;
		if (hash_table[index] == key)
			FOUND = TRUE;
		else
			i++;
	}

	if ( !FOUND ) printf("Key/Value [%d] is not found!\n", key);
	else if (FOUND) printf("Key/Value [%d] is found at index/slot [%d]\n", key, index);

	return ( FOUND );
}

void display_hash_table(int hash_table[],                         // The integer 1D array implementing the Hash Table.
                        int MAX_HASH_TABLE_SIZE)                  // Max. number of slots defined for the Hash Table.
//==============================================
// Print the contents of the "hash_table".
{
	printf("\n");
	printf("Contents of Hash Table:\n");
    printf("====================== \n");
    printf("Index/Slot   Key/Value \n");
    printf("==========   ========= \n");

	for (int i=0; i< MAX_HASH_TABLE_SIZE; i++) {
       if ( hash_table[i] == (int)NULL )
          printf("%10d   %9s\n", i, "empty");
       else
          printf("%10d   %9d\n", i, hash_table[i]);
	}
	printf("\n");
	return;
}