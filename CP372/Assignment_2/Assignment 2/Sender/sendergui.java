import javax.swing.JFrame;

/**
 *
 * @author Jake
 */
public class sendergui extends javax.swing.JFrame {

    public int packets_sent;
    
    public sendergui() {

        this.packets_sent = 0;

        initComponents();
    }

    public void setPacketCount() {

        jLabel3.setText( String.valueOf(this.packets_sent) );
    }

    public void updateStatusText(String text) {

        textupdates.setText(text);
    }

    public String getMode() { //used in sender to determine whether reliable or unreliable was selected
        //will return unreliable if the radio button is toggled, reliable for anything else (i.e reliable is selected or nothing is selected)

        boolean is_unreliable = unreliable.isSelected();
        String result = "reliable";

        if (is_unreliable) { 
            result = "unreliable";
        }

        return result;
    }

    @SuppressWarnings("unchecked")

    private void initComponents() {

         
        unreliable = new javax.swing.JRadioButton();
        ipaddress = new javax.swing.JTextField();
        ackport = new javax.swing.JTextField();
        dataport = new javax.swing.JTextField();
        filename = new javax.swing.JTextField();
        timeout = new javax.swing.JTextField();
        jLabel1 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        textupdates = new javax.swing.JTextArea();
        isalive = new javax.swing.JButton();
        jLabel2 = new javax.swing.JLabel();
        send = new javax.swing.JButton();
        reliable = new javax.swing.JRadioButton();
        jLabel3 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        unreliable.setText("Unreliable Sending");
        

        ipaddress.setText("Enter Receiver IP here");
        ipaddress.setToolTipText("Enter Receiver IP");
        ipaddress.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ipaddressActionPerformed(evt);
            }
        });

        ackport.setText("Enter UDP ACK Port Here");
        ackport.setToolTipText("Enter UDP ACK port");
        ackport.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ackportActionPerformed(evt);
            }
        });

        dataport.setText("Enter UDP DATA port here");
        dataport.setToolTipText("Enter UDP Data port here");
        dataport.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                dataportActionPerformed(evt);
            }
        });

        filename.setText("Enter Filename here");
        filename.setToolTipText("Enter Filename");
        filename.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                filenameActionPerformed(evt);
            }
        });

        timeout.setText("Enter Timeout");
        timeout.setToolTipText("Enter the timeout (in microseconds)");
        timeout.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                timeoutActionPerformed(evt);
            }
        });

        jLabel1.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        jLabel1.setText("Current number of sent in-order packets");

        textupdates.setColumns(20);
        textupdates.setRows(5);
        jScrollPane1.setViewportView(textupdates);

        isalive.setText("ISALIVE?");
        isalive.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                isaliveActionPerformed(evt);
            }
        });

        jLabel2.setFont(new java.awt.Font("Tahoma", 0, 18)); // NOI18N
        jLabel2.setText("Sender GUI");

        send.setText("SEND");
        send.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                sendActionPerformed(evt);
            }
        });

        reliable.setText("Reliable Sending");

        jLabel3.setFont(new java.awt.Font("Tahoma", 0, 18)); // NOI18N
        jLabel3.setText("0");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 263, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(reliable)
                            .addComponent(unreliable))
                        .addGap(0, 0, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(ipaddress)
                            .addComponent(ackport)
                            .addComponent(dataport, javax.swing.GroupLayout.DEFAULT_SIZE, 150, Short.MAX_VALUE)
                            .addComponent(filename)
                            .addComponent(timeout)
                            .addComponent(jLabel2))
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGap(98, 98, 98)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(isalive, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(send, javax.swing.GroupLayout.PREFERRED_SIZE, 110, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(0, 0, Short.MAX_VALUE))
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 40, Short.MAX_VALUE)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                        .addComponent(jLabel1)
                                        .addContainerGap())
                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                        .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 89, javax.swing.GroupLayout.PREFERRED_SIZE)
                                        .addGap(78, 78, 78))))))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jLabel2)
                        .addGap(30, 30, 30)
                        .addComponent(ipaddress, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(20, 20, 20)
                        .addComponent(jLabel1)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 25, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(ackport, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(10, 10, 10)
                        .addComponent(dataport, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(15, 15, 15)
                        .addComponent(filename, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(timeout, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(47, 47, 47))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGap(23, 23, 23)
                        .addComponent(isalive, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(16, 16, 16)
                        .addComponent(send, javax.swing.GroupLayout.PREFERRED_SIZE, 59, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(27, 27, 27)))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 0, Short.MAX_VALUE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(reliable)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(unreliable)
                        .addGap(0, 84, Short.MAX_VALUE)))
                .addContainerGap())
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void ipaddressActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:
    }

    private void ackportActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:
    }

    private void dataportActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:
    }

    private void filenameActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:
    }

    private void timeoutActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:
    }

    private void isaliveActionPerformed(java.awt.event.ActionEvent evt) {
        //getting all the arguments for the handler that connects to the backend
        String receiver_address = ipaddress.getText();
        String ack_port = ackport.getText();
        String data_port = dataport.getText();
        String timeout_str = timeout.getText();

        try {
            String isAlive_result = Sender.handleIsAliveButtonPress(receiver_address, ack_port, data_port, timeout_str);
            textupdates.setText(isAlive_result);

        } catch (Exception e) {
            e.printStackTrace();
            textupdates.setText("Error completing isAlive? action.");
        }
    }

    private void sendActionPerformed(java.awt.event.ActionEvent evt) {
        //getting all the arguments for the handler that connects to the backend
        String receiver_address = ipaddress.getText();
        String ack_port = ackport.getText();
        String data_port = dataport.getText();
        String file_name = filename.getText();
        String timeout_str = timeout.getText();
        System.out.println(ack_port);

        //if any of the fields required still say "Enter <parameter> here"
        if ( receiver_address.contains("Enter") || ack_port.contains("Enter") || 
        data_port.contains("Enter") || file_name.contains("Enter") || timeout_str.contains("Enter") ) {
            textupdates.setText("Current input is invalid, fill in all fields and try again.");
        }

        else {

            try {
                String send_result = Sender.handleSendButtonPress(receiver_address, ack_port, data_port, file_name, timeout_str, this);
                textupdates.setText(send_result);
            
            } catch (Exception e) {
                e.printStackTrace();
                textupdates.setText("Error completing Send action.");
            }

        }
    }


    public static void main(String args[]) {
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(sendergui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(sendergui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(sendergui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(sendergui.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }



        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new sendergui().setVisible(true);
            }
        });
    }

    private javax.swing.JTextField ackport;
    private javax.swing.JTextField dataport;
    private javax.swing.JTextField filename;
    private javax.swing.JTextField ipaddress;
    private javax.swing.JButton isalive;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JRadioButton reliable;
    private javax.swing.JButton send;
    private javax.swing.JTextArea textupdates;
    private javax.swing.JTextField timeout;
    private javax.swing.JRadioButton unreliable;

}
