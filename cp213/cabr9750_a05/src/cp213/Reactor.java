package cp213;

import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.util.Random;

/**
 * A simple nuclear reactor simulation. Given a starting temperature and control
 * rods heights, attempt to control the reactor over a period of time.
 *
 * @author -- your name here --
 * @author David Brown
 * @version 2020-11-25
 *
 */
public class Reactor {

    // ---------------------------------------------------------------
    /**
     * Enumerated type for the Reactor status. The reactor is assumed to be in
     * OPERATING mode at the beginning of the simulation.
     */
    public enum Status {
	FINISHED("Finished"), MELTDOWN("MELTDOWN!!"), OPERATING("Operating"), SHUTDOWN("Shutdown");

	private String statusString;

	Status(final String statusString) {
	    this.statusString = statusString;
	}

	@Override
	public String toString() {
	    return this.statusString;
	}
    }

    // ---------------------------------------------------------------
    // Public Constants.
    // ?C - Room temperature.
    public static final double MIN_TEMP = 25;
    // ?C - Meltdown if exceeded.
    public static final double MAX_TEMP = 1000;
    // Minimum temperature at which power is generated.
    public static final double MIN_POWER_TEMP = 100;
    // Maximum power in Mw output at maximum temperature.
    public static final double MAX_POWER = 800;
    // Lengths of rods in cm.
    public static final int ROD_LENGTH = 200;
    // Temperature multiplier per tick.
    public static final double TEMP_FACTOR = 1.125;
    // Range of temperature decrease/increase.
    public static final int RAND_HIGH = 3;
    public static final int RAND_LOW = -3;

    // Private Constants.
    // Power calculation factor. Multiplies current temperature.
    private static final double POWER_FACTOR = MAX_POWER / (MAX_TEMP - MIN_POWER_TEMP);

    /**
     * Calculates and returns the temperature random factor.
     *
     * @return value
     */
    private static int randomFactor() {
	final int value = new Random().nextInt(RAND_HIGH - RAND_LOW + 1) + RAND_LOW;
	return value;
    }

    // Allows views to listen to generic changes in the model.
    private final PropertyChangeSupport pcs = new PropertyChangeSupport(this);
    private double power = 0;
    private boolean rodsChanged = false;
    private int rodsHeight = 0;
    private Status status = Status.OPERATING;
    private double temperature = 0;
    private int ticks = 0;
    private long totalPower = 0;
    private long totalTemperature = 0;

    /**
     * Reactor constructor.
     *
     * @param initialTemperature The initial temperature of the reactor.
     * @param initialRodsHeight  The initial heights of the reactor control rods.
     */
    public Reactor(final double initialTemperature, final int initialRodsHeight) {
	this.temperature = initialTemperature;
	this.rodsHeight = initialRodsHeight;
	// Initialze the total temperature to the current temperature.
	this.totalTemperature = (long) this.temperature;
	// Calculate the initial power level.
	this.power = this.temperature >= MIN_POWER_TEMP ? (long) ((this.temperature - 100) * POWER_FACTOR) : 0;
	// Initialize the total power to the current power.
	this.totalPower = (long) this.power;
    }

    // ---------------------------------------------------------------
    /**
     * Attaches listeners to the model.
     *
     * @param listener The listener to attach to the model.
     */
    public void addPropertyChangeListener(final PropertyChangeListener listener) {
	this.pcs.addPropertyChangeListener(listener);
    }

    /**
     * Attaches listeners to the model for a particular property.
     *
     * @param propertyName The name of the property to listen for.
     * @param listener     The listener to attach to the model.
     */
    public void addPropertyChangeListener(final String propertyName, final PropertyChangeListener listener) {
	this.pcs.addPropertyChangeListener(propertyName, listener);
    }

    /**
     * Drops the rods entirely into the reactor core - i.e. set the rods lengths to
     * the maximum rods lengths.
     */
    public void dropRods() {
	this.rodsHeight = ROD_LENGTH;
	this.status = Reactor.Status.SHUTDOWN;
	this.rodsChanged = true;
    }

    /**
     * Returns the average power produced by the reactor since the start of a
     * simulation.
     *
     * @return average power.
     */
    public double getAveragePower() {
	return this.totalPower / (this.ticks + 1);
    }

    /**
     * Returns the average temperature of the reactor since the start of a
     * simulation.
     *
     * @return average temperature.
     */
    public double getAverageTemperature() {
	return this.totalTemperature / (this.ticks + 1);
    }

    /**
     * Returns the reactor's current power level.
     *
     * @return power.
     */
    public double getPower() {
	return this.power;
    }

    /**
     * Returns the reactor's current rod heights.
     *
     * @return rodsHeight.
     */
    public int getRodsHeight() {
	return this.rodsHeight;
    }

    /**
     * Returns the reactor's current status.
     *
     * @return status.
     */
    public Status getStatus() {
	return this.status;
    }

    /**
     * Returns the reactor's current temperature.
     *
     * @return temperature.
     */
    public double getTemperature() {
	return this.temperature;
    }

    /**
     * Returns the number of ticks since the beginning of a simulation.
     *
     * @return ticks
     */
    public int getTicks() {
	return this.ticks;
    }

    /**
     * Lower the rod heights by one step. Rods cannot be lowered by more than one
     * step per tick.
     */
    public void lowerRods() {

	if (!this.rodsChanged) {
	    this.rodsHeight = Math.min(Math.max(0, this.rodsHeight + 1), ROD_LENGTH);
	    this.rodsChanged = true;
	}
    }

    /**
     * Sets reactor status to FINISHED.
     */
    public void quit() {
	this.status = Status.FINISHED;
	return;
    }

    /**
     * Raise the rod heights by one step. Rods cannot be raised by more than one
     * step per tick.
     */
    public void raiseRods() {

	if (!this.rodsChanged) {
	    this.rodsHeight = Math.min(Math.max(0, this.rodsHeight - 1), ROD_LENGTH);
	    this.rodsChanged = true;
	}
    }

    /**
     * Increment the simulation tick by one. Update the reactor temperature, power,
     * and status (in that order), and allow the rods to be raised or lowered during
     * this tick.
     */
    public void tick() {

	if (this.status == Status.OPERATING) {
	    this.ticks++;
	    this.updateTemperature();
	    this.updatePower();
	    this.updateStatus();
	    this.rodsChanged = false;
	    this.pcs.firePropertyChange(null, false, true);
	}
    }

    /**
     * Updates the current reactor power level.
     */
    private void updatePower() {

	if (this.temperature < MIN_POWER_TEMP) {
	    this.power = 0;
	} else {
	    this.power = (this.temperature - 100) * POWER_FACTOR;
	}
	this.totalPower += this.power;
	return;
    }

    /**
     * Updates the current reactor status.
     */
    private void updateStatus() {

	if (this.temperature >= MAX_TEMP) {
	    this.status = Status.MELTDOWN;
	} else if (this.temperature <= MIN_TEMP) {
	    this.status = Status.SHUTDOWN;
	}
	return;
    }

    /**
     * Updates the current reactor temperature.
     */
    private void updateTemperature() {
	this.temperature = this.temperature * TEMP_FACTOR - this.rodsHeight + randomFactor();
	this.totalTemperature += this.temperature;
	return;
    }
}