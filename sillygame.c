#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main ()
{
srand(time(0));

int number = rand() % 10 +1;
int guess;

printf("Silly game! Guess number between 1 and 10; ");
scanf("%d", &guess);

if (guess == number) 
{
printf("You Won!\n");
}
else{
printf("You Lost! ezzzz ^_^\n");
}
return 0;
}
