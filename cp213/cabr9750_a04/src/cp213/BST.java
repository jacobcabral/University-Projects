package cp213;

/**
 * Implements a Binary Search Tree.
 *
 * @author your name here
 * @author David Brown
 * @version 2020-10-30
 */
public class BST {
	protected int comparisons = 0; // Count of comparisons performed by tree.

	// Attributes.
	protected TreeNode root = null; // Root node of the tree.
	protected int size = 0; // Number of elements in the tree.

	/**
	 * Auxiliary method for {@code equals}. Determines whether two subtrees are
	 * identical in data and height.
	 *
	 * @param source Node of this BST.
	 * @param target Node of that BST.
	 * @return true if source and target are identical in data and height.
	 */
	protected boolean equalsAux(final TreeNode source, final TreeNode target) {
		boolean isEqual = false;

		if (source == null && target == null) 
		{
			// Reached a bottom of the tree.
			
			isEqual = true; 
			
		} 
		else if (source != null && target != null && source.getValue().compareTo(target.getValue()) == 0
				&& source.getHeight() == target.getHeight()
				&& source.getValue().getCount() == target.getValue().getCount()) 
		{
			isEqual = this.equalsAux(source.getLeft(), target.getLeft())
					&& this.equalsAux(source.getRight(), target.getRight());
		} 
		else 
		{
			isEqual = false;
		}
		return isEqual;
	}

	/**
	 * Auxiliary method for {@code insert}. Inserts data into this BST.
	 *
	 * @param node the current node (TreeNode)
	 * @param data data to be inserted into the node
	 * @return the inserted node.
	 */
	protected TreeNode insertAux(TreeNode node, final CountedCharacter data) 
	{

		if (node == null) {
			// Base case - add a new node containing the data.
		    TreeNode new_node = new TreeNode(data);
		    node = new_node;
			 
			this.size++;
		} 
		else 
		{
			// Compare the node data against the insert data.
			final int result = node.getValue().compareTo(data);

			if (result > 0) 
			{
				// General case - check the left subtree.
				node.setLeft(this.insertAux(node.getLeft(), data));
			} 
			else if (result < 0) 
			{
				// General case - check the right subtree.
				node.setRight(this.insertAux(node.getRight(), data));
			} 
			else 
			{
				// Base case - data is already in the tree, increment its count
				node.getValue().incrementCount();
				
			}
		}
		node.updateHeight();
		return node;
	}

	/**
	 * Auxiliary method for {@code valid}. Determines if a subtree based on node is
	 * a valid subtree.
	 *
	 * @param node The root of the subtree to test for validity.
	 * @return true if the subtree base on node is valid, false otherwise.
	 */
	protected boolean isValidAux(final TreeNode node) {
		boolean valid = false;

		if (node == null) {
			// Base case: bottom of tree
			valid = true;
		} 
		else if (Math.max(this.nodeHeight(node.getLeft()), this.nodeHeight(node.getRight())) != node.getHeight()
				- 1) 
		{
			// Base case - height fault: current node height is not valid
			valid = false;
		}
		else if (node.getLeft() != null && node.getLeft().getValue().compareTo(node.getValue()) >= 0
				|| node.getRight() != null && node.getRight().getValue().compareTo(node.getValue()) <= 0) 
		{
			// Base case - data fault: current data not valid compared to children's data
			valid = false;
		}
		else 
		{
			// Check validity of children
			valid = this.isValidAux(node.getLeft()) && this.isValidAux(node.getRight());
		}
		return valid;
	}

	/**
	 * Returns the height of a given TreeNode.
	 *
	 * @param node The TreeNode to determine the height of.
	 * @return The value of the height attribute of node, 0 if node is null.
	 */
	protected int nodeHeight(final TreeNode node) {
		int height = 0;

		if (node != null) {
			height = node.getHeight();
		}
		return height;
	}

	/**
	 * Determines if this BST contains key.
	 *
	 * @param key The key to search for.
	 * @return true if this BST contains key, false otherwise.
	 */
	public boolean contains(final CountedCharacter key) {
		return this.retrieve(key) != null;
	}
 
