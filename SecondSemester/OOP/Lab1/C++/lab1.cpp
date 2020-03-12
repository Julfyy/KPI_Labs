#include <iostream>

using namespace std;
int Add(int,int);
void Compare(int, int, int &c);

int main()
{
    cout << Add(4, 5) << endl;
    int c;
    Compare(3, 6, c);
    cout << c << endl;

    return 0;
}

int Add(int x, int y)
{
    while (y != 0)
    {
        int carry = x & y;
        x = x ^ y;
        y = carry << 1;
    }

    return x;
}

void Compare(int x, int y, int &c)
{
    int sign = Add(x, Add(~y, 1));
    sign >>= 31;
    c = !sign;
}
