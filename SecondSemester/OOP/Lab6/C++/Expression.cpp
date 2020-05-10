//
// Created by bohdan on 27.04.20.
//

#include <stdexcept>
#include "Expression.h"
#include "cmath"

using namespace std;

Expression::Expression(double a, double b, double c) {
    set_A(a);
    set_B(b);
    set_C(c);
}

void Expression::Calculate() {
    if ((this->_a * this->_b + 2) <= 0) {
        throw std::invalid_argument("Log(a * b + 2) has only positive range of argument values");;
    }
    if ((41 - (this->_b / this->_c) + 1) == 0) {
        throw std::range_error("Division by zero is impossible!");;
    }
    this->_result = (log(this->_a * this->_b + 2) * 2) / (41 - (this->_b / this->_c) + 1);
}


double Expression::getResult() {
    return this->_result;
}

void Expression::set_A(double a) {
    this->_a = a;
}
void Expression::set_B(double b) {
    this->_b = b;
}
void Expression::set_C(double c) {
    if (c == 0) {
        throw std::invalid_argument("Division by zero has occurred!");
    }
    this->_c = c;
}

double Expression::get_A() {
    return this->_a;
}
double Expression::get_B() {
    return this->_b;
}
double Expression::get_C() {
    return this->_c;
}