#include <iostream>
#include "Expression.h"

using namespace std;

int main() {
    try {
        Expression expression = Expression(-1.32, 123, 0);
        expression.Calculate();
        cout << expression.getResult() << endl;
    }
    catch (range_error er) {
        cout << er.what() << endl;
    }
    catch (invalid_argument er) {
        cout <<  er.what() << endl;
    }
    return 0;
}
