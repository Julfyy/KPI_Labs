//
// Created by bohdan on 27.04.20.
//

#ifndef LAB6_EXPRESSION_H
#define LAB6_EXPRESSION_H


class Expression {
private:
    double _result;
    double _a;
    double _b;
    double _c;

public:
    Expression(double, double, double);
    void set_A(double);
    double get_A();
    void set_B(double);
    double get_B();
    void set_C(double);
    double get_C();
    void Calculate();
    double getResult();


};


#endif //LAB6_EXPRESSION_H
