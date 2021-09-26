#include <stdlib.h>

int main(){
    int v1, numInvertido=0, resto;
    printf("Insira o valor a ser invertido: ");
    scanf ("%i", &v1);

    while (v1%10>0){
        resto = v1%10;
        v1 = (v1-resto)/10;
        numInvertido = numInvertido*10 + resto;
    }
    numInvertido = numInvertido + v1/10;
    printf("Resultado final: %i\n", numInvertido);
    return 0;
}