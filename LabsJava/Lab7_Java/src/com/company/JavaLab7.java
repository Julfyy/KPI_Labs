package com.company;

import java.util.Arrays;
import java.util.Scanner;


public class JavaLab7 {

    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {

        System.out.println("Insert volume of array and insert elements (float): ");
        int n = in.nextInt();
        float[] array = initArray(n);

        System.out.println("Your array looks like this: ");
        outArray(array);

        System.out.println("\nYour array looks like this after sorting:");

        array = sortArrayByDescending(array);
        outArray(array);

        System.out.println("\nSumm of even elements is: " + summArray(array) + " \n");

    }

    public static float[] initArray(int n) {
        float[] array = new float[n];

        for (int i = 0; i < n; i++) {
            array[i] = in.nextFloat();

        }
        return array;
    }

    public static float[] sortArrayByDescending(float[] array) {
        Arrays.sort(array);

        float[] newArray = new float[array.length];

        for (int i = 0, j = array.length - 1; i < array.length; i++, j--) {
            newArray[i] = array[j];
        }
        return newArray;
    }

    public static void outArray(float[] array) {
        for (float i : array) System.out.println(i);
    }

    public static float summArray(float[] array) {
        float summ = 0;
        for (int i = 0; i < array.length; i += 2) {
            summ += array[i];
        }
        return summ;
    }


}
