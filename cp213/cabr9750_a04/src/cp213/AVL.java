package cp213;

/**
 * Implements an AVL (Adelson-Velsky Landis) tree. Extends BST.
 *
 * @author your name here
 * @author David Brown
 * @version 2020-11-04
 */
public class AVL extends BST {

	/**
	 * Returns the balance value of node. If greater than 1, then left heavy, if
	 * less than -1, then right heavy. If in the range -1 to 1 inclusive, the node
	 * is balanced. Used to determine whether to rotate a node upon insertion.
	 *
	 * @param node The TreeNode to analyze for balance.
	 * @return A balance number.
	 */
	private int balance(final TreeNode node) {
		return this.nodeHeight(node.getLeft()) - this.nodeHeight(node.getRight());
	}

	/**
	 * Performs a left rotation around node.
	 *
	 * @param node The subtree to rotate.
	 * @return The new root of the subtree.
	 */
	private TreeNode rotateLeft(final TreeNode node) {
		// Rearrange the nodes.
		final TreeNode temp = node.getRight();
		node.setRight(temp.getLeft());
		temp.setLeft(node);
		node.updateHeight();
		temp.updateHeight();
		
		
		return temp;
	}

	/**
	 * Performs a right rotation around {@code node}.
	 *
	 * @param node The subtree to rotate.
	 * @return The new root of the subtree.
	 */
	private TreeNode rotateRight(final TreeNode node) {
		// Rearrange the nodes.
		final TreeNode temp = node.getLeft();
		node.setLeft(temp.getRight());
		temp.setRight(node);
		// Update the node heights.
		node.updateHeight();
		// Return new root.
		return temp;
	}

	/**
	 * Auxiliary method for {@code insert}. Inserts data into this AVL.
	 *
	 * @param node the current node (TreeNode)
	 * @param data Data to be inserted into the node
	 * @return The inserted node.
	 */
	@Override
	protected TreeNode insertAux(TreeNode node, final CountedCharacter data) {
		int balance = 0;

		if (node == null) {
			// Base case - add a new node containing the data.
			node = new TreeNode(data);	
			
			this.size++; 
			
			
		} else {
			// Compare the node data against the insert data.
			final int result = node.getValue().compareTo(data);

			if (result > 0) {
				// General case - check the left subtree.
				node.setLeft(this.insertAux(node.getLeft(), data));
				node.updateHeight();
				// As a left insertion, can only be unbalanced on the left.
				balance = this.balance(node);

				if (balance > 1 && this.balance(node.getLeft()) >= 0) {
					// Left Left Case - single rotation
					node = this.rotateRight(node);
				} else if (balance > 1 && this.balance(node.getLeft()) < 0) {
					// Left Right Case - double rotation
					node.setLeft(this.rotateLeft(node.getLeft()));
					node = this.rotateRight(node);
				}
			} else if (result < 0) {
				// General case - check the right subtree.
				node.setRight(this.insertAux(node.getRight(), data));
				node.updateHeight();
				// As a right insertion, can only be unbalanced on the right.
				balance = this.balance(node);

				if (balance < -1 && this.balance(node.getRight()) <= 0) {
					// Right Right Case - single rotation
					node = this.rotateLeft(node);
				} else if (balance < -1 && this.balance(node.getRight()) > 0) {
					// Right Left Case - double rotation
					node.setRight(this.rotateRight(node.getRight()));
					node = this.rotateLeft(node);
				}
			} else {
				// Base case - data is already in the tree, increment its count
				
				node.getValue().incrementCount();
				
			}
		}
		return node;
	}

	/**
	 * Auxiliary method for {@code valid}. Determines if a subtree based on node is
	 * a valid subtree. An AVL must meet the BST validation conditions, and
	 * additionally be balanced in all its subtrees - i.e. the difference in height
	 * between any two children must be no greater than 1.
	 *
	 * @param node The root of the subtree to test for validity.
	 * @return true if the subtree base on node is valid, false otherwise.
	 */
	@Override
	protected boolean isValidAux(final TreeNode node) {
		boolean valid = false;

		if (node == null) {
			// Base Case: bottom of tree
			valid = true;
		} else if (Math.max(this.nodeHeight(node.getLeft()), this.nodeHeight(node.getRight())) != node.getHeight()
				- 1) {
			// Base Case - height fault: current node height is not valid
			valid = false;
		} else if (node.getLeft() != null && node.getLeft().getValue().compareTo(node.getValue()) >= 0
				|| node.getRight() != null && node.getRight().getValue().compareTo(node.getValue()) <= 0) {
			// Base Case - data fault: current data not valid compared to
			// children's data
			valid = false;
		} else if (Math.abs(this.nodeHeight(node.getLeft()) - this.nodeHeight(node.getRight())) > 1) {
			// Base Case - AVL fault: child node heights are not correct
			valid = false;
		} else {
			valid = this.isValidAux(node.getLeft()) && this.isValidAux(node.getRight());
		}
		return valid;
	}

	/**
	 * Determines whether two AVLs are identical.
	 *
	 * @param target The AVL to compare this AVL against.
	 * @return true if this AVL and target contain nodes that match in position,
	 *         value, count, and height, false otherwise.
	 */
	public boolean equals(final AVL target) {
		return super.equals(target);
	}

}
