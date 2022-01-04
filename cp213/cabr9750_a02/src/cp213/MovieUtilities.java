package cp213;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.io.PrintStream;

/**
 * Utilities for working with Movie objects.
 *
 * @author David Brown
 * @version 2020-10-01
 */
public class MovieUtilities {

    /**
     * Counts the number of movies in each genre given in Movie.GENRES.
     *
     * @param movies
     *            list of movies
     * @return
     */
    public static int[] genreCounts(final ArrayList<Movie> movies) {

    int[] i_gcount = new int[10];
    int i_scifi = 0, i_fantasy = 0,i_comedy = 0,i_war = 0, i_drama = 0,i_romance = 0,i_zombie = 0,i_action = 0,i_historical = 0,i_horror = 0;
    
    for(Movie movie: movies) {
    	Integer[] i_genres = movie.getGenres();
    	for(int i = 0; i<i_genres.length;i++) {
    	switch(i_genres[i]) {
    	case 0:
    		i_scifi++;
    		break;
    	case 1:
    		i_fantasy++;
    		break;
    	case 2:
    		i_drama++;
    		break;
    	case 3:
    		i_romance++;
    		break;
    	case 4:
    		i_comedy++;
    		break;
    	case 5:
    		i_zombie++;
    		break;
    	case 6:
    		i_action++;
    		break;
    	case 7:
    		i_historical++;
    		break;
    	case 8:
    		i_horror++;
    		break;
    	case 9:
    		i_war++;
    		break;
    		}
    	}
    }
    i_gcount[0] = i_scifi;
    i_gcount[1] = i_fantasy;
    i_gcount[2] = i_drama;
    i_gcount[3] = i_romance;
    i_gcount[4] = i_comedy;
    i_gcount[5] = i_zombie;
    i_gcount[6] = i_action;
    i_gcount[7] = i_historical;
    i_gcount[8] = i_horror;
    i_gcount[9] = i_war;
    
    return i_gcount;

    }

    /**
     * Creates a Movie object by requesting data from a user.
     *
     * @param keyboard
     *            a keyboard Scanner
     * @return a Movie object
     */
    public static Movie getMovie(final Scanner keyboard) {
    int year;
    double rating;
    System.out.println("Enter the title for your movie: ");
    String title = keyboard.nextLine();
    System.out.println("Enter the Director's name: ");
    String director = keyboard.nextLine();
    System.out.println("Please enter the codes for genres, a number from one to ten seperated by commas");
    System.out.println(Movie.menu());
    String s_genre = keyboard.nextLine();
    Integer[] genrelist = Movie.genresStringToList(s_genre);
    do {
	    System.out.println("Please enter the year of the movie, must be larger than 1888: ");
	    while (!keyboard.hasNextInt()) {
	        System.out.println("That's not a year");
	        keyboard.next(); // this is important!
	    }
	    year = keyboard.nextInt();
	} while (year <= 1888);
    
    do {
	    System.out.println("Please enter the movie's rating between 0 and 10");
	    while (!keyboard.hasNextDouble()) {
	        System.out.println("That's not a number!");
	        keyboard.next(); // this is important!
	    }
	    rating = keyboard.nextDouble();
	} while (rating <= 0 && rating <= 10);
    
    Movie movie = new Movie(title,year,director,rating,genrelist);
    return movie;
    }

    /**
     * Creates a list of Movies whose list of genres include genre.
     *
     * @param movies
     *            list of movies
     * @param genre
     *            genre to compare against
     * @return list of movies for genre
     */
    public static ArrayList<Movie> getByGenre(final ArrayList<Movie> movies,
	    final int genre) {
	final ArrayList<Movie> gMovies = new ArrayList<>();

    for(Movie movie: movies) {
    	Integer [] i_genrelist = movie.getGenres();
    	for(int i = 0; i<i_genrelist.length;i++) {
    		if(i_genrelist[i] == genre) {
    			gMovies.add(movie);
    			
    		}
    	}
    }

	return gMovies;
    }

