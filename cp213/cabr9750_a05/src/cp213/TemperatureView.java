package cp213;

import java.awt.Color;
import java.awt.Graphics;

/**
 * Horizontal bar view of current reactor temperature.
 *
 * @author -- your name here --
 * @version 2020-11-25
 */
@SuppressWarnings("serial")
public class TemperatureView extends BarView {

    private Reactor model = null;

    public TemperatureView(Reactor model) {
        super(Color.CYAN, Reactor.MAX_TEMP);
        this.model = model;
    }

    @Override
    public void paintComponent(Graphics g) {
        this.modelValue = this.model.getTemperature();
        super.paintComponent(g);
    }

}