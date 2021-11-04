#include <stdio.h>

int main() {
    int num;
    
    printf("Press a number : ");
    scanf("%d", &num);

    int arr[num];
    printf("Press array number : ");
    for(int i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
    }

    int min = arr[0];
    int max = arr[0];

    for(int j = 0; j < num; j++) {
        if(arr[j] > max) max = arr[j];
        if(arr[j] < min) min = arr[j];
    }
    printf("max : %d, min : %d\n", max, min);
}
