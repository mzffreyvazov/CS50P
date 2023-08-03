  #include <cs50.h>
  #include <stdio.h>

int main(void)
  {
      int a = get_int("Row: ");
      int b = get_int("Column: ");
      for (int i = 0; i < b; i++)
      {
        for (int j = 0; j < a; j++)
        {
            printf("#");
        }
        printf("\n");

      }
  }