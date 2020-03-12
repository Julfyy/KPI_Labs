#include <iostream>

using namespace std;

int main()
{
    float a, b, c;
    cout << "Enter a, b, c values:" << endl;
    cin >> a;
    cin >> b;
    cin >> c;

    if (a == b)
        cout << "a and b are equal" << endl;
    else if (b == c)
        cout << "b and c are equal" << endl;
    else if (c == a)
        cout << "a and c are equal" << endl;

        return 0;
}