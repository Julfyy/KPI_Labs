
#include <iostream>
#include "String.h"
#include "SymbolString.h"
#include "Rhombus.h"
#include "Circle.h"


int main() {
    //Task 1
    String first = String("this is a regular string");
    cout << first.Sentence << endl;
    cout << first.GetLength() << endl;


    SymbolString second = SymbolString("this is a symbol string");
    cout << second.Sentence << endl;
    second.Sort();
    cout << second.Sentence << endl;
    cout << second.GetLength() << endl;


    //Task 2
    float coord[4][2] = {{0,0},{2,0}, {3,2}, {1,2}};
    Rhombus rhombus = Rhombus(coord);
    cout << rhombus.GetPerimeter() << endl;
    cout << rhombus.GetArea() << endl;

    Circle circle = Circle(3);
    cout << circle.GetArea() << endl;
    cout << circle.GetPerimeter() << endl;

    return 0;
}
