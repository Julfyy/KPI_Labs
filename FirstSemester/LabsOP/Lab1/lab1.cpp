#include <iostream>
using namespace std;

int main (){
    float firstElement, numberOfFirstElement, secondElement, numberOfSecondElement, d, n, sum, element1;
    cout << "Initialize your progression. Input number and value of two elements:" << endl;
    cout << "Element №"; cin >> numberOfFirstElement;
    cout << "Value: "; cin >> firstElement;
    cout << "Element №"; cin >> numberOfSecondElement;
    cout << "Value: "; cin >> secondElement;
    cout << "Enter amount of elements to sum" << endl; cin >> n;
    
    
    d = (secondElement-firstElement)/(numberOfSecondElement-numberOfFirstElement);
    element1 = firstElement - d*(numberOfFirstElement-1);
    sum = ((2*element1 + d*(n-1))*n)/2;

    cout << "Sum is " << sum << endl;

    return 0;
}