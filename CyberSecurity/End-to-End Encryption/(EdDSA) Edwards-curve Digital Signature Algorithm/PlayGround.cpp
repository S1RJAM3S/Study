#include <math.h>
#include <iostream>

using namespace std;

int calcAddX(int x1, int y1, int x2, int y2) {
    return int(pow((y2 - y1)/(x2 - x1), 2) - x1 - x2);
}

int calcAddY(int x1, int y1, int x2, int y2) {
    return ((y2 - y1)/(x2 - x1))*(x1 - calcAddX(x1, y1, x2, y2)) - y1;
}
int calcMultX(int x, int y, int a) {
    return int(pow(((3*pow(x,2)+a)/2*y), 2) - 2*x);
}

int calcMultY(int x, int y, int a) {
    return int((3*pow(x, 2) + a)/2*y)*(x - calcMultX(x, y, a)) - y;
}
int main() {
    // y^2 = x^3 + x + 1
    int a = 1;
    int b = 1;
    int Px = 0;
    int Py = 1;
    int skey = 12;
    int pkey_x = calcMultX(Px, Py, a);
    int pkey_y = calcMultY(Px, Py, a);
    cout << pkey_x << " " << pkey_y << "\n";
    for(int i = 0; i < skey; i++) {
        cout << pkey_x << " " << pkey_y << "\n";
        pkey_x = calcMultX(pkey_x, pkey_y, a);
        pkey_y = calcMultY(pkey_x, pkey_y, a);
    }
    cout << pkey_x << " " << pkey_y;
}