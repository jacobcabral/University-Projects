package cp213;

import java.awt.Color;
import java.awt.Graphics;

/**
 * Horizontal bar view of the reactor average temperature.
 *
 * @author -- your name here --
 * @version 2020-11-25
 */
@SuppressWarnings("serial")
public class AverageTemperatureView extends BarView {

    private Reactor model = null;


    public AverageTemperatureView(Reactor model) {
        super(Color.RED, Reactor.MAX_TEMP);
        this.model = model;
    }

    @Override
    public void paintComponent(Graphics g) {
        this.modelValue = this.model.getAverageTemperature();
        super.paintComponent(g);
    }
}