using System;
using System.Net.Http.Headers;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Add(4,5));
            Console.WriteLine(Compare(6, 5));

        }

        static int Add(int x, int y)
        {
            while (y != 0)
            {
                int carry = x & y;

                x = x ^ y;

                y = carry << 1;
            }

            return x;
        }
        
        
        static Boolean Compare(int x, int y)
        {
            int temp = Add(x, Add(~y, 1));
            temp >>= 31;

            return !temp;
        }
        
    }
}