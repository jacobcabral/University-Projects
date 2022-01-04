package cp213;

import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Movie class definition.
 *
 * @author David Brown
 * @version 2020-10-01
 */
public class Movie implements Comparable<Movie> {

    // Constants
    public static final int FIRST_YEAR = 1888;
    public static final String[] GENRES = { "science fiction", "fantasy",
	    "drama", "romance", "comedy", "zombie", "action", "historical",
	    "horror", "war" };
    public static final int MAX_RATING = 10;
    public static final int MIN_RATING = 0;

    /**
     * Converts a string of the form "2,3,6" to an array of Integer objects, [2,
     * 3, 6]. Used when reading Movie objects from a file.
     *
     * @param string
     *            The string to convert to an array.
     * @return The array version of string.
     */
    public static Integer[] genresStringToList(final String string) {
	final ArrayList<Integer> genresList = new ArrayList<>();
	
	String[] letters = string.split(",");

    for(int i = 0; i<letters.length; i++) {
    	genresList.add(Integer.parseInt(letters[i]));
    }

	// Convert arraylist to an array of Integer.
	return genresList.toArray(new Integer[1]);
    }

    /**
     * Testing.
     *
     * @param args
     *            Unused.
     */
    public static void main(final String[] args) {
	// Movie testing
    Movie pulpFiction = new Movie("Pulp Fiction", 1998, "Quinten Taratino", 8.5, new Integer[] {6,2} );
    Movie FMJ = new Movie("Full Metal Jacket", 1987, "Stanley Kubrick", 8.5, new Integer[] {9} );
    System.out.println(pulpFiction.toString());
    System.out.println(FMJ.toString());
    System.out.println();
    System.out.println(FMJ.compareTo(pulpFiction));
    }

    /**
     * Returns a string of all genres in the Movie.GENRES list. Use for input
     * menus. Formatted as " 3: romance"
     *
     * @return the genres.
     */
    public static String menu() {

    // your code here
    String s_menu = "";
    s_menu = s_menu + 1 + ": " +GENRES[0];
    
    for(int i = 1; i<GENRES.length;i++) {
    	s_menu = s_menu + "\n" + (i+1) + ": " +GENRES[i];
    }
    return s_menu;
    }

    // Attributes
    private String director = "";
    private Integer[] genres = null;
    private double rating = 0;
    private String title = "";
    private int year = 0;

    /**
     * Instantiates a Movie object.
     *
     * @param title
     *            movie title
     * @param year
     *            year of release
     * @param director
     *            name of director
     * @param rating
     *            rating of 1 - 10 from IMDB
     * @param genres
     *            numbers representing movie genres list
     */
    public Movie(final String title, final int year, final String director,
	    final double rating, final Integer[] genres) {
    boolean isvalidgenres = true;	
    assert year >= Movie.FIRST_YEAR: String.format("Movie year must be >= %d", Movie.FIRST_YEAR);
    assert Movie.MIN_RATING <= rating && rating <= Movie.MAX_RATING:"Movie rating must be between one and ten";
    for (int j = 0;j<genres.length;j++) {
    	if(0 <= genres[j] && genres[j] <= 9) {
    		isvalidgenres = true;
    	}else {isvalidgenres = false;}
    }
    assert isvalidgenres : "Movie genres must be within the range of one and ten";
    

    this.title = title;
    this.year = year;
    this.director = director;
    this.rating = rating;
    this.genres = genres;

    }

    /*
     * (non-Javadoc) Compares this Movie against that Movie. Returns -1 if this Movie
     * comes before that Movie, 1 if this Movie comes after that Movie, and 0 if
     * the two Movies are the same.
     * 
     * Movies are compared first by title, then by year.
     *
     * @see java.lang.Comparable#compareTo(java.lang.Object)
     */
    @Override
    public int compareTo(final Movie that) {
    int result = 0;
    int titlecompare = (this.title).compareTo(that.title);
    if(titlecompare == 0) {
    	//check the dates
    	if(this.year > that.year) {
    		//that movie comes before this movie
    		result = -1;
    	}else if (this.year < that.year) {
    		result = 1;
    	} else {
    		result = 0;
    	}
    	
    }else if(titlecompare > 0) {
    	//greater than zero this > that
    	result = -1;
    }else if(titlecompare < 0) {
    	// that < this
    	result = 1;
    }
    return result;
    }

    /**
     * Converts a list of genre integers to a string of genre names.
     *
     * @return comma delimited string of genre names based upon the current
     *         movie object's integer genres list. e.g.: [0, 2] returns "science
     *         fiction, drama"
     */
    public String genresListToNames() {

    String result = "";
    for(int i = 0; i < this.genres.length;i++) {
     result = result + Movie.GENRES[this.genres[i]] + ",";
    }
    result = result.substring(0, result.length() - 1);
    return result;
    }

    /**
     * Director getter.
     *
     * @return the director
     */
    public String getDirector() {
	return this.director;
    }

    /**
     * Genres getter.
     *
     * @return the genres list
     */
    public Integer[] getGenres() {
	return this.genres;
    }

    /**
     * Rating getter.
     *
     * @return the rating
     */
    public double getRating() {
	return this.rating;
    }

    /**
     * Title getter.
     *
     * @return the title
     */
    public String getTitle() {
	return this.title;
    }

    /**
     * Year getter.
     *
     * @return the year
     */
    public int getYear() {
	return this.year;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#hashCode()
     */
    @Override
    public int hashCode() {
	int hash = 0;

	for (int i = 0; i < this.title.length(); i++) {
	    hash += this.title.charAt(i);
	}
	hash *= this.year;
	return hash;
    }

    /**
     * Creates a formatted string of Movie key data in the format "title, year".
     * Ex: "Zulu, 1964".
     *
     * @return a Movie key as a string
     */
    public String key() {
	return String.format("%s, %d", this.title, this.year);
    }

    /**
     * Director setter.
     *
     * @param director
     *            the new director value
     */
    public void setDirector(final String director) {
	this.director = director;
    }

    /**
     * Genres setter.
     *
     * @param genres
     *            the new list of numeric genres
     */
    public void setGenres(final Integer[] genres) {
	this.genres = genres;
    }

    /**
     * Rating setter.
     *
     * @param rating
     *            the new rating
     */
    public void setRating(final double rating) {
	this.rating = rating;
    }

    /**
     * Title setter.
     *
     * @param title
     *            the new title
     */
    public void setTitle(final String title) {
	this.title = title;
    }

    /**
     * Year setter.
     *
     * @param year
     *            the new year
     */
    public void setYear(final int year) {
	this.year = year;
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Object#toString() Creates a formatted string of movie
     * data.
     */
    @Override
    public String toString() {

    String formatted = "Title:    "+ this.title + "\nYear:     "+ this.year + "\nDirector: " + this.director + "\nRating:   " + this.rating + "\nGenres:   " + this.genresListToNames();
    return formatted;
    }

    /**
     * Writes a single line of movie data to an open file in the format
     * title|year|director|rating|codes
     *
     * @param ps
     *            output printstream
     */
    public void write(final PrintStream ps) {
    
    String s_write = "";
    s_write = s_write + this.title + "|" + this.year + "|" + this.director + "|" + this.rating + "|" + this.genres;
    ps.println(s_write);
    }

    /**
     * Converts a genres list of the form [2,3,7] to a string "2,3,7" for
     * writing Movie data to a file.
     *
     * @return the genres list string
     */
    private String genresListToString() {
    String result = "";
    for(int i = 0; i<this.genres.length;i++) {
		result += this.genres[i] + ",";
	}
    result = result.substring(0, result.length() - 1);
    return result;
    }

}
