using System;

namespace Lab6
{
    class Program
    {
        static void Main(string[] args)
        {
            Expression[] expressionsArray = new Expression[3];
            
            try
            {
                expressionsArray[0] = new Expression(1.2, 5, 12);
                expressionsArray[1] = new Expression(-0.5, 5, 1.0);
                expressionsArray[2] = new Expression(-541.4444, -23, 3215.15);
                
                expressionsArray[0].Calculate();
                expressionsArray[1].Calculate();
                expressionsArray[2].Calculate();
                
                Console.WriteLine("First expression equals to: " + expressionsArray[0].GetResult());
                Console.WriteLine("Second expression equals to: " + expressionsArray[1].GetResult());
                Console.WriteLine("Third expression equals to: " + expressionsArray[2].GetResult());
            }
            catch (DivideByZeroException er)
            {
                Console.WriteLine(er.Message);
            }
            catch (ArgumentOutOfRangeException er)
            {
                Console.WriteLine(er.Message);
            }
        }
    }
}