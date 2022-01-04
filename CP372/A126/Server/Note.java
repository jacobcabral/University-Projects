public class Note {
    int x;
    int y;
    int width;
    int height;
    String color;
    String message;
    boolean status;

    public Note(int x, int y,int width, int height, String color,
      String message, boolean status) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.color = color;
        this.message = message;
        this.status = status;
    }

    public String getNoteProperties() {

        String properties = "";

        properties += "(x,y): " + String.valueOf(x) + ", " + String.valueOf(y) + "|";
        properties += "width, height: " + String.valueOf(width) + ", " + String.valueOf(height) + "|";
        properties += "Color: " + color + "|";
        properties += "Message: " + message + "|";
        properties += "Pinned: " + String.valueOf(status);

        return properties;
    }
}