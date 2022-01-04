package cp213;

/**
 * Stores a character and an occurrence count for that character.
 *
 * @author David Brown
 * @version 2020-10-30
 */
public class CountedCharacter {

    // Attributes.
    private Character character = null; // data
    private int count = 0; // character count

    /**
     * Constructor for key version of object. (character count defaults to 0)
     *
     * @param character A character.
     */
    public CountedCharacter(final Character character) {
	this.character = character;
    }

    /**
     * Constructor.
     *
     * @param character A character.
     * @param count     The character count.
     */
    public CountedCharacter(final Character character, final int count) {
	this.character = character;
	this.count = count;
    }

    /**
     * Copy constructor.
     *
     * @param source Another CountedCharacter object.
     */
    public CountedCharacter(final CountedCharacter source) {
	this.character = source.character;
	this.count = source.count;
    }

    /**
     * Comparison method.
     *
     * @param target Object to compare against.
     * @return less than 0 if this character comes before target character, greater
     *         than 0 if this character comes after target character, 0 if the
     *         characters are the same.
     */
    public int compareTo(final CountedCharacter target) {
	return this.character.compareTo(target.character);
    }

    /**
     * Decrements the character count.
     */
    public void decrementCount() {
	this.count--;
    }

    /**
     * Returns this character.
     *
     * @return this character.
     */
    public Character getCharacter() {
	return this.character;
    }

    /**
     * Returns this character count.
     *
     * @return this character count.
     */
    public int getCount() {
	return this.count;
    }

    /**
     * Increments the character count.
     */
    public void incrementCount() {
	this.count++;
    }

    /**
     * Sets the character count.
     *
     * @param count the new character count.
     */
    public void setCount(final int count) {
	this.count = count;
	return;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString()
     */
    @Override
    public String toString() {
	return "{" + this.character + ": " + this.count + "}";
    }

}
