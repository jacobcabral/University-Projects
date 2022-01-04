
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Iterator;


public class Server extends Thread implements Runnable {
	    private ServerSocket serverSocket;
	    private int port;
	    private boolean running;
        public ArrayList<Note> noteList = new ArrayList<Note>();
        public int board_width;
        public int board_height;
        public String[] colors;

	    public Server( int port, int board_width, int board_height, String[] colors) {
	        this.port = port;
	        this.running = false;
            this.board_width = board_width;
            this.board_height = board_height;
            this.colors = colors;

	    }

	    public void startServer() {
	    	try {
	    		this.running = true;
	            serverSocket = new ServerSocket( port );
	            super.start();
	        
	    	} catch (IOException e) {
	    		e.printStackTrace();
	        }
	    }

	    public void stopServer() {
	        running = false;
	        super.interrupt();
	    }

	    @Override
	    public void run() {
	    	while(running) {
	    		try {
		            System.out.println( "Server >> Listening..." );
	                Socket socket = serverSocket.accept();
	                ClientConnectionThread client = new ClientConnectionThread( this, socket );
	                client.start();
	                
	    		} catch (IOException e) {
	                e.printStackTrace();
	            }
	        }
	    }

	    public static void main(String[] args) {
	        int port = Integer.parseInt(args[0]);
            int board_width = Integer.parseInt(args[1]);
            int board_height = Integer.parseInt(args[2]);
            
            String[] colors = new String[(args.length - 1) - 2];

            int index = 0;
            for (int i = 3; i < (args.length); i++) {
                colors[index] = args[i];
                index++;
            }
            //System.out.println(colors[2]);
	        Server server = new Server( port, board_width, board_height, colors );
	        server.startServer();

	        try {
	            Thread.sleep( 60000 ); //CHANGE THIS VALUE TO CHANGE SERVER UPTIME
	        
	        } catch(Exception e) {
	            e.printStackTrace();
	        }

	        server.stopServer();
	    }
	}

	class ClientConnectionThread extends Thread {
	    
		private Socket socket;
        private Server server;
        //private boolean maintain_connection;
	    
		public ClientConnectionThread(Server server, Socket socket) {
			this.socket = socket;
            this.server = server;
            //this.maintain_connection = true;
	    }

	    @Override
	    public void run() {
	        
            //System.out.println( "Server >> Connection Received" );

            try {
	            System.out.println( "Server >> Connection Received" );

	            BufferedReader in = new BufferedReader( new InputStreamReader( socket.getInputStream() ) );
	            PrintWriter out = new PrintWriter( socket.getOutputStream() );

	            String input = in.readLine();
	            System.out.println( "Server >> Client input received: " + input );
	            String response = "UNDEFINED";
	            switch(input.split(" ")[0]) { //gotta add reactions for POST, PIN, UNPIN, CLEAR, SHAKE, DISCONNECT
	            	case "CONNECT":
                        response = "Client successfully connected.";

                        break;
                    
                    
                    
                    
                    case "GET":
	            		//response = "I GOT A GET";
                        ArrayList<Note> list_copy = server.noteList;
                        
                        if (server.noteList.isEmpty()) {
                            response = "GET recieved, no notes to send.";
                        }
                        
                        //System.out.println(String.valueOf(input.split(" ")[1]));
                        else if (input.split(" ")[1].equals("PINS")) {
                            //System.out.println("Inside PINS if check");
                            String notes_list = "";
                            Iterator<Note> pins_iter = list_copy.iterator();

                            while (pins_iter.hasNext()) {
                                Note curr_note = pins_iter.next();

                                if (curr_note.status == true) { //if the note is pinned, add it to the pins list
                                    notes_list += curr_note.getNoteProperties();
                                }
                            }

                            response = "GET PINS recieved, pinned notes:" + System.lineSeparator() + notes_list;

                        }

                        else {

                            String[] parameters = input.split(" ");

                            boolean search_by_color = false;
                            String color_param = "";
                            boolean search_by_coords = false;
                            String coords_param = "";
                            boolean search_by_substring = false;
                            String substring_param = "";
                            String results = "";

                            if (input.equals("GET") == false) {
                                
                                for (String parameter : parameters) {
                                    //System.out.println(parameter);
                                    if (parameter.contains("color=")) {
                                        search_by_color = true;
                                        color_param = parameter.split("=")[1];
                                        //System.out.println(color_param);
                                    }
    
                                    if (parameter.contains("contains=")) {
                                        search_by_coords = true;
                                        coords_param = parameter.split("=")[1];
                                    }
    
                                    if (parameter.contains("refersTo=")) {
                                        search_by_substring = true;
                                        substring_param = parameter.split("=")[1];
                                    }
                                }
                            }


                            

                            if (search_by_color == true && search_by_coords == false && search_by_substring == false) {

                                Iterator<Note> color_iter = server.noteList.iterator();

                                while (color_iter.hasNext()) {
                                    Note currNote = color_iter.next();

                                    if (currNote.color.equals(color_param)) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else if (search_by_color == false && search_by_coords == true && search_by_substring == false) {

                                Iterator<Note> coords_iter = server.noteList.iterator();

                                while (coords_iter.hasNext()) {
                                    Note currNote = coords_iter.next();

                                    int x_coord = Integer.parseInt(coords_param.split(",")[0]);
                                    int y_coord = Integer.parseInt(coords_param.split(",")[1]);

                                    if (currNote.x == x_coord && currNote.y == y_coord) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else if (search_by_color == false && search_by_coords == false && search_by_substring == true) {

                                Iterator<Note> substring_iter = server.noteList.iterator();

                                while (substring_iter.hasNext()) {
                                    Note currNote = substring_iter.next();

                                    if (currNote.message.contains(substring_param)) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else if (search_by_color == true && search_by_coords == true && search_by_substring == false) {

                                Iterator<Note> color_coords_iter = server.noteList.iterator();

                                while (color_coords_iter.hasNext()) {
                                    Note currNote = color_coords_iter.next();

                                    int x_coord = Integer.parseInt(coords_param.split(",")[0]);
                                    int y_coord = Integer.parseInt(coords_param.split(",")[1]);

                                    if (currNote.color.equals(color_param) && currNote.x == x_coord && currNote.y == y_coord) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else if (search_by_color == true && search_by_coords == false && search_by_substring == true) {
                                
                                Iterator<Note> color_substring_iter = server.noteList.iterator();

                                while (color_substring_iter.hasNext()) {
                                    Note currNote = color_substring_iter.next();

                                    if (currNote.color.equals(color_param) && currNote.message.contains(substring_param)) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else if (search_by_color == false && search_by_coords == true && search_by_substring == true) {

                                Iterator<Note> coords_substring_iter = server.noteList.iterator();

                                while (coords_substring_iter.hasNext()) {
                                    Note currNote = coords_substring_iter.next();

                                    int x_coord = Integer.parseInt(coords_param.split(",")[0]);
                                    int y_coord = Integer.parseInt(coords_param.split(",")[1]);

                                    if (currNote.x == x_coord && currNote.y == y_coord && currNote.message.contains(substring_param)) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else if (search_by_color == true && search_by_coords == true && search_by_substring == true) {

                                Iterator<Note> color_coords_substring_iter = server.noteList.iterator();

                                while (color_coords_substring_iter.hasNext()) {
                                    Note currNote = color_coords_substring_iter.next();

                                    int x_coord = Integer.parseInt(coords_param.split(",")[0]);
                                    int y_coord = Integer.parseInt(coords_param.split(",")[1]);

                                    if (currNote.color.equals(color_param) && currNote.x == x_coord && currNote.y == y_coord && currNote.message.contains(substring_param)) {
                                        results += currNote.getNoteProperties();
                                    }
                                }
                            }

                            else { //no parameters, get all notes
                                //System.out.println("In no parameters else");
                                Iterator<Note> notes_iter = server.noteList.iterator();

                                while (notes_iter.hasNext()) {
                                    Note currNote = notes_iter.next();

                                    results += currNote.getNoteProperties();
                                }

                            }


                            response = "GET recieved, notes:" + System.lineSeparator() + results;
                        }


	            		break;
	            
	            	case "POST":
	            		
                        String[] args = input.split(" "); //getting each argument as an array element to plug into note object creation
                        
                        //setting up note object to add to list

                        int x_coord = Integer.parseInt(args[1]);
                        int y_coord = Integer.parseInt(args[2]);
                        int width = Integer.parseInt(args[3]);
                        int height = Integer.parseInt(args[4]);
                        String color = args[5];
                        String message = args[6];

                        if ( (x_coord + width) < server.board_width && (y_coord + height) < server.board_height) { //making sure note is in bounds

                            //check colors list to make sure given color is in list
                            boolean color_in_list = false;
                            for (int i = 0; i < server.colors.length; i++) {
                                if (server.colors[i].equals(color)) {
                                    color_in_list = true;
                                }
                            }

                            if (color_in_list == true) { //note args are all within boundaries, create note and add to list

                                try {
                                    Note new_note = new Note(x_coord, y_coord, width, height, color, message, false);
                                    server.noteList.add(new_note);
                                    response = "POST command is valid, updating board.";
                                } catch (Exception e) {
                                    response = "POST command invalid, check input formatting.";
                                }

                                
                            }

                            else {
                                response = "POST command invalid:\ncolor chosen is not in available color list.";
                            }

                        }

                        else {
                            response = "POST command invalid:\nnote is not within board boundaries.";
                        }
                        
                        //System.out.println(server.noteList.size());

	            		break;

                    case "PIN":
                        String[] coords = input.split(" ");

                        boolean note_pinned = false;
                        int x = Integer.parseInt(coords[1]);
                        int y = Integer.parseInt(coords[2]);

                        Iterator<Note> iter = server.noteList.iterator();

                        while (iter.hasNext()) {
                            Note curr_note = iter.next();
                            if ( (curr_note.x == x) && (curr_note.y == y) && (curr_note.status == false) ) {
                                curr_note.status = true; //set pinned true
                                response = "Note pinned on board.";
                                note_pinned = true;
                            }
                        }

                        if (note_pinned == false) {
                            response = "Reference note not found, no note pinned.";
                        }
                        

                        break;

                    case "UNPIN":
                        String[] note_coords = input.split(" ");
                        //System.out.println("In unpin case");
                        boolean note_unpinned = false;
                        int x_coordinate = Integer.parseInt(note_coords[1]);
                        int y_coordinate = Integer.parseInt(note_coords[2]);

                        Iterator<Note> itr = server.noteList.iterator();

                        while (itr.hasNext()) {
                            Note curr_note = itr.next();
                            if ( (curr_note.x == x_coordinate) && (curr_note.y == y_coordinate) && curr_note.status == true ) {
                                curr_note.status = false;
                                response = "Note unpinned on board.";
                                note_unpinned = true;
                            }
                        }

                        if (note_unpinned == false) {
                            response = "Note referenced not found, no note unpinned.";
                        }

                        break;

                    case "SHAKE":
                        if (server.noteList.isEmpty()) {
                            response = "No notes on board. Nothing to clear.";
                        }

                        else {
                            Iterator<Note> iterator = server.noteList.iterator();

                            while (iterator.hasNext()) {
                                Note curr_note = iterator.next();

                                if (curr_note.status == false) {
                                    iterator.remove();
                                }
                            }
                            response = "All unpinned notes removed.";
                        }
                        

                        
                        break;


                    

                    case "CLEAR": //remove all notes from the list regardless of state

                        if (server.noteList.isEmpty()) {
                            response = "No notes to clear.";
                        }

                        else {
                            response = "Clearing out all the notes.";
                            server.noteList.clear();
                        }

                        break;
                    
	            		
	            	default:
	            		break;

                    case "DISCONNECT":

                        response = "Connection closed.";
                        //this.maintain_connection = false;
                        socket.close();
                        in.close();
	                    out.close();
                        System.out.println( "Server >> Connection Closed" );

                        break;
	            		
	            }
	            
	            out.println("RESPONSE >>" + response);
	            out.flush();
	            
	            in.close();
	            out.close();
	            socket.close();
	            System.out.println( "Server >> Connection Closed" );
	        
	        } catch(Exception e) {
	        	e.printStackTrace();
	        }

            }
	    
	}

    