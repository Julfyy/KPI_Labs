#include <iostream>
#include <math.h>
#include <stdlib.h>
using namespace std;

float rowK(float x)
{
	float a_k, summ = 0;

	for (int k = 10;; k++)
	{
		a_k = x / (sqrt(k) * (k + 2));

		if (a_k < pow(10, -4))
		{
			break;
		}
		else
		{
			cout << "\ta_" << k << "= " << a_k << endl;
			summ = summ + a_k;
		}
	}

	cout << "Sum is " << summ << endl;
	return 0;
}

int main()
{
	float x;
	cout << "Enter x value\n";
	cin >> x;

	rowK(x);
}
