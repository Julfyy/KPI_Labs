//
// Created by bohdan on 07.04.20.
//

#include "Circle.h"
#include "math.h"



Circle::Circle(float radius)
{
    Radius = radius;
}

double Circle::GetArea()
{
    return M_PI* pow(Radius, 2);
}

double Circle::GetPerimeter()
{
    return 2 * M_PI * Radius;
}

