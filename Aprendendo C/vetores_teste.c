#include <stdio.h>

int main (void){ 

    int vetor[5];
    int total=0;
    float media;

    for(int i=0; i<5; i++){
        scanf("%i", &vetor[i]);
        
    }
    for(int j=0; j<5; j++){
        total += vetor[j];
    }
    media = total/5;
    printf("%f", media);
}