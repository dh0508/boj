#include <bits/stdc++.h>
using namespace std;

int main() {
    int N; cin >> N;
    vector<int>v(N);
    for (int i=0; i<N; i++) {
        cin >> v[i];
    }
    int ans = 0;
    for (int i=N-2; i>=0; i--) {
        if (v[i] >= v[i+1]) {
            ans += v[i] - (v[i+1]-1);
            v[i] = v[i+1]-1;
        }
    }
    cout << ans;
    return 0;
}