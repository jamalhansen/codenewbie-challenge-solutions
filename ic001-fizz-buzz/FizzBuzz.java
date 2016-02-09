/* Fizz Buzz solution in Java
 * might not be the most efficient Java solution
 * would love to see a better way to do this in Java */
class FizzBuzz
{
    /* The entry point to a Java program will have the following entry point*/
    public static void main(String[] args)
    {
        /* Start our loop, it uses an integer in the variable i
         * and it will continue while i <= 100
         * and it will iterate the value of i with each pass through the loop */
        for(int i = 1; i <= 100; i++)
        {
            /* Initialize a boolean variable to false, it will be set to true
             * if the number is divisible by 3 or 5 */
            boolean fizzBuzz = false;

            /* Evaluate fizz */
            if(i % 3 == 0)
            {
                fizzBuzz = true;
                System.out.print("fizz");
            }

            /* Evaluate buzz */
            if(i % 5 == 0)
            {
                fizzBuzz = true;
                System.out.print("buzz");
            }

            /* If neither fizz nor buzz, output the number */
            if(!fizzBuzz)
            {
                System.out.print(i);
            }

            /* Output a new line */
            System.out.print("\n");
        }
    }
}
