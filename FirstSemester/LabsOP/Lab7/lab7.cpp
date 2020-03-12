#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <algorithm>
using namespace std;
/*
30. Заданий масив Y(n), дійсних чисел, серед яких є і від'ємні.
Упорядкувати елементи за зменшенням
та знайти суму тих елементів упорядкованого масиву Y,
що знаходяться на парних позиціях.
Виконав: Шибецький Богдан
*/

void initArray(float *p, int number_of_elements);
void outputArray(float *p, int number_of_elements);
void sortArray(float *p, int number_of_elements);
float summArray(float *p, int number_of_elements);

int main()
{
    const int n = 7;
    float array[n], *p;

    srand(time(0));
    initArray(array, n);
    cout << "Array looks like this" << endl;
    outputArray(array,n);
    sortArray(array, n);
    cout << "\nArray is sorted" << endl;
    outputArray(array, n);
    
    cout << "Summ is " << summArray(array,n) << endl;
    return 0;
}

void initArray(float *p, int number_of_elements)
{
    for (int i = 0; i < number_of_elements; i++)
    {
        p[i] = -10 + static_cast<float>(rand()) / static_cast<float>(RAND_MAX / 20);
    }
}

void outputArray(float *p, int number_of_elements)
{
    for (int i = 0; i < number_of_elements; i++)
    {
        cout << p[i] << endl;
    }
}

void sortArray(float *p, int number_of_elements)
{
    sort(p, p + number_of_elements, greater<float>());
}

float summArray(float *p, int number_of_elements)
{
    float summ = 0;
    for (int i = 0; i < number_of_elements; i += 2)
    {
        summ += p[i];
    }
    return summ;
}
