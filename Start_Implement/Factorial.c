#include <stdio.h>
int factorial(int num);

int main() {
    int num;
    
    printf("Press a number : ");
    scanf("%d", &num);

    printf("%d! : %d", num, factorial(num));
}
int factorial(int num) {
    if(num <= 1) return 1;
    
    return num * factorial(num - 1);
}
