import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;


public class lab2_dm {
    public static int n, m;


    public static void main(String[] args) throws IOException {
        int[][] array = readFile();
        Scanner in = new Scanner(System.in);
        int [][] adjMatr = createAdjacencyMatrix(array);

        System.out.print("The file is read, graph looks like this: ");
        outputArray(array);
        System.out.println("The graph is oriented? (y/n)");
        String answer = in.nextLine();
        if (answer.contains("n")){
            adjMatr = findSymmetricalMatrix(createAdjacencyMatrix(array));
        }
        System.out.print("Adjacency");
        outputArray(adjMatr);
        System.out.print("Path matrix  looks like this: ");
        outputArray(createPathMatrix(findSymmetricalMatrix(adjMatr)));
        System.out.print("Reach matrix  looks like this: ");
        outputArray(createReachMatrix(adjMatr));
        if (answer.contains("n")) {
            System.out.println("Diameter  is: " + findDiameter(createPathMatrix(createAdjacencyMatrix(array))));
            System.out.println("Center node is: " + findCenter(createPathMatrix(createAdjacencyMatrix(array))));
            System.out.println("Radius is: " + findRadius(createPathMatrix(findSymmetricalMatrix(createAdjacencyMatrix(array)))));
        }


    }



    public static int findRadius(int[][] pathMatr) {
        int radius = 0;
        radius = Arrays.stream(pathMatr[findCenter(findSymmetricalMatrix(pathMatr)).get(0)]).min().getAsInt();
        if (radius == 0)
            return radius + 1;

        return radius;
    }

    public static int findDiameter(int[][] pathMatr) {
        int[] diameter = new int[n];
        for (int i = 0; i < n; i++)
            diameter[i] = Arrays.stream(pathMatr[i]).max().getAsInt();

        return Arrays.stream(diameter).max().getAsInt();
    }

    public static int[][] findSymmetricalMatrix(int[][] matrix) {
        int[][] symmetricalMatr = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 1) {
                    symmetricalMatr[i][j] = matrix[i][j];
                    symmetricalMatr[j][i] = matrix[i][j];
                }

            }
        }
        return symmetricalMatr;
    }

    public static ArrayList<Integer> findCenter(int[][] pathMatr) {
        ArrayList<Integer> center = new ArrayList<>();

        int[] maxInLine = new int[n];
        for (int j = 0; j < n; j++) {
            int max = pathMatr[j][0];
            for (int k = 0; k < n; k++) {
                if (max < pathMatr[j][k]) {
                    max = pathMatr[j][k];
                }
            }
            maxInLine[j] = max;
        }
        int min = maxInLine[0];
        for (int elements : maxInLine) {
            if (min > elements) {
                min = elements;
            }
        }

        for (int i = 0; i < n; i++) {
            if (min == maxInLine[i]) {
                center.add(i + 1);
            }
        }
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
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int counter = n - 1; counter >= 1; counter--) {
                    if (i == j)
                        pathMatrix[i][j] = 0;
                    else if (powerMatrix(adjacencyMatr, counter)[i][j] != 0)
                        pathMatrix[i][j] = counter;
                }
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
        Scanner sc = new Scanner(new FileReader("/home/bohdan/GitHubRepositories/KPI_Labs/LabsJava/labs_dm/input.txt"));
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

    public static int[][] createAdjacencyMatrix(int[][] array) {

        int[][] adjacencyMatrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int k = 0; k < array.length; k++)
                adjacencyMatrix[array[k][0] - 1][array[k][1] - 1] = 1;
        }
        return adjacencyMatrix;
    }
    public static int[][] findTransposedMatrix(int[][] matr) {
        int[][] transposedMatr = new int[matr.length][matr[0].length];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                transposedMatr[i][j] = matr[j][i];

            }
        }
        return transposedMatr;

    }
}

