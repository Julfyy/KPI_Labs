#include <iostream>

using namespace std;
int Add(int,int);
bool Compare(int, int);

int main()
{
    cout << Add(4, 5) << endl;
    cout << Compare(9, 8) << endl;
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

bool Compare(int x, int y)
{
    int temp = Add(x, Add(~y, 1));
    temp >>= 31;

    
    

    return !temp;

}
