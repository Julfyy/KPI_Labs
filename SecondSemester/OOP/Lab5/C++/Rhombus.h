//
// Created by bohdan on 07.04.20.
//

#ifndef C___RHOMBUS_H
#define C___RHOMBUS_H


#include "Figure.h"

class Rhombus : public Figure {
private:
    float _nodeCoordinates[4][2];
    double _sideLength;
    double _firstDiagonalLength;
    double _secondDiagonalLength;
    void CalculateSides();
    void CalculateDiagonals();

public:
    double GetArea() override;
    double GetPerimeter() override;
    Rhombus(float nodeCoordinates[4][2]);
};


#endif //C___RHOMBUS_H
