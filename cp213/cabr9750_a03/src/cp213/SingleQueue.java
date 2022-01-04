package cp213;

/**
 * A simple linked queue structure of <code>Node T</code> objects. Only the
 * <code>T</code> data contained in the queue is visible through the standard
 * queue methods. Extends the <code>SingleLink</code> class, which already
 * defines the head node, length, peek, isEmpty, and iterator.
 *
 * @author your name here
 * @author David Brown
 * @version 2020-10-16
 * @param <T> the SingleQueue data type.
 */
public class SingleQueue<T> extends SingleLink<T> {

    // Pointer to the rear of the queue.
    private SingleNode<T> rear = null;

    /**
     * Combines the contents of the left and right SingleQueues into the current SingleQueue.
     * Moves nodes only - does not move data or call the high-level methods insert
     * or remove. left and right SingleQueues are empty when done. Nodes are moved
     * alternately from left and right to this SingleQueue.
     *
     * You have two queues called left and right queues. You remove nodes from these
     * two queues to create a new queue (current queue).
     *
     * If the current queue is empty or not, it should not make a difference to you.
     * you just get nodes from the right and left queues and add them to the current
     * queue. Do not use insert and remove methods. …. Use moveFront method included
     * in the class.
     *
     * Remember to remove a node from the list you have to update the reference or
     * the pointer that is pointing to the current node.
     *
     * The getNext () and setNext() methods from SingleNode class can be used for
     * these purpose.
     *
     * Do not assume that both right and left queues are of the same length.
     *
     * @param left  The first SingleQueue to extract nodes from.
     * @param right The second SingleQueue to extract nodes from.
     */
    public void combine(final SingleQueue<T> left, final SingleQueue<T> right) {

    while(left.length > 0|| right.length > 0) {
    	if(left.length > 0) {
    		this.moveFront(left);
    	}
    	if(right.length > 0) {
    		this.moveFront(right);
    	}
    }

    }

    /**
     * Adds data to the rear of the queue. Increments the queue length.
     *
     * @param data The data to added to the rear of the queue.
     */
    public void insert(final T data) {

    if(this.length > 0) {
    	SingleNode<T> node = this.head;
    	while(node.getNext() != null) {
    		node = node.getNext();
    	}
    	node.setNext(new SingleNode<T>(data,null));
    	this.rear = node;
    	
    }else {
    	this.head = this.rear = new SingleNode<T>(data,null);
    }
    this.length++;
    }

    /**
     * Returns the front data of the queue and removes that data from the queue. The
     * next node in the queue becomes the new first node. Decrements the queue
     * length.
     *
     * @return The data at the front of the queue.
     */
    public T remove() {
    T value = this.head.getValue();
    this.head = this.head.getNext();
    if(this.length == 1) {
    	this.rear = this.head;
    }
    this.length --;
    return value;
    }

    /**
     * Splits the contents of the current SingleQueue into the left and right SingleQueues.
     * Moves nodes only - does not move data or call the high-level methods insert
     * or remove. this SingleQueue is empty when done. Nodes are moved alternately from
     * this SingleQueue to left and right.
     *
     * This is the opposite of the combine method.
     *
     * @param left  The first SingleQueue to move nodes to.
     * @param right The second SingleQueue to move nodes to.
     */
    public void split(final SingleQueue<T> left, final SingleQueue<T> right) {

    boolean alt = true;
    while(this.length > 0) {
    	if(alt) {
    		left.moveFront(this);
    	}else {
    		right.moveFront(this);
    	}
    	alt = !alt;
    }
    
    }

    /**
     * Helper method to move the front node from the SingleQueue source to the rear of this
     * SingleQueue.
     *
     * @param source SingleQueue to move node from
     */
    private void moveFront(final SingleQueue<T> source) {
	// Extract the first node of the source SingleQueue.
	final SingleNode<T> node = source.head;
	source.head = source.head.getNext();
	node.setNext(null);

	if (source.head == null) {
	    source.rear = null;
	}
	// Update this SingleQueue.
	if (this.head == null) {
	    this.head = node;
	} else {
	    this.rear.setNext(node);
	}
	this.rear = node;
	// Update the SingleQueue lengths.
	this.length++;
	source.length--;
    }
}