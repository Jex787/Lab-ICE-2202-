#include <iostream>
using namespace std;

void tower_of_hanoi(int n, char source, char destination, char auxiliary) {
    if (n == 1) {
        cout << "Move disk 1 from " << source << " to " << destination << endl;
        return;
    }
    tower_of_hanoi(n-1, source, auxiliary, destination);
    cout << "Move disk " << n << " from " << source << " to " << destination << endl;
    tower_of_hanoi(n-1, auxiliary, destination, source);
}

int main() {
    int n;
    cout << "Enter the number of disks: ";
    cin >> n;
    tower_of_hanoi(n, 'A', 'C', 'B');
    return 0;
}
