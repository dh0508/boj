#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);
    if (s.find("d2") != string::npos || s.find("D2") != string::npos) {
        cout << "D2";
    }
    else {
        cout << "unrated";
    }

    return 0;
}