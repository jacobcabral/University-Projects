package cp213;

/**
 * A simple linked list structure of <code>Node T</code> objects. Only the
 * <code>T</code> data contained in the stack is visible through the standard
 * list methods. Extends the <code>SingleLink</code> class, which already
 * defines the head node, length, iterator, and toArray.
 *
 * @author David Brown
 * @version 2020-10-16
 * @param <T> this SingleList data type.
 */
public class SingleList<T extends Comparable<T>> extends SingleLink<T> {

	 private SingleNode<T> rear = null;

	/**
     * Searches for the first occurrence of key in this SingleList. Private helper methods
     * - used only by other ADT methods.
     *
     * @param key The value to look for.
     * @return A pointer to the node previous to the node containing key.
     */
    private SingleNode<T> linearSearch(final T key) {

    	 SingleNode<T> current = this.head;
         
         while (current != null && current.getValue() != key) {                    
             current = current.getNext();      
         }
                     
         return(current);
    }
    private SingleNode<T> prevLinearSearch(final T key) {

        SingleNode<T> current = this.head;
        SingleNode<T> previous = null;
                
        while (current != null && current.getValue() != key) {                    
            previous = current;
            current = current.getNext();     
        }
                    
        return(previous);
    }

    /**
     * A helper method to move the front node of the SingleList source to this SingleList.
     *
     * @param source The list to move the front of.
     */
    private void moveFront(final SingleList<T> source) {

    SingleNode<T> current = this.head;
    this.head = this.head.getNext();
    current.setNext(source.head);
    source.head = current;
    
    }

    /**
     * Appends data to the end of this SingleList.
     *
     * @param data The data to append.
     */
    public void append(final T data) {
    	SingleNode<T> current = this.head;
        SingleNode<T> previous = null;
        
        if (this.head == null) {
            this.head = new SingleNode<T>(data, null);
        } else {
            while (current.getNext() != null) {
                previous = current;
                current = current.getNext();
            }
            current.setNext(new SingleNode<T>(data, null));
            this.length++;
        }

    }

    /**
     * Removes duplicates from this SingleList. The list contains one and only one of each
     * value formerly present in this SingleList. The first occurrence of each value is
     * preserved.
     */
    public void clean() {

//    SingleNode<T> current = this.head;
//    while(current != null) {
//    	SingleNode<T> runner = current;
//    	while(runner.getNext()!= null) {
//    		if(runner.getValue() == current.getValue())
//    			runner.setNext(runner.getNext().getNext());
//    		else
//    			runner = runner.getNext();
//    	}
//    	current = current.getNext();
//    }
    	
    SingleNode<T> current = this.head;
    SingleNode<T> ptr = null;
    SingleNode<T> dup = null;
    while(current != null && current.getNext() != null) {
    	ptr = current;
    	while(ptr.getNext() != null) {
    		if(current.getValue().compareTo(ptr.getNext().getValue()) == 0) {
    			dup = ptr.getNext();
    			ptr.setNext(ptr.getNext().getNext());
    			
    		}else {
    			ptr = ptr.getNext();
    		}
    	}
    	current = current.getNext();
    }

    }

    /**
     * Combines contents of two lists into a third. Values are alternated from the
     * origin lists into this SingleList. The origin lists are empty when finished. NOTE:
     * data must not be moved, only nodes.
     *
     * @param left  The first list to combine with this SingleList.
     * @param right The second list to combine with this SingleList.
     */
    public void combine(final SingleList<T> left, final SingleList<T> right) {

    boolean alt = true;
    while(left.length > 0 || right.length > 0) {
    	if(alt == true && left.length > 0)
    		this.moveFront(left);
    	else if(alt == false && right.length > 0){
    		this.moveFront(right);
    	}
    	alt = !alt;
    }

    }

    /**
     * Determines if this SingleList contains key.
     *
     * @param key The key value to look for.
     * @return true if key is in this SingleList, false otherwise.
     */
    public boolean contains(final T key) {

    boolean found = false;
    SingleNode<T> node = this.linearSearch(key);
    if (node.getValue() == key) {
    	found = true;
    }
    return found;
    }

