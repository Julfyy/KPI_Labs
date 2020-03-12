//
// Source code recreated from a .class file by IntelliJ IDEA
// (powered by Fernflower decompiler)
//

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class lab3_dm {
    public static int n;
    public static int m;

    public lab3_dm() {
    }

    public static void main(String[] args) throws IOException {
        int[][] graph = readFile();
        Scanner in = new Scanner(System.in);
        System.out.println("Graph looks like this: ");
        outputArray(graph);
        System.out.println("Enter start node: ");
        int startNode = in.nextInt();
        BFSsearch(findSymmetricalMatrix(createAdjacencyMatrix(graph)), startNode);
        DFSsearch(findSymmetricalMatrix(createAdjacencyMatrix(graph)), startNode);
    }

    public static ArrayList<Integer> DFSsearch(int[][] adjMatrix, int startNode) {
        ArrayList<Integer> queueArray = new ArrayList();
        ArrayList<Integer> visitedNodes = new ArrayList();
        int DFScounter = 1;
        queueArray.add(startNode);
        System.out.println("Node DFS Queue");
        System.out.println(startNode + "\t" + DFScounter + "\t" + queueArray.toString());
        visitedNodes.add(startNode);

        while(!queueArray.isEmpty()) {
            for(int i = 1; i <= n; ++i) {
                if (adjMatrix[(Integer)queueArray.get(queueArray.size() - 1) - 1][i - 1] == 1 && !visitedNodes.contains(i)) {
                    queueArray.add(i);
                    visitedNodes.add(i);
                    ++DFScounter;
                    System.out.println(i + "\t" + DFScounter + "\t" + queueArray.toString());
                    i = 0;
                }
            }

            queueArray.remove(queueArray.size() - 1);
            System.out.println("-\t-\t" + queueArray.toString());
        }

        return queueArray;
    }

    public static ArrayList<Integer> BFSsearch(int[][] adjMatrix, int startNode) {
        ArrayList<Integer> queueArray = new ArrayList();
        ArrayList<Integer> visitedNodes = new ArrayList();
        int BFScounter = 1;
        queueArray.add(startNode);
        System.out.println("Node BFS Queue");
        System.out.println(startNode + "\t" + BFScounter + "\t" + queueArray.toString());
        visitedNodes.add(startNode);

        while(!queueArray.isEmpty()) {
            for(int i = 1; i <= n; ++i) {
                if (adjMatrix[(Integer)queueArray.get(0) - 1][i - 1] == 1 && !visitedNodes.contains(i)) {
                    queueArray.add(i);
                    visitedNodes.add(i);
                    ++BFScounter;
                    System.out.println(i + "\t" + BFScounter + "\t" + queueArray.toString());
                    i = 0;
                }
            }

            queueArray.remove(0);
            System.out.println("-\t-\t" + queueArray.toString());
        }

        return queueArray;
    }

    public static int[][] createAdjacencyMatrix(int[][] array) {
        int[][] adjacencyMatrix = new int[n][n];

        for(int i = 0; i < n; ++i) {
            for(int k = 0; k < array.length; ++k) {
                adjacencyMatrix[array[k][0] - 1][array[k][1] - 1] = 1;
            }
        }

        return adjacencyMatrix;
    }

    public static int[][] findSymmetricalMatrix(int[][] matrix) {
        int[][] symmetricalMatr = new int[n][n];

        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1) {
                    symmetricalMatr[i][j] = matrix[i][j];
                    symmetricalMatr[j][i] = matrix[i][j];
                }
            }
        }

        return symmetricalMatr;
    }

    public static void outputArray(int[][] array) {
        for(int i = 0; i < array.length; ++i) {
            System.out.print("\n");

            for(int j = 0; j < array[0].length; ++j) {
                System.out.print(array[i][j] + "\t");
            }
        }

        System.out.println();
    }

    public static int[][] readFile() throws IOException {
        Scanner sc = new Scanner(new FileReader("/home/bohdan/GitHubRepositories/KPI_Labs/LabsJava/labs_dm/input.txt"));
        n = sc.nextInt();
        m = sc.nextInt();
        int[][] array = new int[m][2];

        for(int i = 0; i < m; ++i) {
            for(int j = 0; j < 2; ++j) {
                array[i][j] = sc.nextInt();
            }
        }

        return array;
    }
}
