#include <stdio.h>

int main (){ 

    int base;
    int altura;

    printf("Digite o valor da base: ");
    scanf ("%i", &base);
    printf("Digite a altura: ");
    scanf ("%i", &altura);

    int area = base * altura;

    printf ("A area e: %i", area);

    return 0;
}