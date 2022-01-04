package cp213;

/**
 * @author your name here
 * @author David Brown
 * @version 2020-10-16
 */
public class A03Test {

    /**
     * Note that not all the data structure methods are called in this main. The
     * main method is just an illustration of how you may test your code. Test your
     * code thoroughly.
     *
     * When you start, comment out all code in the main, and un-comment as you add
     * code to the class.
     *
     * @param args (unused)
     */
    public static void main(String[] args) {
	final String LINE = new String(new char[40]).replace("\0", "-");

	// Test SingleStack
	SingleStack<Integer> stack = new SingleStack<>();
	System.out.println(LINE);
	System.out.println("SingleStack");
	System.out.println("Empty: " + stack.isEmpty());
	System.out.println("Add values:");

	for (int i = 0; i < 6; i++) {
	    stack.push(i);
	}
	System.out.println("Empty: " + stack.isEmpty());
	System.out.println("Peek: " + stack.peek());
	System.out.println("Clear stack:");

	while (!stack.isEmpty()) {
	    System.out.println("Popped: " + stack.pop());
	}

	// Test SingleQueue
	SingleQueue<Integer> queue = new SingleQueue<>();
	System.out.println(LINE);
	System.out.println("SingleQueue");
	System.out.println("Empty: " + queue.isEmpty());
	System.out.println("Add values:");

	for (int i = 0; i < 6; i++) {
	    queue.insert(i);
	}
	System.out.println("Empty: " + queue.isEmpty());
	System.out.println("Peek: " + queue.peek());
	System.out.println("Split: ");
	SingleQueue<Integer> left = new SingleQueue<>();
	SingleQueue<Integer> right = new SingleQueue<>();
	queue.split(left, right);
	System.out.println("queue Empty: " + queue.isEmpty());
	System.out.println("left: ");
	// Print queue contents with iterator
	for (Integer i : left) {
	    System.out.println("  " + i);
	}
	System.out.println("right: ");

	for (Integer i : right) {
	    System.out.println("  " + i);
	}
	System.out.println("Combine: ");
	queue.combine(left, right);
	System.out.println("left Empty: " + left.isEmpty());
	System.out.println("right Empty: " + right.isEmpty());
	System.out.println("queue: ");

	for (Integer i : queue) {
	    System.out.println("  " + i);
	}
	System.out.println("Clear queue:");

	while (!queue.isEmpty()) {
	    System.out.println("Removed: " + queue.remove());
	}

	// Test SinglePriorityQueue
	SinglePriorityQueue<Integer> pq = new SinglePriorityQueue<>();
	System.out.println(LINE);
	System.out.println("SinglePriorityQueue");
	System.out.println("Empty: " + pq.isEmpty());
	System.out.println("Add values:");

	for (int i = 5; i >= 0; i--) {
	    pq.insert(i);
	}
	System.out.println("Empty: " + pq.isEmpty());
	System.out.println("Peek: " + pq.peek());
	System.out.println("Clear queue:");

	SinglePriorityQueue<Integer> lower = new SinglePriorityQueue<>();
	SinglePriorityQueue<Integer> higher = new SinglePriorityQueue<>();
	int key = 3;
	System.out.println("Split Key: " + key);
	pq.splitByKey(key, higher, lower);
	System.out.println("lower: ");

	while (!lower.isEmpty()) {
	    System.out.println("Removed: " + lower.remove());
	}
	System.out.println("higher: ");

	while (!higher.isEmpty()) {
	    System.out.println("Removed: " + higher.remove());
	}

	// Test SingleList
	SingleList<Integer> list = new SingleList<>();
	System.out.println(LINE);
	System.out.println("SingleList");
	System.out.println("Empty: " + list.isEmpty());
	System.out.println("Add values:");

	for (int i = 0; i < 6; i++) {
	    list.append(i);
	}
	System.out.println("Empty: " + list.isEmpty());
	System.out.println("Peek: " + list.peek());
	System.out.println("Clear list:");

	while (!list.isEmpty()) {
	    System.out.println("Removed: " + list.removeFront());
	}
	System.out.println(LINE);
    }

}