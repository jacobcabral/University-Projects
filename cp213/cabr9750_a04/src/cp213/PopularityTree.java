package cp213;

/**
 * Implements a Popularity Tree. Extends BST.
 *
 * @author your name here
 * @author David Brown
 * @version 2020-10-30
 */
public class PopularityTree extends BST {

	/**
	 * Auxiliary method for {@code valid}. May force node rotation if the retrieval
	 * count of the located node value is incremented.
	 *
	 * @param node The node to examine for key.
	 * @param key  The value to search for. Count is updated to count in matching
	 *             node value if key is found.
	 * @return the updated node.
	 */
	private TreeNode retrieveAux(TreeNode node, final CountedCharacter key) {

		if (node == null) 
		{
			return null;
		} 
		else 
		{
			// Compare the node data against the retrieve data.
			final int result = node.getValue().compareTo(key);
			this.comparisons++;

			if (result > 0) 
			{
				// General case - check the left subtree.
				node.setLeft(this.retrieveAux(node.getLeft(), key));

				if (node.getLeft() != null && node.getValue().getCount() < node.getLeft().getValue().getCount()) 
				{
					node = this.rotateRight(node);
				}
			} 
			else if (result < 0) 
			{
				// General case - check the right subtree.
				node.setRight(this.retrieveAux(node.getRight(), key));

				if (node.getRight() != null && node.getValue().getCount() < node.getRight().getValue().getCount()) 
				{
					node = this.rotateLeft(node);
				}
			} 
			else 
			{
				// Base case - data is in the Popularity Tree.
				node.getValue().incrementCount();
				key.setCount(node.getValue().getCount());
			}
		}
		return node;
	}

	/**
	 * Performs a left rotation around node.
	 *
	 * @param parent The subtree to rotate.
	 * @return The new root of the subtree.
	 */
	private TreeNode rotateLeft(final TreeNode parent) {
		// Rearrange the nodes.
		final TreeNode temp = parent.getRight();
		parent.setRight(temp.getLeft());
		temp.setLeft(parent);
		// Update the node heights.
		parent.updateHeight();
		temp.updateHeight();
		// Return new root.
		return temp;
	}

	/**
	 * Performs a right rotation around {@code node}.
	 *
	 * @param parent The subtree to rotate.
	 * @return The new root of the subtree.
	 */
	private TreeNode rotateRight(final TreeNode parent) {
		// Rearrange the nodes.
		final TreeNode temp = parent.getLeft();
		parent.setLeft(temp.getRight());
		temp.setRight(parent);
		// Update the node heights.
		parent.updateHeight();
		// Return new root.
		return temp;
	}

	/**
	 * Replaces BST {@code insertAux} - does not increment count on repeated
	 * insertion. Counts are incremented only on retrieve.
	 */
	@Override
	protected TreeNode insertAux(TreeNode node, final CountedCharacter data) {

		if (node == null) {
			// Base case - add a new node containing the data.
			
			TreeNode new_node = new TreeNode(data);
			node = new_node;
			
			this.size++;
		} else {
			// Compare the node data against the insert data.
			final int result = node.getValue().compareTo(data);

			if (result > 0) {
				// General case - check the left subtree.
				node.setLeft(this.insertAux(node.getLeft(), data));
			} else if (result < 0) {
				// General case - check the right subtree.
				node.setRight(this.insertAux(node.getRight(), data));
			}
		}
		node.updateHeight();
		return node;
	}

	/**
	 * Auxiliary method for {@code valid}. Determines if a subtree based on node is
	 * a valid subtree. An Popularity Tree must meet the BST validation conditions,
	 * and additionally the counts of any node data must be greater than or equal to
	 * the counts of its children.
	 *
	 * @param node The root of the subtree to test for validity.
	 * @return true if the subtree base on node is valid, false otherwise.
	 */
	@Override
	protected boolean isValidAux(final TreeNode node) {
		boolean valid = false;

		if (node == null) {
			// Base case: bottom of tree
			
			valid = true;
			

		} else if (Math.max(this.nodeHeight(node.getLeft()), this.nodeHeight(node.getRight())) != node.getHeight()
				- 1) {
			// Base case - height fault: current node height is not valid
			valid = false;
		} else if (node.getLeft() != null && node.getLeft().getValue().compareTo(node.getValue()) >= 0
				|| node.getRight() != null && node.getRight().getValue().compareTo(node.getValue()) <= 0) {
			// Base case - data fault: current data not valid compared to
			// children's data
			valid = false;
		} else if (node.getLeft() != null && node.getValue().getCount() < node.getLeft().getValue().getCount()
				|| node.getRight() != null && node.getValue().getCount() < node.getRight().getValue().getCount()) {
			// Base Case - count fault: count of node must be greater or equal
			// to counts of children.
		} else {
			valid = this.isValidAux(node.getLeft()) && this.isValidAux(node.getRight());
		}
		return valid;
	}

	/**
	 * Very similar to the BST retrieve, but increments the character count here
	 * instead of in the insertion.
	 *
	 * @param key The key to search for.
	 */
	@Override
	public CountedCharacter retrieve(CountedCharacter key) {
		this.root = this.retrieveAux(this.root, key);

		if (key.getCount() == 0) {
			key = null;
		} else {
			key = new CountedCharacter(key);
		}
		return key;
	}

	/**
	 * Determines whether two PopularityTrees are identical.
	 *
	 * @param target The PopularityTree to compare this PopularityTree against.
	 * @return true if this PopularityTree and target contain nodes that match in
	 *         position, value, count, and height, false otherwise.
	 */
	public boolean equals(final PopularityTree target) {
		return super.equals(target);
	}

}
