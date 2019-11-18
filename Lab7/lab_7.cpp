#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int n = 7;
float array[n], *p;

void initArray(float *);
void outputArray(float *);
float summArray(float *);

int main()
{
    initArray(array);
    outputArray(array);
    summArray(array);
    return 0;
}

void initArray(float *p)
{
    srand(time(0));
    for (int i = 0; i <= n; i++)
    {
        *p = -10 + static_cast<float>(rand()) / static_cast<float>(RAND_MAX / 20);
        p++;
    }
}

void outputArray(float *p)
{
    cout << "Array looks like this\n";
    for (int i = 0; i <= n; i++)
    {
        cout << *(p + i) << endl;
    }
    sort(array, array + n, greater<float>());
    cout << "\nArray looks like this after sorting\n";
    for (int i = 0; i < n; i++)
    {
        cout << *(p + i) << endl;
    }
}

float summArray(float *p)
{
    float summ = 0;
    for (int i = 2; i < n; i += 2)
    {
        summ += *(p + i);
    }
    cout << "\nSumm is " << summ << endl;
    return 0;
}
