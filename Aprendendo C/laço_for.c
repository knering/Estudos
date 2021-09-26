#include <stdio.h>

int main () {

    int var;
    int soma = 0;

    for (int i=0; i < 4; i++){

        printf ("Insira o valor %i: \n", i);
        scanf ("%i", &var);
        soma = soma + var;
    }
    printf("A soma e: %i", soma);

    return 0;
}