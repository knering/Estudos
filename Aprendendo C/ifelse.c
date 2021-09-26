#include <stdio.h>

int main () {

    int idade;
    printf("Insira sua idade: ");
    scanf("%i", &idade);
    if (idade >18){
        printf("Bebida liberada");
    }
    else 
        printf("Bebida proibida");

    return 0;
}