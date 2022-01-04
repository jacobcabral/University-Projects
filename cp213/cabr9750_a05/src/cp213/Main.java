package cp213;

import javax.swing.JFrame;

/**
 * @author -- your name here --
 * @author David Brown
 * @version 2020-11-25
 *
 */
public class Main {

    public static void main(String[] args) {
	Main main = new Main();
	main.RunReactorController(400, 50);
    }

    /**
     * Run the Reactor model with an automatic controller given an initial
     * temperature and an initial rod lengths.
     *
     * @param initialTemperature Initial reactor temperature.
     * @param initialRodsHeight  Initial reactor rods heights.
     */
    public void RunReactorController(final int initialTemperature, final int initialRodsHeight) {
	Reactor model = new Reactor(initialTemperature, initialRodsHeight);
	ReactorControllerView view = new ReactorControllerView(model);

	final JFrame f = new JFrame("Reactor");
	f.setContentPane(view);
	f.setSize(500, 400);
	f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	f.setVisible(true);
	ReactorController rc = new ReactorController(model);
	rc.run();
    }

}