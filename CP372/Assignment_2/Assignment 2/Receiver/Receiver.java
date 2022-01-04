
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.lang.Object;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.net.DatagramPacket;

public class Receiver {
     static int seq = 0;

    public static void main(String args[]) {

        /**
         * Parsing cmd line inputs that follow the following format:
         * java Receiver ip_address UDP_port_number UDP_port_number filename
         */
        String sender_address = args[0];
        String data_port = args[1];
        String ack_port = args[2];
        String filename = args[3];

        int i_ackport = Integer.parseInt(ack_port);
        int packets_received = 0;

        BufferedWriter bw = null;

        //if the specified filename does not exist, create it
        try {
            
            File receiving_file = new File(filename);
            
            

            if ( receiving_file.createNewFile() ){
                System.out.println("File does not exist, creating file: " + filename);
            }

            else {
                System.out.println("File already exists.");
            }
            FileWriter fw = new FileWriter(receiving_file);
            bw = new BufferedWriter(fw);
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        try{
            //receiver sets up data exchange port
            int data_port_int = Integer.parseInt(data_port);
            DatagramSocket data_socket = new DatagramSocket(data_port_int);
            InetAddress senderaddress = InetAddress.getByName(sender_address);
            System.out.println("Setting up data socket with port: " + data_port);

            Boolean is_running = true;
            byte[] buf = new byte[256];

            long start_time = 0;

            while(is_running){
                //make and receive incoming packet
                DatagramPacket packet = new DatagramPacket(buf,buf.length);
                System.out.println("Waiting for packet");
                data_socket.receive(packet);

                if (packets_received == 0) {
                    start_time = System.currentTimeMillis();
                }

                packets_received += 1;

                String write = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Received packet");
                //System.out.println(write);
                String substring = write.substring(0, write.length() - 1);                    
                if(Integer.parseInt(write.substring(write.length() -1)) == seq) {
                    
                    
                    if ( !write.equals("end") ) {
                            
                        
                        //System.out.println(substring);

                        if (!substring.equals("alive?")) {
                            
                            write = write.substring(0, write.length()-1);
                    
                            bw.write(write);
                        }

                        
                    }

                       
                    
    
                    packet = new DatagramPacket(buf,buf.length,senderaddress,i_ackport);
                    String receive = new String(packet.getData(), 0, packet.getLength());
    
                    System.out.println("Received data: " + receive);
    
                    if(write.equals("end")){
                        is_running = false;
                        continue;
                    }
                    data_socket.send(packet);
    
                    bw.flush();
                    buf = new byte[256]; //effectively flushing the buffer, so that packets like end packet with less data don't inherit extra from the previous packet

                    if (!substring.equals("alive?")) {
                        
                        if(seq == 0) {
                            seq = 1;
                        }
                        else if(seq == 1) {
                            seq = 0;
                        }
                    }


                    
                }
   
            }

            long end_time = System.currentTimeMillis();
            System.out.println("End of transmission packet received");
            
            double transfer_time = (end_time - start_time) / 1000.00; //converting ms to seconds

            System.out.println("Total time taken to transfer file: " + String.valueOf(transfer_time) + "sec");
        
            bw.close();
            data_socket.close();
        } catch (SocketException e){
            e.printStackTrace();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
