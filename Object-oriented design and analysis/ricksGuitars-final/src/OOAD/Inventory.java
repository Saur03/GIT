package OOAD;

import java.util.ArrayList;

public class Inventory {
  private ArrayList<Guitar> guitars;

  public Inventory() {
    guitars = new ArrayList<>();
  }

  public void addGuitar(String serialNumber, double price,
                        GuitarSpec spec) {
    Guitar guitar = new Guitar(serialNumber, price, spec);
    guitars.add(guitar);
  }

  public Guitar getGuitar(String serialNumber) {
    for (Guitar guitar : guitars) {
      if (guitar.getSerialNumber().equals(serialNumber)) {
        return guitar;
      }
    }
    return null;
  }

  public ArrayList<Guitar> search(GuitarSpec searchSpec) {
    ArrayList<Guitar> matchingGuitars = new ArrayList<>();
    for (Guitar guitar : guitars) {
      if (guitar.getSpec().matches(searchSpec))
        matchingGuitars.add(guitar);
    }
    return matchingGuitars;
  }
}
