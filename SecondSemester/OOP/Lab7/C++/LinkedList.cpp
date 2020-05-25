//
// Created by bohdan on 19.05.20.
//


#include "LinkedList.h"

void LinkedList::InsertLast(short newData)
{
    Node* newNode = new Node(newData);
    if (_head == nullptr)
    {
        _head = newNode;
        return;
    }
    Node* lastNode = GetLastNode();
    lastNode->next = newNode;
}

Node* LinkedList::GetLastNode()
{
    Node* temp = _head;
    while (temp->next != nullptr)
    {
        temp = temp->next;
    }
    return temp;
}

short LinkedList::GetByIndex(int index)
{
    Node* current = _head;
    int count = 0;
    while (current != nullptr)
    {
        if (count == index)
        {
            return current->data;
        }
        count++;
        current = current->next;
    }
    throw std::out_of_range("Index out of range");
}

int LinkedList::GetLength() {
    Node* temp = _head;
    int lastIndex = 0;
    while (temp->next != nullptr) {
        temp = temp->next;
        lastIndex++;
    }
    return lastIndex;
}

int LinkedList::GetNumberOfMultiples(int number)
{
    int counter = 0;
    for (int i = 0; i <= this->GetLength(); i++)
    {
        if (GetByIndex(i) % number == 0)
        {
            counter++;
        }
    }
    return counter;
}

double LinkedList::GetMeanValue()
{
    short sum = 0;
    for (int i = 0; i <= GetLength(); i++)
    {
        sum += GetByIndex(i);
    }

    return (float) sum / GetLength();
}

void LinkedList::ReplaceWithZeroIfMoreThen(double value)
{
    Node* current = _head;
    while (current != nullptr)
    {
        if (current->data > value)
        {
            current->data = 0;
        }

        current = current->next;
    }
}
string LinkedList::ToString()
{
    Node* current = _head;
    string stringArray = "";
    while (current != nullptr)
    {
        stringArray += to_string(current->data);
        stringArray += " ";
        current = current->next;
    }

    return stringArray;
}







#include "LinkedList.h"
