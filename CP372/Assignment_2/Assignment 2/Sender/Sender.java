
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.lang.Object;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketTimeoutException;
import java.net.DatagramPacket;

public class Sender {

    sendergui gui;

    public Sender(sendergui gui) {
        this.gui = gui;
    }
    
    public static void main(String args[]) throws Exception{
        
        
        /**
         * DatagramPacket objects need to be contsructed before being sent off to receiver
         * data in said packets is of type byte, which stores whole numbers from -128 to 127
         * also has Inet address and port properties, but setters exist for setting those properly
         */

        sendergui gui = new sendergui();
        Sender sender = new Sender(gui);
        sender.gui.setVisible(true);
        
        

    }

    /**
     * 
     * @param receiver_address - Inputted IP address for receiver from GUI
     * @param ack_port - Inputted UDP ACK port from GUI
     * @param data_port - Inputted UDP data port from GUI
     * @param filename - Inputted filename from GUI
     * @param timeout - Inputted timeout from from GUI
     */

    public static String handleSendButtonPress(String receiver_address, String ack_port, String data_port, String filename, String timeout, sendergui gui) 
        throws Exception {

        String result = "";

        //ports need to be changed to ints for Datagram objects
        int ack_port_int = Integer.parseInt(ack_port);
        int data_port_int = Integer.parseInt(data_port);

        //setup UDP ack socket with inputted port number
        DatagramSocket ack_socket = new DatagramSocket(ack_port_int);
        System.out.println("Creating ack_socket with port number " + ack_port);

        //also need timeout as an integer
        int timeout_int = Integer.parseInt(timeout);

        //making the File object to pass to sendPackets
        File file_object = new File(filename);

        //send processed inputs to sendPackets
        try {
            sendPackets(receiver_address, ack_port_int, data_port_int, file_object, timeout_int, ack_socket, gui);
       
        } catch (Exception e) {
            e.printStackTrace();
            result = "Error while preparing file to send to receiver.";
        }

        result = "Sent file to receiver.";
        ack_socket.close();

        return result;

    }

    public static String handleIsAliveButtonPress(String receiver_address, String ack_port, String data_port, String timeout)
        throws Exception {

        String result = "";

        int ack_port_int = Integer.parseInt(ack_port);
        int data_port_int = Integer.parseInt(data_port);

        //setup UDP ack socket with inputted port number
        DatagramSocket ack_socket = new DatagramSocket(ack_port_int);
        System.out.println("Creating ack_socket with port number " + ack_port);

        int timeout_int = Integer.parseInt(timeout);

        try {
            sendIsAlivePacket(receiver_address, ack_port_int, data_port_int, timeout_int, ack_socket);

        } catch (Exception e) {
            e.printStackTrace();
            result = "Error while preparing IsAlive? packet.";
        }

        result = "Receiver is ready for packets.";
        ack_socket.close();

        return result;
    }


    /**
     * Method that gets called once the SEND button is pressed on the GUI
     * @param sendingFile - the file to be sent to the receiver
     */

