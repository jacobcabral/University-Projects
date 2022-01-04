package cp213;

import java.awt.Color;
import java.awt.Graphics;

/**
 * Horizontal bar view of current reactor rod height.
 *
 * @author -- your name here --
 * @version 2020-11-25
 */
@SuppressWarnings("serial")
public class RodsView extends BarView {

    private Reactor model = null;

    public RodsView(Reactor model) {
        super(Color.GREEN, Reactor.ROD_LENGTH);
        this.model = model;
    }

    @Override
    public void paintComponent(Graphics g) {
        this.modelValue = this.model.getRodsHeight();
        super.paintComponent(g);
    }
}