	/**
	 * Determines whether two BSTs are identical.
	 *
	 * @param target The BST to compare this BST against.
	 * @return true if this BST and that BST contain nodes that match in position,
	 *         value, count, and height, false otherwise.
	 */
	public boolean equals(final BST target) {
		boolean isEqual = false;
		
		isEqual = equalsAux(this.root,target.root);
		
		return isEqual;
	}
	
	/**
	 * Get number of comparisons executed by the {@code retrieve} method.
	 *
	 * @return comparisons
	 */
	public int getComparisons() {
		return this.comparisons;
	}

	/**
	 * Returns the height of the root node of this BST.
	 *
	 * @return height of root node, 0 if the root node is null.
	 */
	public int getHeight() {
		int height = 0;

		if (this.root != null) {
			height = this.root.getHeight();
		}
		return height;
	}

	/**
	 * Returns the number of nodes in the BST.
	 *
	 * @return number of node in this BST.
	 */
	public int getSize() {
		return this.size;
	}

	/**
	 * Returns an array of copies of CountedCharacter objects in a linked data
	 * structure. The array contents are in data order from smallest to largest.
	 *
	 * Not thread safe as it assumes contents of data structure are not changed by
	 * an external thread during the copy loop. If data elements are added or
	 * removed by an external thread while the data is being copied to the array,
	 * then the declared array size may no longer be valid.
	 *
	 * @return this tree data as an array of data.
	 */
	public CountedCharacter[] inOrder() {
		return this.root.inOrder();
	}

	/**
	 * Inserts data into this BST.
	 *
	 * @param data Data to store.
	 */
	public void insert(final CountedCharacter data) {
		this.root = this.insertAux(this.root, data);
		return;
	}

	/**
	 * Determines if this BST is empty.
	 *
	 * @return true if this BST is empty, false otherwise.
	 */
	public boolean isEmpty() {
		return this.root == null;
	}

	/**
	 * Determines if this BST is a valid BST; i.e. a node's left child data is
	 * smaller than its data, and its right child data is greater than its data, and
	 * a node's height is equal to the maximum of the heights of its two children
	 * (empty child nodes have a height of 0), plus 1.
	 *
	 * @return true if this BST is a valid BST, false otherwise.
	 */
	public boolean isValid() {
		return this.isValidAux(this.root);
	}

	/**
	 * Returns an array of copies of CountedCharacter objects int a linked data
	 * structure. The array contents are in level order starting from the root
	 * (this) node. Helps determine the structure of the tree.
	 *
	 * Not thread safe as it assumes contents of data structure are not changed by
	 * an external thread during the copy loop. If data elements are added or
	 * removed by an external thread while the data is being copied to the array,
	 * then the declared array size may no longer be valid.
	 *
	 * @return this tree data as an array of data.
	 */
	public CountedCharacter[] levelOrder() {
		return this.root.levelOrder();
	}

	/**
	 * Resets the comparison count to 0.
	 */
	public void resetComparisons() {
		this.comparisons = 0;
		return;
	}

	/**
	 * Retrieves a copy of data matching key character (key should have character
	 * count of 0). Returning a complete CountedCharacter gives access to the
	 * character and count.
	 *
	 * @param key The key to look for.
	 * @return data The complete CountedCharacter that matches key, null otherwise.
	 */
	public CountedCharacter retrieve(final CountedCharacter key) {
		TreeNode node = this.root;
		CountedCharacter data = null;

		while (node != null && data == null) {
			// Compare the node data against the key.
			final int result = node.getValue().compareTo(key);
			// Increment the tree comparisons.
			this.comparisons++;

			if (result > 0) 
			{
				// Search the left side.
				node = node.getLeft();
			} 
			else if (result < 0) 
			{
				
				// Search the right side.
				
				// complete code here 
				
				node = node.getRight();
			} 
			else 
			{
				
				// Data matching key found.
				
				data = node.getValue(); 
			}
		}
		return data;
	}
}
