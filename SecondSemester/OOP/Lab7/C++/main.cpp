#include <iostream>
#include "LinkedList.h"

int main() {
    LinkedList* linkedList = new LinkedList();

    linkedList->InsertLast(5);
    linkedList->InsertLast(15);
    linkedList->InsertLast(7);

    //cout << linkedList->GetByIndex(2) << endl;
    cout << linkedList->GetNumberOfMultiples(1) << endl;
    cout << linkedList->GetMeanValue() << endl;

    //linkedList->ReplaceWithZeroIfMoreThen(5);
    cout << linkedList->ToString() << endl;

    return 0;
}
