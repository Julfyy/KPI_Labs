using System;

namespace Lab5
{
    class Program
    {
        static void Main(string[] args)
        {
            
            //Task 1
            String first = new String("this is a regular string");
            Console.WriteLine(first.Sentence);
            Console.WriteLine(first.GetLength());
            
            
            SymbolString second = new SymbolString("this is a symbol string");
            Console.WriteLine(second.Sentence);
            second.Sort();
            Console.WriteLine(second.Sentence);
            Console.WriteLine(second.GetLength());
            
            //Task 2
            Rhombus rhombus = new Rhombus(new float[,] {{0,0},{2,0}, {3,2}, {1,2}});
            Console.WriteLine(rhombus.GetPerimeter());
            Console.WriteLine(rhombus.GetArea());
            
            Circle circle = new Circle(3);
            Console.WriteLine(circle.GetArea());
            Console.WriteLine(circle.GetPerimeter());

        }
    }
}