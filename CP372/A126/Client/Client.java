import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
import java.net.UnknownHostException;

public class Client {
    // private Socket socket;

    // public Client() {
    //     this.socket = null;
    // }
	public static void main(String[] args) 
			throws Exception {
		
        //configure connection stuff here
        // String hostname = "localhost";
		// int port = 4444;
		
        frame gui = new frame();
        gui.setVisible(true);

        /**
         * Test cases for each request function
         */

		// System.out.println("Client >> Sending GET request...");
		// String getResult = sendGetRequest(hostname, port, "images/test.png");
		// System.out.println("Client >> Result: " + getResult);

        // System.out.println("Client >> Sending POST request...");
        // String postResult = sendPostRequest(hostname, port, "20 50 150 200 blue testmessage");
        // System.out.println("Client >> Result: " + postResult);

        // System.out.println("Client >> Sending POST request...");
        // String postResult2 = sendPostRequest(hostname, port, "30 40 100 200 green reminder");
        // System.out.println("Client >> Result: " + postResult2);

        // System.out.println("Client >> Sending PIN request...");
        // String pinResult = sendPinRequest(hostname, port, "20 50");
        // System.out.println("Client >> Result: " + pinResult);

        // System.out.println("Client >> Sending SHAKE request...");
        // String shakeResult = sendShakeRequest(hostname, port);
        // System.out.println("Client >> Result: " + shakeResult);

        // System.out.println("Client >> Sending UNPIN request...");
        // String unpinResult = sendUnpinRequest(hostname, port, "20 50");
        // System.out.println("Client >> Result: " + unpinResult);

        

        // System.out.println("Client >> Sending CLEAR request...");
        // String clearResult = sendClearRequest(hostname, port);
        // System.out.println("Client >> Result: " + clearResult);
	}

    public static String sendConnectionRequest(String hostname, int port) throws Exception{

        String result = "";

        try {
            Socket socket = new Socket(hostname, port);

            PrintStream out = new PrintStream( socket.getOutputStream() );

            out.println("CONNECT");
            out.close();

            result = "Successfully connected to host: " + hostname + " port: " + String.valueOf(port);
            socket.close();
        } catch (UnknownHostException e) {
            result = "Unable to connect to host: " + hostname + " port: " + String.valueOf(port);
        }  catch (IOException e) {
            result = "I/O error while establishing connection to " + hostname + " port: " + String.valueOf(port);
        }     

        return result;
    }


    public static String sendDisconnectRequest(String hostname, int port) throws Exception{

        String result = "";

        Socket socket = new Socket(hostname, port);

        PrintStream out = new PrintStream( socket.getOutputStream() );

        out.println("DISCONNECT");
        out.close();

        socket.close();

        result = "Disconnected from host: " + hostname + " port: " + String.valueOf(port);

        return result;

    }


	public static String sendGetRequest(String hostname, int port, String body) 
			throws Exception {
		Socket socket = new Socket(hostname, port);

		PrintStream out = new PrintStream( socket.getOutputStream() );
        BufferedReader in = new BufferedReader( new InputStreamReader( socket.getInputStream() ) );
        
        if (body.equals("")) {
            out.println("GET ALL");
        }

        else {
            out.println("GET " + body);
        }

        out.println();
        out.flush();

        String result = "";
        String line = in.readLine();
        while( line != null ) {
        	result += line;
        	line = in.readLine();
        }
        
        out.flush();

        out.close();
        in.close();
        socket.close();
        
        return result;
	}

    public static String sendPostRequest(String hostname, int port, String body) throws Exception{

        Socket socket = new Socket(hostname, port);

        PrintStream out = new PrintStream( socket.getOutputStream() );
        BufferedReader in = new BufferedReader(new InputStreamReader( socket.getInputStream() ) );

        out.println("POST " + body);
        out.println();
        out.flush();

        String result = "";
        String line = in.readLine();
        while (line != null) {
            result += line;
            line = in.readLine();
        }

        out.flush();

        out.close();
        in.close();
        socket.close();

        return result;

    }

    public static String sendPinRequest(String hostname, int port, String body) throws Exception {

        Socket socket = new Socket(hostname, port);

        PrintStream out = new PrintStream( socket.getOutputStream() );
        BufferedReader in = new BufferedReader(new InputStreamReader( socket.getInputStream() ) );

        out.println("PIN " + body);
        out.println();
        out.flush();

        String result = "";
        String line = in.readLine();
        while (line != null) {
            result += line;
            line = in.readLine();
        }

        out.flush();

        out.close();
        in.close();
        socket.close();

        return result;
    }

    public static String sendUnpinRequest(String hostname, int port, String body) throws Exception {

        Socket socket = new Socket(hostname, port);

        PrintStream out = new PrintStream( socket.getOutputStream() );
        BufferedReader in = new BufferedReader(new InputStreamReader( socket.getInputStream() ) );

        out.println("UNPIN " + body);
        out.println();
        out.flush();

        String result = "";
        String line = in.readLine();
        while (line != null) {
            result += line;
            line = in.readLine();
        }

        out.flush();

        out.close();
        in.close();
        socket.close();

        return result;

    }

    public static String sendShakeRequest(String hostname, int port) throws Exception {

        Socket socket = new Socket(hostname, port);

        PrintStream out = new PrintStream( socket.getOutputStream() );
        BufferedReader in = new BufferedReader(new InputStreamReader( socket.getInputStream() ) );

        out.println("SHAKE");
        out.println();
        out.flush();

        String result = "";
        String line = in.readLine();
        while (line != null) {
            result += line;
            line = in.readLine();
        }

        out.flush();
        in.close();
        out.close();

        socket.close();

        return result;

    }

    public static String sendClearRequest(String hostname, int port) throws Exception {

        Socket socket = new Socket(hostname, port);

        PrintStream out = new PrintStream( socket.getOutputStream() );
        BufferedReader in = new BufferedReader(new InputStreamReader( socket.getInputStream() ) );

        out.println("CLEAR");
        out.println();
        out.flush();

        String result = "";
        String line = in.readLine();
        while (line != null) {
            result += line;
            line = in.readLine();
        }

        out.flush();

        out.close();
        in.close();
        socket.close();

        return result;

    }
	
}
