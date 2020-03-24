//
// Created by bohdan on 24.03.20.
//

#ifndef LAB3_VECTOR_H
#define LAB3_VECTOR_H


class Vector {
public:
    double PolarRadius;
    double PolarAngle;
    Vector();
    Vector (double polarRadius, double polarAngle);
    Vector(Vector const &vec);
    void Rotate(double angle);
    Vector operator + (Vector const &v);
    Vector operator * (int scalar);



private:
    double pi;

};


#endif //LAB3_VECTOR_H
