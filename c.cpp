#include <stdio.h>
#include <string.h>

int main(){

char nome1[30],nome2[30],nome3[30], cpf1[11], cpf2[11], cpf3[11];
unsigned int alturas[3], pesos[3];

//Os dados serão manipulados como sendo do tipo caractere para economia de recursos computacionais.

int t=0; // variavel de controle para o ciclo do-while.

do{
t+=1;

printf("\nInsira seu nome: ");
gets(nome1);
printf("\nInsira sua altura: ");
scanf("%d",&altura[0]);
printf("\nInsira seu peso: ");
scanf("%d",&peso[0]);
printf("\nInsira seu CPF: ");
gets(cpf1);

printf("\n\nDeseja continuar cadastrando (max. 3 usuarios)? (s/n): ");
char c;
scanf("%c",&c);
if (c=='s'){
  t += 1;
}
else{
  t=4;
}} while (t<=3);

};
