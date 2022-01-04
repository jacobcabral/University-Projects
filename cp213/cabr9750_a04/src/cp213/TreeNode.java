package cp213;

import java.util.ArrayList;

/**
 * The individual node of a linked structure that stores CountedCharacter
 * objects. This is a doubly-linked node with left and right pointers to child
 * nodes. The node link can be updated, but not the node data, in order to avoid
 * moving data between nodes. Data structures must be reordered by moving nodes.
 *
 * @author David Brown
 * @version 2020-10-30
 */
public class TreeNode {

    // Attributes
    private CountedCharacter data = null; // the node data
    private int height = 1; // the node height

    // Link to the child TreeNodes.
    private TreeNode left = null; // pointer to the left child node
    private TreeNode right = null; // pointer to the right child node

    /**
     * Creates a new TreeNode with data and null links to its child TreeNodes. Not
     * copy safe as it accepts a reference to the data rather than a copy of the
     * data.
     *
     * @param data The data to store in the node.
     */
    public TreeNode(final CountedCharacter data) {
	this.data = data;
    }

    /**
     * Performs an inorder traversal of a tree copying node data to a temporary
     * queue.
     *
     * @param node  a TreeNode
     * @param queue temporary structure to hold nodes
     */
    private final void inOrderAux(final TreeNode node, final ArrayList<CountedCharacter> queue) {
	if (node != null) {
	    this.inOrderAux(node.getLeft(), queue);
	    queue.add(new CountedCharacter(node.getValue()));
	    this.inOrderAux(node.getRight(), queue);
	}
	return;
    }

    /**
     * Returns the height of this TreeNode.
     *
     * @return this node height.
     */
    public int getHeight() {
	return this.height;
    }

    /**
     * Returns the left child of this TreeNode.
     *
     * @return this left child pointer.
     */
    public TreeNode getLeft() {
	return this.left;
    }

    /**
     * Returns the right child of this TreeNode.
     *
     * @return this right child pointer.
     */
    public TreeNode getRight() {
	return this.right;
    }

    /**
     * Returns this node data. Not copy safe as it returns a reference to the data,
     * not a copy of the data.
     *
     * @return this node data.
     */
    public CountedCharacter getValue() {
	return this.data;
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
    public final CountedCharacter[] inOrder() {
	final ArrayList<CountedCharacter> queue = new ArrayList<>();
	this.inOrderAux(this, queue);
	return queue.toArray(new CountedCharacter[queue.size()]);
    }

    /**
     * Returns an array of copies of the CountedCharacter objects in a linked data
     * structure. The array contents are in level order starting from the root
     * (this) node. Helps you to determine the structure of the tree.
     *
     * Not thread safe as it assumes contents of data structure are not changed by
     * an external thread during the copy loop. If data elements are added or
     * removed by an external thread while the data is being copied to the array,
     * then the declared array size may no longer be valid.
     *
     * @return this tree data as an array of data.
     */
    public final CountedCharacter[] levelOrder() {
	final ArrayList<CountedCharacter> values = new ArrayList<>();
	TreeNode node = this;

	if (this != null) {
	    // Put the nodes for one level into a queue.
	    final ArrayList<TreeNode> queue = new ArrayList<>();
	    queue.add(node);

	    while (queue.size() > 0) {
		// Add the node to the queue
		node = queue.remove(0);
		// Add a copy of the node data to the list of data
		values.add(new CountedCharacter(node.getValue()));

		if (node.getLeft() != null) {
		    queue.add(node.getLeft());
		}
		if (node.getRight() != null) {
		    queue.add(node.getRight());
		}
	    }
	}
	return values.toArray(new CountedCharacter[values.size()]);
    }

    /**
     * Updates the left child reference of this TreeNode to another TreeNode.
     *
     * @param left this new left child node to link to.
     */
    public void setLeft(final TreeNode left) {
	this.left = left;
    }

    /**
     * Updates the right child reference of this TreeNode to another TreeNode.
     *
     * @param right this new right child node to link to.
     */
    public void setRight(final TreeNode right) {
	this.right = right;
    }

    /**
     * @return a string version of this node including the data and height.
     */
    @Override
    public String toString() {
	return "D: " + this.data + "; H: " + this.height;
    }

    /**
     * Updates the height of this TreeNode to 1 plus the maximum heights of its two
     * child nodes. Empty child nodes are considered to have a height of 0.
     */
    public void updateHeight() {
	int leftHeight = 0;
	int rightHeight = 0;

	if (this.left != null) {
	    leftHeight = this.left.height;
	}
	if (this.right != null) {
	    rightHeight = this.right.height;
	}
	this.height = Math.max(leftHeight, rightHeight) + 1;
	return;
    }

}