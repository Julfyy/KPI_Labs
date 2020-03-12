#include <iostream>
using namespace std;

float signA (float argument) {
    if (argument < 0) {
        return -1;
    }
    else if (argument == 0) {
        return 0;
    }
    else {
        return 1;
    }
}

int main () {

    float x,y,z;
    cout << "Input x and y:\n";
    cin >> x >> y;

    z = (signA (x) + signA (y))* signA (x+y);

    cout << "z equals " << z << endl;

}