/*
 -------------------------------------
 File:    avl.c
 Project: cabr9750_a07
 file description
 avl
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
#include "avl.h"

// A utility functions
int max(int a, int b) {
	return (a > b) ? a : b;
}

int height(TNODE *np) {
	int height;
	height = 0;

	if (np) {
		height = np->height;
	}

	return height;
}

int balance_factor(TNODE *np) {
	int balance_factor;
	if (np) {
		balance_factor = np->left->height - np->right->height;
	} else if (np->left && !np->right) {
		balance_factor = np->left->height;
	} else if (!np->left && np->right) {
		balance_factor = 0 - np->right->height;
	} else {
		balance_factor = -1;
	}

	return balance_factor;
}

int is_avl(TNODE *root) {
	int result = 1;
	//check if there is no root
	if (!root) {
		result = 1;
	}
	//checking if the height of the root is less than the height of both left and right sub-trees
	if (height(root) < _max(height(root->left), height(root->right)) + 1) {
		result = 0;
	}
	if (abs(balance_factor(root)) > 1) {
		result = 0;
	}
	if (root->left && strcmp(root->left->data.name, root->data.name) > 0
			|| root->right
					&& strcmp(root->right->data.name, root->data.name) < 0) {
		result = 0;
	}
	if (!is_avl(root->left) || !is_avl(root->right)) {
		result = 0;
	}
	return result;
}

TNODE* rotate_right(TNODE *y) {
	TNODE *temp = y->left;
	TNODE *temp2 = temp->right;

	temp->right = y;
	y->left = temp2;

	y->height = 1 + _max(height(y->left), height(y->right));
	temp->height = 1 + _max(height(temp->left), height(temp->right));

	return temp;
}

TNODE* rotate_left(TNODE *x) {
	TNODE *temp = x->right;
	TNODE *temp2 = temp->left;

	temp->left = x;
	x->right = temp2;

	x->height = 1 + _max(height(x->left), height(x->right));
	temp->height = 1 + _max(height(temp->left), height(temp->right));

	return temp;
}

void insert(TNODE **rootp, char *name, float score) {
	TNODE *np = (TNODE*) malloc(sizeof(TNODE));
	if (np == NULL)
		return;
	strcpy(np->data.name, name);
	np->data.score = score;
	np->height = 1;
	np->left = NULL;
	np->right = NULL;

// 1. Perform the normal BST insertion
	if (*rootp == NULL) {
		*rootp = np;
		return;
	}

	TNODE *root = *rootp;
	if (strcmp(name, root->data.name) < 0)
		insert(&root->left, name, score);
	else if (strcmp(name, root->data.name) > 0)
		insert(&root->right, name, score);
	else
		return;

// 2. update height of this root node

// add your code here

// 3. Get the balance factor of this ancestor node to check whether this node became unbalanced

// add your code here

// 4. re-balance if not balanced

// add your code here

}

void delete(TNODE **rootp, char *name) {
	TNODE *root = *rootp;
	TNODE *np;

	if (root == NULL)
		return;

	if (strcmp(name, root->data.name) == 0) {
		if (root->left == NULL && root->right == NULL) {
			free(root);
			*rootp = NULL;
		} else if (root->left != NULL && root->right == NULL) {
			np = root->left;
			free(root);
			*rootp = np;
		} else if (root->left == NULL && root->right != NULL) {
			np = root->right;
			free(root);
			*rootp = np;
		} else if (root->left != NULL && root->right != NULL) {
			np = extract_smallest_node(&root->right);
			np->left = root->left;
			np->right = root->right;
			free(root);
			*rootp = np;
		}
	} else {
		if (strcmp(name, root->data.name) < 0) {
			delete(&root->left, name);
		} else {
			delete(&root->right, name);
		}
	}

// If the tree had only one node then return
	if (*rootp == NULL)
		return;

	root = *rootp;

// STEP 2: update the this root node's height

// add your code here

// STEP 3: get the balance factor of this root node

// add your code here

// STEP 4: re-balance if not balanced

// add your code here
}

// following functions are from bst.c of a7
TNODE* extract_smallest_node(TNODE **rootp) {
	TNODE *tnp = *rootp;
	TNODE *parent = NULL;
	if (tnp == NULL) {
		return NULL;
	} else {
		while (tnp->left) {
			parent = tnp;
			tnp = tnp->left;
		}
		if (parent == NULL)
			*rootp = tnp->right;
		else
			parent->left = tnp->right;
		tnp->left = NULL;
		tnp->right = NULL;
		return tnp;
	}
}

TNODE* search(TNODE *root, char *name) {
	TNODE *tp = root;
	while (tp) {
		if (strcmp(name, tp->data.name) == 0) {
			return tp;
		} else if (strcmp(name, tp->data.name) < 0)
			tp = tp->left;
		else
			tp = tp->right;
	}
	return NULL;
}

void clean_tree(TNODE **rootp) {
	if (*rootp) {
		TNODE *np = *rootp;
		if (np->left)
			clean_tree(&np->left);
		if (np->right)
			clean_tree(&np->right);
		free(np);
	}
	*rootp = NULL;
	;
}

void display_inorder(TNODE *root) {
	if (root) {
		if (root->left)
			display_inorder(root->left);
		printf("(%s %3.1f) ", root->data.name, root->data.score);
		if (root->right)
			display_inorder(root->right);
	}
}

void display_inorder_lines(TNODE *root) {
	if (root) {
		if (root->left)
			display_inorder_lines(root->left);
		printf("%-15s%.1f\n", root->data.name, root->data.score);
		if (root->right)
			display_inorder_lines(root->right);
	}
}

void display_tree(TNODE *root, int prelen) {
	if (root) {
		int i;
		for (i = 0; i < prelen; i++)
			printf("%c", ' ');
		printf("%s", "|___");
		printf("%s %.1f %d\n", root->data.name, root->data.score, root->height);
		display_tree(root->right, prelen + 4);
		display_tree(root->left, prelen + 4);
	}
}
