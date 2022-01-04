/**
 *
 * @author Jake
 */
public class frame extends javax.swing.JFrame {


    public frame() {
        initComponents();
    }


    @SuppressWarnings("unchecked")
 
    private void initComponents() {

        jDialog1 = new javax.swing.JDialog();
        getexecute = new javax.swing.JButton();
        jButton10 = new javax.swing.JButton();
        criteria = new javax.swing.JTextField();
        jLabel3 = new javax.swing.JLabel();
        jDialog2 = new javax.swing.JDialog();
        pinexecute = new javax.swing.JButton();
        jButton12 = new javax.swing.JButton();
        jLabel4 = new javax.swing.JLabel();
        piny = new javax.swing.JSpinner();
        pinx = new javax.swing.JSpinner();
        jLabel5 = new javax.swing.JLabel();
        jDialog3 = new javax.swing.JDialog();
        unpinexecute = new javax.swing.JButton();
        jButton14 = new javax.swing.JButton();
        jLabel6 = new javax.swing.JLabel();
        unpiny = new javax.swing.JSpinner();
        unpinx = new javax.swing.JSpinner();
        jLabel7 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        ip = new javax.swing.JTextField();
        connect = new javax.swing.JButton();
        get = new javax.swing.JButton();
        pin = new javax.swing.JButton();
        unpin = new javax.swing.JButton();
        shake = new javax.swing.JButton();
        clear = new javax.swing.JButton();
        jLabel1 = new javax.swing.JLabel();
        status = new javax.swing.JLabel();
        postmessage = new javax.swing.JTextField();
        disconnect = new javax.swing.JButton();
        post = new javax.swing.JButton();

        jDialog1.setMinimumSize(new java.awt.Dimension(485, 180));

        getexecute.setText("GET NOTES");
        getexecute.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                getexecuteActionPerformed(evt);
            }
        });

        jButton10.setText("CLOSE");
        jButton10.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton10ActionPerformed(evt);
            }
        });

        criteria.setFont(new java.awt.Font("Tahoma", 0, 12)); 
        criteria.setText("Enter Search Criteria");

        jLabel3.setFont(new java.awt.Font("Tahoma", 0, 14)); 
        jLabel3.setText("GET");

        javax.swing.GroupLayout jDialog1Layout = new javax.swing.GroupLayout(jDialog1.getContentPane());
        jDialog1.getContentPane().setLayout(jDialog1Layout);
        jDialog1Layout.setHorizontalGroup(
            jDialog1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jDialog1Layout.createSequentialGroup()
                .addGroup(jDialog1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jDialog1Layout.createSequentialGroup()
                        .addGap(55, 55, 55)
                        .addComponent(getexecute, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(70, 70, 70)
                        .addComponent(jButton10, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jDialog1Layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 31, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jDialog1Layout.createSequentialGroup()
                        .addGap(130, 130, 130)
                        .addComponent(criteria, javax.swing.GroupLayout.PREFERRED_SIZE, 202, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(90, Short.MAX_VALUE))
        );
        jDialog1Layout.setVerticalGroup(
            jDialog1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jDialog1Layout.createSequentialGroup()
                .addComponent(jLabel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGap(29, 29, 29)
                .addComponent(criteria, javax.swing.GroupLayout.PREFERRED_SIZE, 29, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addGroup(jDialog1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(getexecute, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton10, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );

        jDialog2.setMinimumSize(new java.awt.Dimension(485, 180));

        pinexecute.setText("PIN NOTE");
        pinexecute.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                pinexecuteActionPerformed(evt);
            }
        });

        jButton12.setText("CLOSE");
        jButton12.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton12ActionPerformed(evt);
            }
        });

        jLabel4.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        jLabel4.setText("PIN");

        jLabel5.setText("The Coordinates are entered as (x,y)");

        javax.swing.GroupLayout jDialog2Layout = new javax.swing.GroupLayout(jDialog2.getContentPane());
        jDialog2.getContentPane().setLayout(jDialog2Layout);
        jDialog2Layout.setHorizontalGroup(
            jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jDialog2Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jLabel4, javax.swing.GroupLayout.PREFERRED_SIZE, 31, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(108, 108, 108)
                .addComponent(jLabel5)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jDialog2Layout.createSequentialGroup()
                .addGap(64, 64, 64)
                .addGroup(jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(pinexecute, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(pinx, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 78, Short.MAX_VALUE)
                .addGroup(jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(piny, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton12, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(73, 73, 73))
        );
        jDialog2Layout.setVerticalGroup(
            jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jDialog2Layout.createSequentialGroup()
                .addGroup(jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jLabel5))
                .addGap(20, 20, 20)
                .addGroup(jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(piny, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(pinx, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(jDialog2Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(pinexecute, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton12, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );

        jDialog3.setMinimumSize(new java.awt.Dimension(485, 180));

        unpinexecute.setText("UNPIN NOTE");
        unpinexecute.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                unpinexecuteActionPerformed(evt);
            }
        });

        jButton14.setText("CLOSE");
        jButton14.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton14ActionPerformed(evt);
            }
        });

        jLabel6.setFont(new java.awt.Font("Tahoma", 0, 14)); // NOI18N
        jLabel6.setText("UNPIN");

        jLabel7.setText("The Coordinates are entered as (x,y)");

        javax.swing.GroupLayout jDialog3Layout = new javax.swing.GroupLayout(jDialog3.getContentPane());
        jDialog3.getContentPane().setLayout(jDialog3Layout);
        jDialog3Layout.setHorizontalGroup(
            jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jDialog3Layout.createSequentialGroup()
                .addGroup(jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jDialog3Layout.createSequentialGroup()
                        .addContainerGap()
                        .addComponent(jLabel6, javax.swing.GroupLayout.PREFERRED_SIZE, 53, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(106, 106, 106)
                        .addComponent(jLabel7))
                    .addGroup(jDialog3Layout.createSequentialGroup()
                        .addGap(78, 78, 78)
                        .addGroup(jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(unpinexecute, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(unpinx, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(60, 60, 60)
                        .addGroup(jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jButton14, javax.swing.GroupLayout.PREFERRED_SIZE, 135, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(unpiny, javax.swing.GroupLayout.PREFERRED_SIZE, 67, javax.swing.GroupLayout.PREFERRED_SIZE))))
                .addContainerGap(77, Short.MAX_VALUE))
        );
        jDialog3Layout.setVerticalGroup(
            jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jDialog3Layout.createSequentialGroup()
                .addGroup(jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jLabel7))
                .addGap(20, 20, 20)
                .addGroup(jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(unpiny, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(unpinx, javax.swing.GroupLayout.PREFERRED_SIZE, 38, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(18, 18, 18)
                .addGroup(jDialog3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(unpinexecute, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jButton14, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jTextArea1.setEditable(false);
        jTextArea1.setLineWrap(true);
        jTextArea1.setWrapStyleWord(true);
        jTextArea1.setTabSize(4);
        jTextArea1.setColumns(20);
        jTextArea1.setRows(5);
        jScrollPane1.setViewportView(jTextArea1);

        ip.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        ip.setText("Enter IP here");
        ip.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ipActionPerformed(evt);
            }
        });

        connect.setText("Connect");
        connect.setToolTipText("Connect to the server");
        connect.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                connectActionPerformed(evt);
            }
        });

        get.setText("Get");
        get.setToolTipText("Get Specific Note");
        get.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                getActionPerformed(evt);
            }
        });

        pin.setText("Pin");
        pin.setToolTipText("Pin a note to the board");
        pin.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                pinActionPerformed(evt);
            }
        });

        unpin.setText("Unpin");
        unpin.setToolTipText("Unpin a note from the board");
        unpin.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                unpinActionPerformed(evt);
            }
        });

        shake.setText("Shake");
        shake.setToolTipText("Remove all unpinned notes");
        shake.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                shakeActionPerformed(evt);
            }
        });

        clear.setText("Clear");
        clear.setToolTipText("");
        clear.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                clearActionPerformed(evt);
            }
        });

        jLabel1.setFont(new java.awt.Font("Tahoma", 0, 12)); 
        jLabel1.setText("Current Status:");

        status.setFont(new java.awt.Font("Tahoma", 0, 12)); 
        status.setText("DISCONNECTED");

        postmessage.setFont(new java.awt.Font("Tahoma", 0, 12)); 

        disconnect.setText("Disconnect");
        disconnect.setToolTipText("Disconnect from the server");
        disconnect.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                disconnectActionPerformed(evt);
            }
        });

        post.setText("Post");
        post.setToolTipText("Posts note in text field");
        post.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                postActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                            .addComponent(clear, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGap(20, 20, 20))
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                            .addComponent(connect, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, 130, Short.MAX_VALUE)
                            .addComponent(get, javax.swing.GroupLayout.Alignment.LEADING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(pin, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(unpin, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(shake, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)))
                    .addComponent(ip, javax.swing.GroupLayout.PREFERRED_SIZE, 174, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 93, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(status))
                    .addComponent(disconnect, javax.swing.GroupLayout.PREFERRED_SIZE, 130, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 42, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 292, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(post, javax.swing.GroupLayout.PREFERRED_SIZE, 122, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(postmessage, javax.swing.GroupLayout.PREFERRED_SIZE, 170, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(ip, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(postmessage, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel1)
                            .addComponent(status))
                        .addGap(18, 18, 18)
                        .addComponent(connect, javax.swing.GroupLayout.PREFERRED_SIZE, 32, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(disconnect, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(13, 13, 13)
                        .addComponent(get, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(pin, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(unpin, javax.swing.GroupLayout.PREFERRED_SIZE, 33, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(shake, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(clear, javax.swing.GroupLayout.PREFERRED_SIZE, 30, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 12, Short.MAX_VALUE)
                        .addComponent(post, javax.swing.GroupLayout.PREFERRED_SIZE, 40, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 280, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap())))
        );

        pack();
    }

    private void pinActionPerformed(java.awt.event.ActionEvent evt) {
        jDialog2.setVisible(true);
    }

    private void ipActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:
    }

    private void getexecuteActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot send GET command:\nconnection to server required.");
        }

        else {

            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);

            String get_args = criteria.getText();
            

            try {
                String get_result = Client.sendGetRequest(ip_address, port_number, get_args);

                String[] results = get_result.split("\n");

                jTextArea1.setText("");
                for (String result : results) {
                    jTextArea1.append(result);
                    jTextArea1.append("\t");
                }

                //jTextArea1.setText(get_result);
                jDialog1.setVisible(false); //turning off the popup


            } catch (Exception e) {
                e.printStackTrace();
            }

        }

    }

    private void pinexecuteActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot send PIN command:\nconnection to server required.");
        }

        else {
            
            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);

            Integer pin_x_coord = (Integer) pinx.getValue();
            Integer pin_y_coord = (Integer) piny.getValue();

            String pin_args = String.valueOf((pin_x_coord.intValue())) + " " + String.valueOf( (pin_y_coord.intValue()) );

            try {
                String pin_result = Client.sendPinRequest(ip_address, port_number, pin_args);
                jTextArea1.setText(pin_result);
                jDialog2.setVisible(false); //turn off the popup window

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    private void unpinexecuteActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot send UNPIN command:\nconnection to server required.");
        }

        else {
            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);

            Integer unpin_x_coord = (Integer) unpinx.getValue();
            Integer unpin_y_coord = (Integer) unpiny.getValue();

            String unpin_args = String.valueOf((unpin_x_coord.intValue())) + " " + String.valueOf( (unpin_y_coord.intValue()) );

            try {
                String unpin_result = Client.sendUnpinRequest(ip_address, port_number, unpin_args);
                jTextArea1.setText(unpin_result);
                jDialog3.setVisible(false); //turn off popup window

            } catch (Exception e) {
                e.printStackTrace();
            }
        }

    }

    private void jButton14ActionPerformed(java.awt.event.ActionEvent evt) {
        jDialog3.setVisible(false);
    }

    private void getActionPerformed(java.awt.event.ActionEvent evt) {
        jDialog1.setVisible(true);
    }

    private void unpinActionPerformed(java.awt.event.ActionEvent evt) {
        jDialog3.setVisible(true);
    }

    private void postActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot send POST command:\nconnection to server required.");
        }


        else {
            String post_args = postmessage.getText();

            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);
            try {
                String post_result = Client.sendPostRequest(ip_address, port_number, post_args);
                jTextArea1.setText(post_result);
                postmessage.setText("");

            } catch (Exception e) {
                e.printStackTrace();
                jTextArea1.setText("Error processing POST command.");
            }
        }
         

    }

    private void clearActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot send CLEAR command:\nconnection to server required.");
        }

        else {

            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);

            try{
                String clear_result = Client.sendClearRequest(ip_address, port_number);
                jTextArea1.setText(clear_result);

            } catch (Exception e) {
                e.printStackTrace();
            }
        }


    }

    private void shakeActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot send SHAKE command:\nconnection to server required.");
        }

        else {

            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);

            try {
                String shake_result = Client.sendShakeRequest(ip_address, port_number);
                jTextArea1.setText(shake_result);

            } catch (Exception e) {
                e.printStackTrace();
            }

        }
    }

    private void connectActionPerformed(java.awt.event.ActionEvent evt) {
        // TODO add your handling code here:

        if (ip.getText().contains(":") == false) {
            jTextArea1.setText("IP address invalid:\nmust be of the format 'address:port'");
        }

        else {
            //seperate ip address from port number
            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);
            try{
                String connect_attempt = Client.sendConnectionRequest(ip_address, port_number);
                jTextArea1.setText(connect_attempt);
                status.setText("CONNECTED");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        
        
        
    }

    private void disconnectActionPerformed(java.awt.event.ActionEvent evt) {                                           
        
        if (status.getText() == "DISCONNECTED") {
            jTextArea1.setText("Cannot disconnect:\nno connection established.");
        }
        
        else {

            String[] connection_args = ip.getText().split(":");
            String ip_address = connection_args[0];
            int port_number = Integer.parseInt(connection_args[1]);

            try {
                String disconnect = Client.sendDisconnectRequest(ip_address, port_number);
                jTextArea1.setText(disconnect);
                status.setText("DISCONNECTED");
            } catch (Exception e) {
                e.printStackTrace();
            }

        }

    }

    private void jButton10ActionPerformed(java.awt.event.ActionEvent evt) {
        jDialog1.setVisible(false);
    }

    private void jButton12ActionPerformed(java.awt.event.ActionEvent evt) {
        jDialog2.setVisible(false);
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
  
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(frame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }


        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new frame().setVisible(true);
            }
        });
    }

 
    private javax.swing.JButton clear;
    private javax.swing.JButton connect;
    private javax.swing.JTextField criteria;
    private javax.swing.JButton disconnect;
    private javax.swing.JButton get;
    private javax.swing.JButton getexecute;
    private javax.swing.JTextField ip;
    private javax.swing.JButton jButton10;
    private javax.swing.JButton jButton12;
    private javax.swing.JButton jButton14;
    private javax.swing.JDialog jDialog1;
    private javax.swing.JDialog jDialog2;
    private javax.swing.JDialog jDialog3;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JTextArea jTextArea1;
    private javax.swing.JButton pin;
    private javax.swing.JButton pinexecute;
    private javax.swing.JSpinner pinx;
    private javax.swing.JSpinner piny;
    private javax.swing.JButton post;
    private javax.swing.JTextField postmessage;
    private javax.swing.JButton shake;
    private javax.swing.JLabel status;
    private javax.swing.JButton unpin;
    private javax.swing.JButton unpinexecute;
    private javax.swing.JSpinner unpinx;
    private javax.swing.JSpinner unpiny;

}
