//
// Created by bohdan on 07.04.20.
//

#include "SymbolString.h"

SymbolString::SymbolString(string str) : String(str)
{
}

void SymbolString::Sort() {
    std::sort(Sentence.begin(), Sentence.end());
    std::reverse(Sentence.begin(), Sentence.end());
};