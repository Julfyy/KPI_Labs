//
// Created by bohdan on 07.04.20.
//

#include "String.h"



String::String(string str)
{
    Sentence = str;
}

int String::GetLength()
{
    return Sentence.length();
}