    /**
     * Finds the number of times key appears in list.
     *
     * @param key The value to look for.
     * @return The number of times key appears in this SingleList.
     */
    public int count(final T key) {
	int n = 0;
	SingleNode<T> current = this.head;

	while (current != null) {
	    if (current.getValue().compareTo(key) == 0) {
		n++;
	    }
	    current = current.getNext();
	}
	return n;
    }

    /**
     * Finds and returns the value in list that matches key.
     *
     * @param key The value to search for.
     * @return The value that matches key, null otherwise.
     */
    public T find(final T key) {
	T data = null;

	if (this.length > 0) {
	    final SingleNode<T> previous = this.linearSearch(key);

	    if (previous == null) {
		// data at front
		data = this.head.getValue();
	    } else if (previous.getNext() != null) {
		data = previous.getNext().getValue();
	    }
	}
	return data;
    }

    /**
     * Get the nth item in this SingleList.
     *
     * @param n The index of the item to return.
     * @return The nth item in this SingleList.
     * @throws ArrayIndexOutOfBoundsException if n is not a valid index.
     */
    public T get(final int n) throws ArrayIndexOutOfBoundsException {

    SingleNode<T> runner = this.head;
    int count = 0;
    while(count != n) {
    	runner = runner.getNext();
    	count++;
    }
    return runner.getValue();
    }
    
    /**
     * Determines whether two lists are identical.
     *
     * @param source The list to compare against this SingleList.
     * @return true if this SingleList contains the same values in the same order as source,
     *         false otherwise.
     */
    public boolean identical(final SingleList<T> source) {

    boolean identical = false;
    identical = this.length == source.length;
    SingleNode<T> curr1 = this.head;
    SingleNode<T> curr2 = source.head;
    while (identical == true && curr1 != null) {
    	identical = curr1.getValue() == curr2.getValue();
    	curr1 = curr1.getNext();
    	curr2 = curr2.getNext();
    	
    }
    return identical;
    }

    /**
     * Finds the first location of a value by key in this SingleList.
     *
     * @param key The value to search for.
     * @return The index of key in this SingleList, -1 otherwise.
     */
    public int index(final T key) {
    	SingleNode<T> current = this.head;
        int index = 0;
                
        while (current != null && current.getValue() != key) {                    
            current = current.getNext();
            index += 1;          
        }
        
        if (current == null) {
            index = this.length - 1;
        }
                    
        return(index);
    }

    /**
     * Inserts data into this SingleList at index i. If i greater than the length of this
     * SingleList, append value to the end of this SingleList.
     *
     * @param i    The index to insert the new value at.
     * @param data The new value to insert into this SingleList.
     */
    public void insert(int i, final T data) {

    if(i >= this.length)
    	this.append(data);
    else {
    	if (i < 0) {
    		i = this.length - Math.abs(i);
    	}
    	int j = 0;
    	SingleNode<T> prev = null;
    	SingleNode<T> curr = this.head;
    	while(j<i) {
    		prev = curr;
    		curr = curr.getNext();
    		j++;
    	}
    	SingleNode<T> NewNode = new SingleNode<T>(data, curr);
    	prev.setNext(NewNode);
    	this.length += 1;
    }

    }

    /**
     * Inserts data into the front of this SingleList.
     *
     * @param data The value to insert into the front of this SingleList.
     */
    public void insertFront(final T data) {

    SingleNode<T> current = this.head;
    if(this.length > 0)
    	this.head = new SingleNode<T>(data,this.head);
    else
    	while(current.getNext()!=null) {
    		current = current.getNext();
    	}
    	this.head = current = new SingleNode<T>(data,null);

    }

    /**
     * Finds the maximum value in this SingleList.
     *
     * @return The maximum value.
     */
    public T max() {

    SingleNode<T> pointer = this.head;
    T maximum = pointer.getValue();
    
    while(pointer.getNext() != null) {
    	pointer = pointer.getNext();
    	if (pointer.getValue().compareTo(maximum) > 0) {
    		maximum = pointer.getValue();
    	}
    }
    return maximum;
    }

