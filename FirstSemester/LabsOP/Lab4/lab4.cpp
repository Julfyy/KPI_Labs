#include <iostream>
#include <math.h>

using namespace std;


int main ()
{
    cout << "Insert n" << endl;
    int n; cin >> n;
    long double res = 0;

	for (int i = 0; i < n; i++)
    {
        res = sqrtl(2.0 + res);
        cout << res << endl;
    }
	
}