    public static void sendPackets(String receiver_address, int ack_port, int data_port, File sendingFile, int timeout, DatagramSocket socket, sendergui gui) throws Exception {

        
        BufferedReader line = new BufferedReader( new FileReader(sendingFile) );
        int sequence_number = 0; //for making sure the packets are received in order
        InetAddress receiver_ip = InetAddress.getByName(receiver_address);
        

        String mode = gui.getMode(); //reliable or unreliable
        boolean unreliable = false; //used a flag below to determine whether every 10th packet should "dropped"

        if (mode.equals("unreliable")) {
            unreliable = true;
        }

        boolean eof = false;
        
        
        //while we haven't reached the end of the file, create a DatagramPacket, and send it to the receiver, and wait for ack before sending next packet
        while (!eof) {

            String data = "";

            for (int i = 0; i < 7; i++) {
                char curr_char = (char) line.read();
                // System.out.println(curr_char);
                
                // int compare = Character.compare(curr_char, '?');
                // System.out.println("Results of compare: " + String.valueOf(compare));

                if (Character.compare(curr_char, '?') == 65472) { //in testing whatever char that it was filling when the while loop was going forever looked like a '?'
                    eof = true;                                   //but apparently isn't because of the weird difference value in the if above
                    
                }  

                else {
                    data += curr_char;
                }
                              
         
            }

            if (sequence_number == 0) {
                data += "0";
                sequence_number = 1;
                
            }

            else {
                data += "1";
                sequence_number = 0;
                
            }

            if (unreliable && (gui.packets_sent % 10 == 0)) { //if sender is set to unreliable and we are on the tenth packet

                socket.setSoTimeout(timeout / 1000); //setting timeout for receive (input is in microseconds, need to convert to milliseconds so we divide by 1000)
                byte[] buffer = new byte[8];
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                System.out.println("Waiting for ACK");

                gui.packets_sent += 1;
                gui.setPacketCount();
                gui.paintAll( gui.getGraphics() );

                try {
                    socket.receive(packet);
                } catch (SocketTimeoutException e) { //if it timesout, send the packet again
                    gui.updateStatusText("Packet dropped, resending packet");
                    System.out.println("Packet dropped, resending packet");
                    packet = new DatagramPacket(data.getBytes(), data.length(), receiver_ip, data_port);
                    socket.send(packet);

                    gui.packets_sent += 1;
                    gui.setPacketCount();
                    gui.paintAll( gui.getGraphics() ); //so that we can see the number of packets sent increasing

                    packet = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet);
                }

            }

            else {

                DatagramPacket packet = new DatagramPacket(data.getBytes(), data.length(), receiver_ip, data_port);
                System.out.println("Creating packet with data: " + data);
                socket.send(packet);
                socket.setSoTimeout(timeout / 1000); //setting timeout for receive (input is in microseconds, need to convert to milliseconds so we divide by 1000)
                byte[] buffer = new byte[8];
                packet = new DatagramPacket(buffer, buffer.length);
                System.out.println("Waiting for ACK");

                gui.packets_sent += 1;
                gui.setPacketCount();
                gui.paintAll( gui.getGraphics() );

                try {
                    socket.receive(packet);
                } catch (SocketTimeoutException e) { //if it timesout, send the packet again
                    packet = new DatagramPacket(data.getBytes(), data.length(), receiver_ip, data_port);
                    socket.send(packet);

                    gui.packets_sent += 1;
                    gui.setPacketCount();
                    gui.paintAll( gui.getGraphics() );

                    packet = new DatagramPacket(buffer, buffer.length);
                    socket.receive(packet);
                }
            }

            System.out.println("Ack received");

        }

        String end_of_transmission = "end" + sequence_number;
        DatagramPacket end_packet = new DatagramPacket(end_of_transmission.getBytes(), end_of_transmission.length(), receiver_ip, data_port);
        socket.send(end_packet);
        System.out.println("Sent end of transmission packet");

        line.close();

    }

    public static void sendIsAlivePacket(String receiver_address, int ack_port, int data_port, int timeout, DatagramSocket ack_socket) throws Exception {

        //works similar to send packet except it sends a prebuilt is alive packet
        int sequence_number = 0;
        InetAddress receiver_ip = InetAddress.getByName(receiver_address);
        String alive = "alive?" + String.valueOf(sequence_number);

        DatagramPacket packet = new DatagramPacket(alive.getBytes(), alive.length(), receiver_ip, data_port);
        ack_socket.send(packet);
        System.out.println("Sent receiver 'alive?' packet");
        
        byte[] buffer = new byte[8];
        packet = new DatagramPacket(buffer, buffer.length);
        System.out.println("Waiting for 'alive?' ACK");
        ack_socket.receive(packet);
        System.out.println("'alive?' ACK received");

    }

}