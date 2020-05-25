//
// Created by bohdan on 19.05.20.
//

#ifndef LAB7_LINKEDLIST_H
#define LAB7_LINKEDLIST_H

#include <iostream>
#include "Node.h"
using namespace std;


class LinkedList {
private:
    Node* _head = nullptr;
    Node* GetLastNode();

public:
    int GetLength();
    double GetMeanValue();
    void InsertLast(short newData);
    short GetByIndex(int index);
    int GetNumberOfMultiples(int number);
    void ReplaceWithZeroIfMoreThen(double value);
    string ToString();
};


#endif //LAB7_LINKEDLIST_H
