#include <iostream>
#include <vector>

int main(){
    std::vector<std::vector<int>> a(3, std::vector<int>(3));  // покАЧТО 3 на 3!
    a[0][0] = 1;
    std::cout << a[0][0];
    return 0;
}