// test.c
#include <stdio.h>
#include <stdlib.h>
#define MAX_LEN 10

char shift_char(char, int);
char *shift_str(char*, int);

int main(void)
{
    char buffer[MAX_LEN + 1];
    char *first;
    char *last;
    int age,days;
    printf("What is your first name? ");
    fgets(buffer, MAX_LEN + 1, stdin);
    buffer[strlen(buffer) - 1] = '\0';
    printf("How old are you? ");
    scanf("%d", &age);
    first = shift_str(buffer,age);
    printf("Your first name, encrypted by your age, is %s\n",first);
    days = 365*age;
    printf("%s, as a person who is at least %d days old", first,days);
    printf(", you should be able to decrypt this!\n");
    return 0;
}

char shift_char(char ch, int n)
{
    if('a' <= ch && ch <= 'z')
        return 'a' + (n + ch - 'a') % 26;
    else if('A' <= ch && ch <= 'Z')
        return 'A' + (n + ch - 'A') % 26;
    else return ch;
}

char *shift_str(char* plaintext,int n)
{
    int i,len;
    char ciphertext[MAX_LEN+1];
    len = strlen(plaintext);
    for(i = 0; i < MIN(len,MAX_LEN) ; i++)
    {
        ciphertext[i] = shift_char(plaintext[i],n);
    }
    ciphertext[i] = '\0';
    return ciphertext;
}