    /**
     * Finds the minimum value in this SingleList.
     *
     * @return The minimum value.
     */
    public T min() {

    	SingleNode<T> pointer = this.head;
        T maximum = pointer.getValue();
        
        while(pointer.getNext() != null) {
        	pointer = pointer.getNext();
        	if (pointer.getValue().compareTo(maximum) < 0) {
        		maximum = pointer.getValue();
        	}
        }
        return maximum;

    }

    /**
     * Finds, removes, and returns the value in this SingleList that matches key.
     *
     * @param key The value to search for.
     * @return The value matching key, null otherwise.
     */
    public T remove(final T key) {
    	SingleNode<T> current = this.linearSearch(key);
        SingleNode<T> previous = this.prevLinearSearch(key);
        int index = this.index(key);

        T value = null;

        if (current != null && this.length == 1) {

            value = current.getValue();

            this.head = null;
            this.rear = null;
            this.length = 0;

        } else if (current != null && this.length > 1) {

            if (index == 0) {

                value = current.getValue();
                this.head = this.head.getNext();

                current = this.head;
                previous = this.head;

                this.length--;

            } else if (index == this.length - 1) {

                int i = 0;

                value = current.getValue();
                this.rear = previous;

                current = previous;
                current.setNext(null);

                this.length -= 1;
                previous = this.head;

                while (i != this.length - 2) {
                    i++;
                    previous = previous.getNext();
                }

            } else {

                value = current.getValue();
                previous.setNext(current.getNext());
                current = current.getNext();
                this.length--;
            }
        }

        return(value);
    }

    /**
     * Removes the value at the front of this SingleList.
     *
     * @return The value at the front of this SingleList.
     */
    public T removeFront() {

    	T value = this.head.getValue();
        
        if (this.head.getNext() != null) {
            this.head = this.head.getNext();
        } else {
            this.head = null;
        }
            
        this.length--;
        
        return value;
    }

    /**
     * Reverses the order of the values in this SingleList.
     */
    public void reverse() {
	SingleNode<T> newHead = null;
	SingleNode<T> temp = null;

	while (this.head != null) {
	    temp = this.head.getNext();
	    this.head.setNext(newHead);
	    newHead = this.head;
	    this.head = temp;
	}
	this.head = newHead;
	return;
    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists. Moves nodes
     * only - does not move data or call the high-level methods insert or remove.
     * this SingleList is empty when done. The first half of this SingleList is moved to left,
     * and the last half of this SingleList is moved to right. If the resulting lengths
     * are not the same, left should have one more item than right.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void split(final SingleList<T> left, final SingleList<T> right) {

    int half = this.length / 2;
    while(this.length > half)
    	left.moveFront(this);
    while(this.length > 0)
    	right.moveFront(this);

    }

    /**
     * Splits the contents of this SingleList into the left and right SingleLists. Moves nodes
     * only - does not move data or call the high-level methods insert or remove.
     * this SingleList is empty when done. Nodes are moved alternately from this SingleList to
     * left and right.
     *
     * @param left  The first SingleList to move nodes to.
     * @param right The second SingleList to move nodes to.
     */
    public void splitAlternate(final SingleList<T> left, final SingleList<T> right) {

    boolean alt = true;
    while(this.head != null) {
    	if(alt) {
    		left.moveFront(this);
    	}else {
    		right.moveFront(this);
    	}
    	alt = !alt;
    }
    	
    
    }

    /**
     * Creates a union of two other SingleLists into this SingleList. Copies data to this list.
     * left and right SingleLists are unchanged.
     *
     * @param left  The first SingleList to create a union from.
     * @param right The second SingleList to create a union from.
     */
    public void union(final SingleList<T> left, final SingleList<T> right) {

    SingleNode<T> node = this.head;
    while(node != null) {
    	if(this.index(node.getValue()) == -1) {
    		this.append(node.getValue());
    	}
    node = node.getNext();
    }
    
    node = right.head;
    while(node != null) {
    	if(this.index(node.getValue()) == -1) {
    		this.append(node.getValue());
    	}
    node = node.getNext();
    }
    }
}