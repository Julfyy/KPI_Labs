#include <iostream>
#include "Vector.h"

using namespace std;

int main() {
    //Angles presented as Pi products (Pi = 3.14 = 180 degrees), e.q. 180 = 3.14, 360 = 6.28, 90 = 1.57,  etc
    cout << "____Task 1, create 3 objects via 3 different constructors\n";
    Vector Z1 = Vector(); //using default constructor
    Vector Z2 = Vector(1, 3.14); //using params
    Vector Z3 = Vector(Z2);//copying

    cout << "Vector 1: angle ="  <<  Z1.PolarAngle <<  ", radius = " <<  Z1.PolarRadius << endl;
    cout << "Vector 2: angle ="  <<  Z2.PolarAngle <<  ", radius = " <<  Z2.PolarRadius << endl;
    cout << "Vector 3: angle ="  <<  Z3.PolarAngle <<  ", radius = " <<  Z3.PolarRadius << endl;



    cout <<  "\n____Task 2, increase radius of Z3 by 2\n";
    Z3 = Z3 * 2;
    cout << "Vector 3: angle ="  <<  Z3.PolarAngle <<  ", radius = " <<  Z3.PolarRadius << endl;

    cout <<  "\n____Task 3, Z3 by 90 deg\n";
    Z3.Rotate(1.57);
    cout << "Vector 3: angle ="  <<  Z3.PolarAngle <<  ", radius = " <<  Z3.PolarRadius << endl;

    cout << "\n____Task 4, Z1 = Z2 + Z3\n";
    Z1 = Z2 + Z3;
    cout << "Vector 1: angle ="  <<  Z1.PolarAngle <<  ", radius = " <<  Z1.PolarRadius << endl;
    return 0;
}
