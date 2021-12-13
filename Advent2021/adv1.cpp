#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int x=0, up=0, a=0, b=0, c=0, d=0, ac=0, bc=0, cc=0, dc=0, counter=1;
    cout << "Hello World!\n";
    ifstream inFile;
    inFile.open("C:\\Users\\allut\\Documents\\adv1.txt");
    while (inFile >> x) {
        /*cout << "a: " << a << " ac: " << ac << "\n";
        cout << "b: " << b << " bc: " << bc << "\n";
        cout << "c: " << c << " cc: " << cc << "\n";
        cout << "d: " << b << " dc: " << dc << "\n";*/
        switch (counter){
        case 1:
            a += x;
            ac++; counter++;
            break;
        case 2:
            a += x; b += x;
            ac++; bc++; counter++;
            break;
        case 3:
            a += x; b += x; c += x;
            ac++; bc++; cc++; counter++;
            break;
        case 4:
            b += x; c += x; d += x;
            bc++; cc++; dc++; counter++;
            break;
        case 5:
            a += x; c += x; d += x;
            ac++; cc++; dc++; counter++;
            break;
        case 6:
            a += x; b += x; d += x;
            ac++; bc++; dc++;
            counter = 3;
            break;
        }
        if ((ac == 3) && (bc == 3)) {
            cout << "a: " << a << " ac: " << ac << "\n";
            cout << "b: " << b << " bc: " << bc << "\n";
            if (b > a) { up++; }
            ac = 0; a = 0;
        }
        if ((bc == 3) && (cc == 3)) {
            cout << "b: " << b << " bc: " << bc << "\n";
            cout << "c: " << c << " cc: " << cc << "\n";
            if (c > b) { up++; }
            bc = 0; b = 0;
        }
        if ((cc == 3) && (dc == 3)) {
            cout << "c: " << c << " cc: " << cc << "\n";
            cout << "d: " << b << " dc: " << dc << "\n";
            if (d > c) { up++; }
            cc = 0; c = 0;
        }
        if ((dc == 3) && (ac == 3)) {
            cout << "d: " << b << " dc: " << dc << "\n";
            cout << "a: " << a << " ac: " << ac << "\n";
            if (a > d) { up++; }
            dc = 0; d = 0;
        }
    }
    cout << up;
}

