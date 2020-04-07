//
// Created by bohdan on 07.04.20.
//

#ifndef C___SYMBOLSTRING_H
#define C___SYMBOLSTRING_H

#include <iostream>
#include <algorithm>
#include "String.h"

using namespace std;

class SymbolString : public String{
public:
    SymbolString(string str);
    void Sort();
};


#endif //C___SYMBOLSTRING_H
