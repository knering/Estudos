#include <stdio.h>

int main() {
    int v1, v2;

    printf ("Insira os valores: ");
    scanf ("%i %i", &v1, &v2);

    if (v2 == 0){
        printf ("Divisão inválida");
    }
    if (v1 % v2 == 0){
        printf("Resulta em valor inteiro");
    }
    else 
        printf("Não resulta em valor inteiro");

    return 0;
}