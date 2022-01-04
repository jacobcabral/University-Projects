package cp213;

public class A01 {
	 public static void main(String[] args) {
		 int year = 2001;
		 int year2 = 2000;
		 //System.out.println(isLeapYear(year2));
		 System.out.println(isPalindrome("Racecar"));
		 System.out.println(pigLatin("hanayo"));

	    }
	 /**
	     * Determines if s is a palindrome. Ignores case, spaces, digits, and
	     * punctuation in the string parameter s.
	     *
	     * @param s
	     *            a string
	     * @return true if s is a palindrome, false otherwise
	     */
	 public static boolean isPalindrome(final String s) {
		 boolean isPalindrome = true;
		 char[] letters = s.replaceAll("[[^A-Za-z]+]", "").toLowerCase().toCharArray();
		 int front = 0;
		 int back = letters.length -1; 
		 while (front < back) { 
			  
	            if (letters[front] != letters[back]) 
	                isPalindrome = false; 
	  	            
	            front++; 
	            back--; 
	        } 
		 return isPalindrome;
		 		
		 	}
		
		 	
	 /**
	     * Determines whether or not a year is a leap year.
	     *
	     * @param year
	     *            The year to test (int > 0)
	     * @return true if year is a leap year, false otherwise.
	     */  
	 public static boolean isLeapYear(final int year) {
	        boolean isLeapYear = false;
	        if(year % 4 == 0) {
	        	if(year % 100 == 0) {
	        		if (year % 400 == 0) 
	        			isLeapYear = true;
	        		else 
	        			isLeapYear = false;
	        		
	        	}
	        	else 
        			isLeapYear = true;
	        }
	        else {isLeapYear = false;
	        }
	        return isLeapYear;
	    }
	 /**
	     * Determines if name is a valid Java variable name. Variables names must
	     * start with a letter or an underscore, but cannot be an underscore alone.
	     * The rest of the variable name may consist of letters, numbers and
	     * underscores.
	     *
	     * @param name
	     *            a string to test as a Java variable name
	     * @return true if name is a valid Java variable name, false otherwise
	     */
	 public static boolean isValid(final String name) {
		 boolean isValid = true;
	        if(name == "_")
	        	isValid = false;
	        for(int i = 0; i<name.length();i++) {
	        	if (Character.isAlphabetic(name.charAt(i)) == false || Character.isDigit(name.charAt(i)) == false || name.charAt(i) == '_') {
	        		isValid = false;
	        	}
	        }
	        return isValid;
	    }
	 
	 /**
	     * Determines the smallest, largest, total, and average of the values in the 2D
	     * list a. You may assume there is at least one value in a and that a is a
	     * square matrix - i.e. the number of columns per row is the same. a must be
	     * unchanged.
	     *
	     * @param a - a 2D list of numbers (2D list of double)
	     *
	     * @return a list of four double values containing the smallest number in a,the
	     *         largest number in a, the total of all numbers in a, and the average
	     *         of all numbers in a, in that order.
	     */
	    public static double[] matrixStats(double[][] a) {
	    	double smallest = a[0][0];
	    	double largest = a[0][0];
	    	double total = 0;
	    	int counter = 0;
	    	
	    	for(int i = 0; i<a.length; i++) {
	        	for(int j = 0;j<a[i].length;j++ ) {
	        		total += a[i][j];
	        		counter++;
	        		if(a[i][j] < smallest) {
	        			smallest = a[i][j];
	        		} else if (a[i][j] > largest) {
	        			largest = a[i][j];
	        		}
	        }
	    }
	    	double average = total/counter;
	    	double[] results = new double[4];
	    	results[0] = smallest;
	    	results[1] = largest;
	    	results[2] = total;
	    	results[3] = average;
	    	return results;
	    }
	    /**
	     * Converts a word to Pig Latin. The conversion is:
	     * 

	     
	if a word begins with a vowel, add "way" to the end of the word.

	     
	if the word begins with consonants, move the leading consonants to the
	     end of the word and add "ay" to the end of that. "y" is treated as a
	     consonant if it is the first character in the word, and as a vowel for
	     anywhere else in the word.

	     

	     * Preserve the case of the word - i.e. if the first character of word is
	     * upper-case, then the new first character should also be upper case.
	     *
	     * @param word The string to convert to Pig Latin
	     * @return the Pig Latin version of word
	     */
	    public static String pigLatin(String word) {
			String pl = "ay";
			String pltwo = "way";
			String consenant = "";
			String ending = "";
			String finalword = "";
			String cap = "";
			boolean firstupper;
			//godspeed to the sea shanties that i listen to when i write this.
			//check if the first letter is capital so i can change it later.
			if (Character.isUpperCase(word.charAt(0)) == true) {
				firstupper = true;
			}else {firstupper = false;}
			word = word.toLowerCase();
			//check if the first letter is a vowel
			if(word.charAt(0) == 'a' ||word.charAt(0) == 'e'|| word.charAt(0) == 'i'|| word.charAt(0) == 'o'||word.charAt(0) == 'u') {
				//add "way" to the end of the word
					finalword = word+pltwo;
			}else {
				//in the words of Anakin Skywalker, this is where the fun begins
				for(int i = 0; i < word.length(); i++) {
					if(word.charAt(i) == 'e'||word.charAt(i) == 'a' || word.charAt(i) == 'i' || word.charAt(i) == 'o' || word.charAt(i) == 'u' || word.charAt(i) == 'y') {
						consenant = word.substring(0,i);
						ending = word.substring(i);
						break;
			}
		}
				finalword = ending+consenant+pl;
	        
}
			if(firstupper) {
				cap = finalword.substring(0, 1).toUpperCase() + finalword.substring(1);
			} else { cap = finalword;}
			return cap;
	    }
	    }