    /**
     * Creates a list of Movies whose list of genres include all the genre codes
     * in genres.
     *
     * @param movies
     *            list of movies
     * @param genres
     *            genres list to compare against
     * @return list of movies for genres
     */
    public static ArrayList<Movie> getByGenres(final ArrayList<Movie> movies,
	    final Integer[] genres) {
	final ArrayList<Movie> gMovies = new ArrayList<>();
	boolean found;
    for(Movie movie:movies) {
    	Integer[] tocompare = movie.getGenres();
    	for(int i = 0; i < genres.length;i++) {
    		for(int j = 0; j<tocompare.length;j++) {
    			if(genres[i]==tocompare[j])
    				break;
    			
    			if (j == tocompare.length)
    				found = false;
    		}
    	}
    	found = true;
    	if(found)
    		gMovies.add(movie);
    }
    

	return gMovies;
    }

    /**
     * Creates a list of Movies whose ratings are equal to or higher than
     * rating.
     *
     * @param movies
     *            list of movies
     * @param rating
     *            to compare against
     * @return list of movies for rating
     */
    public static ArrayList<Movie> getByRating(final ArrayList<Movie> movies,
	    final double rating) {
	final ArrayList<Movie> rMovies = new ArrayList<>();

	for(Movie movie: movies) {
    	double ratings = movie.getRating();
    	for(int i = 0;i<movies.size();i++) {
    		if(ratings >= rating) {
    			rMovies.add(movie);
    		}
    	}
    }

	return rMovies;
    }

    /**
     * Creates a list of Movies from a particular year.
     *
     * @param movies
     *            list of movies
     * @param year
     *            year to search for
     * @return list of movies for year
     */
    public static ArrayList<Movie> getByYear(final ArrayList<Movie> movies,
	    final int year) {
	final ArrayList<Movie> yMovies = new ArrayList<>();

	for(Movie movie: movies) {
		int compare = movie.getYear();
		for(int i = 0; i<movies.size();i++) {
			if(compare == year) {
				yMovies.add(movie);
			}
		}
	}

	return yMovies;
    }

    /**
     * Testing.
     *
     * @param args
     *            Unused
     * @throws FileNotFoundException
     */
    public static void main(final String[] args) throws FileNotFoundException {

    // your code here

    }

    /**
     * Asks a user to select genres from a list of genres and returns an integer
     * list of the genres chosen.
     *
     * @return
     */
    public static Integer[] readGenres(final Scanner keyboard) {
	final ArrayList<Integer> genres = new ArrayList<>();

    System.out.println("Please enter the codes for genres, a number from one to ten seperated by commas");
    System.out.println(Movie.menu());
    String s_genre = keyboard.nextLine();
    Integer[] genrelist = Movie.genresStringToList(s_genre);
    for(int i = 0; i<genrelist.length;i++) {
    	genres.add(genrelist[i]);
    }

	return genres.toArray(new Integer[1]);
    }

    /**
     * Creates and returns a Movie object from a line of formatted string data.
     *
     * @param line
     *            a vertical bar-delimited line of movie data in the format
     *            title|year|director|rating|genres
     * @return the data from line as a Movie object
     */
    public static Movie readMovie(final String line) {

    String[] s_moviedata = line.split("|");
    int year = Integer.parseInt(s_moviedata[1]);
    double rating = Double.parseDouble(s_moviedata[3]);
    Integer[] i_genrelist = Movie.genresStringToList(s_moviedata[4]);
    
    Movie movie = new Movie(s_moviedata[0],year,s_moviedata[2],rating,i_genrelist);
    		
    return movie;		
    
    }

    /**
     * Reads a list of Movies from a file.
     *
     * @param file
     *            The file to read.
     * @return A list of Movie objects.
     * @throws FileNotFoundException
     */
    public static ArrayList<Movie> readMovies(final File file)
	    throws FileNotFoundException {
	final ArrayList<Movie> movies = new ArrayList<>();

    Scanner scanner = new Scanner(file);
    while(scanner.hasNextLine()) {
    	String line = scanner.nextLine();
    	Movie read_movie = readMovie(line);
    	movies.add(read_movie);
    }
    scanner.close();
	return movies;
    }

    /**
     * Writes the contents of movies to fv. Overwrites or creates a new file of
     * Movie objects converted to strings.
     *
     * @param fv
     * @param movies
     * @throws FileNotFoundException
     */
    public static void writeMovies(final File file, final Movie[] movies)
	    throws FileNotFoundException {
    PrintStream ps = new PrintStream(file);
    for(Movie movie: movies) {
    	movie.write(ps);
    }
    ps.close();
    }

}
