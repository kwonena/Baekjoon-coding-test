#include <stdio.h>

int main() {
    int a, b;

    while(1) {
        printf("Press two number : ");
        scanf("%d %d", &a, &b);

        if(a == 0 && b == 0) break;

        printf("Sum : %d\n", a + b);
    }
}
