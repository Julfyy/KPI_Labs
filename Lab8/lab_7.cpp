#include <iostream>
#include <iomanip>

using namespace std;

typedef int Matrix[10][10];
void inputArray(Matrix matr, int n);
void outputArray(Matrix matr, int j);
bool magicSquare(Matrix matr, int n);

int main()
{
    int n;
    Matrix A;

    cout << "Insert number of lines and columns in matrix: \n";
    cin >> n;
    cout << "Initialize matrix\n";
    inputArray(A, n);

    cout << "Your matrix looks like this:\n";
    outputArray(A, n);
    if (magicSquare(A, n))
    {
        cout << "It`s a magic matrix!\n";
    }
    else
    {
        cout << "It`s not a magic matrix\n";
    }
}

void inputArray(Matrix matr, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> matr[i][j];
        }
    }
}

void outputArray(Matrix matr, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {

            cout << setw(4) << matr[i][j];
        }
        cout << endl;
    }
}

bool magicSquare(Matrix matr, int n)
{
    int summEtalon = 0, summDiagonal1 = 0, summDiagonal2 = 0;

    for (int i = 0; i < n; i++)
    {
        summEtalon += matr[0][i];
    }

    for (int i = 0; i < n; i++)
    {
        int lineSumm = 0, summColumn = 0;
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                summDiagonal1 += matr[i][j];
            }
            if (i + j == n - 1)
            {
                summDiagonal2 += matr[i][j];
            }

            lineSumm += matr[i][j];
            summColumn += matr[j][i];
        }


        if (lineSumm != summEtalon)
        {
            return false;
        }
        if (summColumn != summEtalon)
        {
            return false;
        }
    }

    if (summDiagonal1 != summEtalon || summDiagonal2 != summEtalon)
    {
        return false;
    }
    return true;
}