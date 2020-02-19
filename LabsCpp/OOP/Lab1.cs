using System;
using System.ComponentModel;
using System.Net.Http.Headers;
using Microsoft.VisualBasic.CompilerServices;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Add(4, 5));
            Console.WriteLine(Compare(7, 5));
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


        static bool Compare(int x, int y)
        {
            
            int sign = Add(x, Add(~y, 1));
            sign >>= 31;
            return sign == 0;
        }
    }
}