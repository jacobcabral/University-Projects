package cp213;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Main method and table generation methods for Assignment 4.
 *
 * @author your name here
 * @author David Brown
 * @version 2020-10-30
 */
public class A04 {

    public static final NumberFormat NF = NumberFormat.getInstance();
    public static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public static final String POPULAR = "ETAOINSHRDLUCMPFYWGBVKJXZQ";
    public static final String SPLIT = "MFTCJPWADHKNRUYBEIGLOQSVXZ";
    public static final String SEPARATOR = "------------------------------";

    public static final String[] STRING_DATA = new String[] { ALPHABET, SPLIT, POPULAR };
    public static final String FILENAME = "./decline.txt" ; // "miserables.txt";

    /**
     * Print a formatted table of character counts and percentages in the format:
     *
     * <pre>
     * Character Table for Comparisons File
     *
     * Char    Count Percent
     *    A  206,946    8.17
     *    B   37,498    1.48
     *    ...
     * </pre>
     *
     * Note: your data may not match this as it is file dependent.
     *
     * @param tree The BST to generate the table from.
     */
    private static void characterTable(final BST tree) {

	final CountedCharacter[] array = tree.inOrder();
	int totalCount = 0;

	for (final CountedCharacter value : array) {
	    totalCount += value.getCount();
	}
	System.out.println("Char    Count Percent");

	for (final CountedCharacter value : array) {
	    final int count = value.getCount();
	    final double percent = (double) value.getCount() / totalCount * 100;
	    System.out.format("%4s %,8d %7.2f%n", value.getCharacter(), count, percent);
	}
	return;
    }

    /**
     * Fill a tree by inserting all letters from a string into the tree. Letters
     * must be converted to upper-case. Non-letters are ignored. The order that
     * letters are inserted into the tree determine its shape.
     *
     * @param tree   The BST/AVL/PopularityTree to fill.
     * @param string The string to read into the tree.
     */
    private static void fillTree(final BST tree, final String string) {

	for (final char letter : string.toCharArray()) {
	    final CountedCharacter data = new CountedCharacter(Character.toUpperCase(letter));
	    tree.insert(data);
	}
	return;
    }

    /**
     * Determine the number of comparisons to retrieve the contents of a file from a
     * tree. Attempt to retrieve every letter in the file from tree. All letters
     * must be converted to upper case.
     *
     * @param tree The BST to process.
     * @param file The file to process.
     * @return The number of comparisons necessary to find every letter in file in
     *         tree.
     * @throws FileNotFoundException Thrown if file not found.
     */
    private static int retrieve(final BST tree, final File file) throws FileNotFoundException {
	final Scanner fileScan = new Scanner(file);

	while (fileScan.hasNextLine()) {
	    final String line = fileScan.nextLine();

	    for (final Character c : line.toCharArray()) {

		if (Character.isLetter(c)) {
		    final CountedCharacter key = new CountedCharacter(Character.toUpperCase(c));
		    tree.retrieve(key);
		}
	    }
	}
	fileScan.close();
	return tree.getComparisons();
    }

    /**
     * Program for Assignment 4.
     *
     * @param args unused
     * @throws IOException If error on files.
     */
    public static void main(final String[] args) throws IOException {
	final File comparisonsFile = new File(FILENAME);

	for (final String string : STRING_DATA) {
	    int minComparisons = Integer.MAX_VALUE;
	    String treeType = null;
	    String minTree = null;
	    System.out.println("Data String: " + string);
	    System.out.println();
	    final ArrayList<BST> trees = new ArrayList<>();
	    trees.add(new BST());
	    trees.add(new PopularityTree());
	    trees.add(new AVL());

	    for (final BST tree : trees) {
		treeType = tree.getClass().getSimpleName();
		System.out.println("  Tree Type: " + treeType);
		A04.fillTree(tree, string);
		final int comparisons = A04.retrieve(tree, comparisonsFile);
		System.out.println("  Height: " + tree.getHeight());
		System.out.println("  Comparisons: " + NF.format(comparisons));

		if (comparisons < minComparisons) {
		    minComparisons = comparisons;
		    minTree = treeType;
		}
		System.out.println();
	    }
	    System.out.println("Tree with minimum comparisons: " + minTree);
	    System.out.println(SEPARATOR);
	}
	final PopularityTree bst = new PopularityTree();
	A04.fillTree(bst, ALPHABET);
	A04.retrieve(bst, comparisonsFile);
	System.out.println("Character Table for Comparisons File");
	System.out.println();
	A04.characterTable(bst);
    }
}
