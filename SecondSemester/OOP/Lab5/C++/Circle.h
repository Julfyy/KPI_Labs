//
// Created by bohdan on 07.04.20.
//

#ifndef C___CIRCLE_H
#define C___CIRCLE_H


#include "Figure.h"

class Circle : Figure {

private:
    float Radius;
public:
    Circle(float radius);
    double GetArea() override;
    double GetPerimeter() override;

};


#endif //C___CIRCLE_H
