#include <stdio.h>

int main (){

    int fat;
    int result = 1;
    printf ("Insira o fatorial a calcular: ");
    scanf ("%i\n", &fat);
    continue
    for (int i = 1; i<=fat; i++){
        result *= i;
    }
    printf ("Resultado: %i", result);

    return 0; 
}