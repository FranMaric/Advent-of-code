#include <stdio.h>
#include <stdlib.h>

#define MAXCHAR 1000
#define length 6

int main()
{
    FILE *fp;
    char str[MAXCHAR];
    char *filename = "C:\\Users\\fran-\\Desktop\\Advent-of-code\\2020-but-in-C\\input.txt";

    fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("Could not open file %s", filename);
        return 1;
    }
    int brojevi[length];
    int i = 0;

    while (fgets(str, MAXCHAR, fp) != NULL)
    {
        brojevi[i] = atoi(str);
        i++;
    }
    fclose(fp);

    for (int i = 0; i < length; i++)
    {
        for (int j = 0; j < length; j++)
        {
            for (int k = 0; k < length; k++)
            {
                if (brojevi[i] + brojevi[j] + brojevi[k] == 2020 && i != j && i != k && j != k)
                {
                    printf("%d", brojevi[i] * brojevi[j] * brojevi[k]);
                    return 0;
                }
            }
        }
    }
    return 0;
}