
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class lab1_dm {
    public static int n, m;

    public static void main(String[] args) throws IOException {
        int[][] array = readFile();
        System.out.print("The file is read, graph looks like this: ");
        outputArray(array);
        System.out.println("If you want to see incident matrix, type \'i\'.\nFor adjacency matrix, type \'a\'.\n" +
                "For power of dots, type \'p\'.\nFor isolated dots, type \'s\'.\nFor hanged dots, type  \'h\'.\n" +
                "To quit, type \'q\'.");
        Scanner in = new Scanner(System.in);
        boolean bool = true;
        while (bool) {
            String letter = in.next();

            if (letter.contains("i")) {
                System.out.print("Incident matrix: ");
                outputArray(createIncidentMatrix(array));
            }
            if (letter.contains("a")) {
                System.out.print("Adjacency matrix: ");
                outputArray(createAdjacencyMatrix(array));
            }
            if (letter.contains("p")) {
                System.out.print("Power of each node: ");
                outputArray(powerOfNodes(createAdjacencyMatrix(array)));
            }
            if (letter.contains("s")) {
                System.out.print("Isolated nodes are number ");
                for (int i = 0; i < n; i++) {
                    if (isolatedDots(powerOfNodes(createAdjacencyMatrix(array)))[i] != 0)
                        System.out.print(isolatedDots(powerOfNodes(createAdjacencyMatrix(array)))[i] + "\t");
                }
                System.out.println();

            }
            if (letter.contains("h")) {
                System.out.print("\nHanged nodes are number ");
                for (int i = 0; i < n; i++) {
                    if (hangedDots(powerOfNodes(createAdjacencyMatrix(array)))[i] != 0)
                        System.out.println(hangedDots(powerOfNodes(createAdjacencyMatrix(array)))[i] + "\t");
                }

            }
            if (letter.contains("q")){
                bool = false;
            }
        }

    }


    private static int[][] readFile() throws IOException {
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
        System.out.println("\n");
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


    public static int[][] powerOfNodes(int[][] array) {
        int[][] arrayPowerOfDots = new int[n][2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arrayPowerOfDots[i][0] = i + 1;
                arrayPowerOfDots[i][1] += array[i][j];
            }
        }

        return arrayPowerOfDots;
    }

    public static int[] isolatedDots(int[][] array) {
        int[] arrayIsolatedDots = new int[n];
        for (int i = 0; i < n; i++) {
            if (array[i][1] == 1)
                arrayIsolatedDots[i] = i + 1;
        }
        return arrayIsolatedDots;
    }

    public static int[] hangedDots(int[][] array) {
        int[] arrayHangedDots = new int[n];
        for (int i = 0; i < n; i++) {
            if (array[i][1] == 0)
                arrayHangedDots[i] = i + 1;
        }
        return arrayHangedDots;
    }
}


