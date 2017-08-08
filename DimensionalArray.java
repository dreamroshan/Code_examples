/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package pkg2.dimensional.array;

/**
 *
 * @author Roshan
 */

import java.util.*;

        
public class DimensionalArray {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter # of rows: ");
    int rows = scanner.nextInt();
    System.out.print("Enter # of cols:");
    int cols = scanner.nextInt();
    
    int[][] a = new int[rows][cols];
    
    System.out.print(" Enter " + rows +"x"+ cols +"=" + (rows*cols) + "Integers :" );
    for (int i=0;i<rows;i++)
        for(int j=0;j<cols;j++)
            a[i][j]= scanner.nextInt();
    
    System.out.println("Here are those " + (rows*cols)+"integers in a "+
            rows+"x"+cols +"2d-array:");
    System.out.println(Arrays.deepToString(a));
    }
    
}
