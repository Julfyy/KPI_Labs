import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;


public class lab2_dm {
    public static int n, m;


    public static void main(String[] args) throws IOException {
        int[][] array = readFile();
        System.out.print("The file is read, graph looks like this: ");
        outputArray(array);


        System.out.print("Path matrix  looks like this: ");
        outputArray(createPathMatrix(createAdjacencyMatrix(array)));
        System.out.print("Reach matrix  looks like this: ");
        outputArray(createReachMatrix(createAdjacencyMatrix(array)));
        System.out.println("Diameter  is: " + findDiameter(createPathMatrix(createAdjacencyMatrix(array))));
        System.out.println("Center is node: " + findCenter(createPathMatrix(createAdjacencyMatrix(array))));


    }
    public static int findDiameter(int[][] pathMatr){
        int diameter = 0;
            for (int i = 0; i < pathMatr.length; i++)
                diameter = Arrays.stream(pathMatr[i]).max().getAsInt();
       return diameter;
    }

    public static int findCenter(int [][] pathMatr){
        int center, minLength = 0, i;
        int[] counter = new int[n];
            for (i = 0; i < pathMatr.length; i++) {
                minLength = Arrays.stream(pathMatr[i]).max().getAsInt();
                if (minLength == 0)
                    minLength++;
                for (int j : pathMatr[i]) {
                    if (pathMatr[i][j] == minLength)
                        counter[i] = i;
                }

            }
        center = Arrays.stream(counter).max().getAsInt();
        return center;
    }
    public static int[][] createReachMatrix(int[][] adjacencyMatr) {
        int[][] reachMatrix = new int[n][n];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (createPathMatrix(adjacencyMatr)[i][j] > 0 || i == j)
                reachMatrix[i][j] = 1;
                else
                    reachMatrix[i][j] = 0;
        return reachMatrix;
    }

    public static int[][] createPathMatrix(int[][] adjacencyMatr) {
        int[][] pathMatrix = new int[n][n];
        for (int i = 0; i < adjacencyMatr.length; i++) {
            for (int j = 0; j < adjacencyMatr.length; j++) {
                if (i == j)
                    pathMatrix[i][j] = 0;
                else if (adjacencyMatr[i][j] == 1)
                    pathMatrix[i][j] = adjacencyMatr[i][j];
                else if (powerMatrix(adjacencyMatr, 2)[i][j] != 0)
                    pathMatrix[i][j] = 2;
                else if (powerMatrix(adjacencyMatr, 3)[i][j] != 0)
                    pathMatrix[i][j] = 3;

            }
        }
        return pathMatrix;
    }

    public static int[][] powerMatrix(int[][] a, int p) {
        int[][] result = a;
        for (int n = 1; n < p; ++n)
            result = multiplyMatrices(result, a);
        return result;
    }

    private static int[][] multiplyMatrices(int[][] a, int[][] b) {
        int temp[][] = new int[a.length][b.length];

        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < a.length; j++) {
                temp[i][j] = 0;
                for (int k = 0; k < a.length; k++) {
                    temp[i][j] += a[i][k] * b[k][j];
                }
            }
        }
        return temp;
    }


    public static int[][] readFile() throws IOException {
        Scanner sc = new Scanner(new FileReader("/home/bohdan/IdeaProjects/lab1_dm/input.txt"));
        n = sc.nextInt();
        m = sc.nextInt();
        int[][] array = new int[m][2];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < 2; j++) {
                array[i][j] = sc.nextInt();
            }
        }
        return array;
    }

    public static void outputArray(int[][] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print("\n");
            for (int j = 0; j < array[0].length; j++) {
                System.out.print(array[i][j] + "\t");
            }
        }
        System.out.println();
    }

    public static int[][] createIncidentMatrix(int[][] array) {
        int[][] incidentMatrix = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i + 1 == array[j][0] && i + 1 == array[j][1]) incidentMatrix[i][j] = 2;
                else if (i + 1 == array[j][0]) incidentMatrix[i][j] = -1;
                else if (i + 1 == array[j][1]) incidentMatrix[i][j] = 1;
                else incidentMatrix[i][j] = 0;
            }
        }
        return incidentMatrix;
    }

    public static int[][] createAdjacencyMatrix(int[][] array) {

        int[][] adjacencyMatrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < array.length; k++)
                adjacencyMatrix[array[k][0] - 1][array[k][1] - 1] = 1;
        }
        return adjacencyMatrix;
    }
}
