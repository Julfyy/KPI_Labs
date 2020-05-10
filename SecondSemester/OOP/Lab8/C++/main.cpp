#include <iostream>
using namespace std;

int GetCharIndex(char symbol, string line);

int main() {
    int (*functionPointer) (char, string);

    functionPointer = GetCharIndex;

    cout << functionPointer('l', "hello") << endl;
    return 0;

}


int GetCharIndex(char symbol, string line) {

    for (int i = line.length() - 1; i >= 0; i--)
    {
        if (line.at(i) == symbol)
        {
            return i;
        }
    }
    return -1;
}
