package cp213;

import cp213.Reactor.Status;

/**
 * A class to control a Reactor model. It's job is to initialize a Reactor and
 * maximize its power output while avoiding a meltdown.
 *
 * @author -- your name here --
 * @author David Brown
 * @version 2020-11-25
 */
public class ReactorController implements Runnable {

    private static final int MAX_VARIANCE = 4;
    // The reactor to control.
    private Reactor model = null;

    /**
     * Constructor.
     *
     * @param model The reactor model.
     */
    public ReactorController(Reactor model) {
	this.model = model;
    }

    /**
     * Update the rods depending on the reactor's current state.
     */
    private void updateModel() {
	// Calculate the next possible temperatures.
	double current = this.model.getTemperature();
	double maxNextTempRodUp = current * Reactor.TEMP_FACTOR - this.model.getRodsHeight() + 1 + Reactor.RAND_HIGH;
	double maxNextTempRodDown = current * Reactor.TEMP_FACTOR - this.model.getRodsHeight() - 1 + Reactor.RAND_HIGH;
	double minNextTempRodDown = current * Reactor.TEMP_FACTOR - this.model.getRodsHeight() - 1 + Reactor.RAND_LOW;

	if (maxNextTempRodDown >= Reactor.MAX_TEMP) {
	    // Possible meltdown!
	    this.model.dropRods();
	} else if (current >= 900) {
	    this.model.lowerRods();
	} else if (current <= 300) {
	    this.model.raiseRods();
	} else if (maxNextTempRodUp - current >= MAX_VARIANCE) {
	    this.model.lowerRods();
	} else if (minNextTempRodDown - current <= -MAX_VARIANCE) {
	    this.model.raiseRods();
	}
    }

    /*
     * (non-Javadoc)
     *
     * @see java.lang.Runnable#run()
     *
     * Run the reactor control.
     */
    @Override
    public void run() {

	try {
	    while (this.model.getStatus() == Status.OPERATING) {
		this.updateModel();
		this.model.tick();
		Thread.sleep(0);
	    }
	} catch (final InterruptedException e) {
	    // Do Nothing.
	}
    }
}