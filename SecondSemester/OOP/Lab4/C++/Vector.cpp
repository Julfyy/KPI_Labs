#include "Vector.h"
//
// Created by bohdan on 24.03.20.
//

#include "Vector.h"

Vector::Vector() {
    PolarRadius = 0.0;
    PolarAngle = 0.0 * pi;
}

//Constructor with params
Vector::Vector(double polarRadius, double polarAngle) {
    PolarRadius = polarRadius;
    PolarAngle = polarAngle;
}

//Constructor for copying
Vector::Vector(Vector const &vec) {
    PolarRadius = vec.PolarRadius;
    PolarAngle = vec.PolarRadius;
}



void Vector::Rotate(double angle) {
    //Rotating clockwise is adding a positive angle, and counterclockwise is adding a negative one
    PolarAngle += angle;
}

Vector Vector::operator + (Vector const &v)
{
    return Vector(PolarAngle + v.PolarAngle, PolarRadius + v.PolarRadius);
}

Vector Vector::operator * (int scalar)
{
    return Vector(PolarRadius * scalar, PolarAngle);
}