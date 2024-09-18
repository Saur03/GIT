package OOAD;

import java.util.ArrayList;
import java.util.Scanner;

public class Saurabh_POS_Store {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // set up Saurabh POS inventory
        Inventory inventory = new Inventory();
        initializeInventory(inventory);

        GuitarSpec whatErinLikes = new GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER);

        ArrayList<Guitar> matchingGuitars = inventory.search(whatErinLikes);
        if (!matchingGuitars.isEmpty()) {
            System.out.println("Erin, you might like these guitars:");
            for (Guitar guitar : matchingGuitars) {
                GuitarSpec spec = guitar.getSpec();
                System.out.println("  We have a " +
                        spec.getBuilder() + " " + spec.getModel() + " " +
                        spec.getType() + " guitar:\n     " +
                        spec.getBackWood() + " back and sides,\n     " +
                        spec.getTopWood() + " top.\n  You can have it for only $" +
                        guitar.getPrice() + "!\n  ----");
            }
        } else {
            System.out.println("Sorry, Erin, we have nothing for you.");
        }

        // list to store purchased guitars
        ArrayList<Guitar> purchasedGuitars = new ArrayList<>();
        double runningTotal = 0.0;

        while(true) {
            System.out.println("Enter the UPC/Serial Number of the guitar to purchase (or type 'done' to finish):");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("done")) {
                break;
            }
            Guitar guitar = inventory.getGuitar(input);
            if (guitar != null) {
                purchasedGuitars.add(guitar);
                runningTotal += guitar.getPrice();

                // Display product info and running total
                System.out.println("Added to cart: " + guitar.getSpec().getModel() + " by " + guitar.getSpec().getBuilder() +
                        " for $" + guitar.getPrice());
                System.out.println("Running total: $" + runningTotal);
            } else {
                System.out.println("Sorry, no guitar found with UPC/Serial Number: " + input);
            }
        }
        // Display final transaction summary
        if (!purchasedGuitars.isEmpty()) {
            double taxAmount = runningTotal * 0.07;
            double grandTotal = runningTotal + taxAmount;

            System.out.println("\n--- Transaction Summary ---");
            for (Guitar guitar : purchasedGuitars) {
                System.out.println(guitar.getSpec().getBuilder() + " " + guitar.getSpec().getModel() + ": $" + guitar.getPrice());
            }
            System.out.println("Subtotal: $" + runningTotal);
            System.out.println("Tax (7%): $" + taxAmount);
            System.out.println("Grand Total: $" + grandTotal);

            // Handle payment
            System.out.println("Enter the payment amount: ");
            double payment = scanner.nextDouble();

            if (payment < grandTotal) {
                System.out.println("Insufficient payment. Please enter an amount greater than or equal to the grand total.");
            } else {
                double change = payment - grandTotal;
                System.out.println("Payment successful. Change: $" + change);
            }

            System.out.println("Thank you for your purchase!");
        } else {
            System.out.println("No items purchased.");
        }

        scanner.close();
    }




    private static void initializeInventory(Inventory inventory) {
        inventory.addGuitar("11277", 3999.95, new GuitarSpec(Builder.COLLINGS, "CJ", Type.ACOUSTIC, 6, Wood.INDIAN_ROSEWOOD, Wood.SITKA));
        inventory.addGuitar("V95693", 1499.95, new GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER));
        inventory.addGuitar("V9512", 1549.95, new GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, 6, Wood.ALDER, Wood.ALDER));
        inventory.addGuitar("122784", 5495.95, new GuitarSpec(Builder.MARTIN, "D-18", Type.ACOUSTIC, 6, Wood.MAHOGANY, Wood.ADIRONDACK));
        inventory.addGuitar("76531", 6295.95, new GuitarSpec(Builder.MARTIN, "OM-28", Type.ACOUSTIC, 6, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK));
        inventory.addGuitar("70108276", 2295.95, new GuitarSpec(Builder.GIBSON, "Les Paul", Type.ELECTRIC, 6, Wood.MAHOGANY, Wood.MAHOGANY));
        inventory.addGuitar("82765501", 1890.95, new GuitarSpec(Builder.GIBSON, "SG '61 Reissue", Type.ELECTRIC, 6, Wood.MAHOGANY, Wood.MAHOGANY));
        inventory.addGuitar("77023", 6275.95, new GuitarSpec(Builder.MARTIN, "D-28", Type.ACOUSTIC, 6, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK));
        inventory.addGuitar("1092", 12995.95, new GuitarSpec(Builder.OLSON, "SJ", Type.ACOUSTIC, 12, Wood.INDIAN_ROSEWOOD, Wood.CEDAR));
        inventory.addGuitar("566-62", 8999.95, new GuitarSpec(Builder.RYAN, "Cathedral", Type.ACOUSTIC, 12, Wood.COCOBOLO, Wood.CEDAR));
        inventory.addGuitar("6 29584", 2100.95, new GuitarSpec(Builder.PRS, "Dave Navarro Signature", Type.ELECTRIC, 6, Wood.MAHOGANY, Wood.MAPLE));
    }

    // 1. add the UPC code in the menu
    // 2. if a customer give less amount as compared to the total amount of the items, ask him to give remaining bucks.
}





