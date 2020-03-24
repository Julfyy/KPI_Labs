using System;

namespace Lab4
{
    class Program
    {
        static void Main(string[] args)
        {
                //Angles presented as Pi products (Pi = 3.14 = 180 degrees), e.q. 180 = 3.14, 360 = 6.28, 90 = 1.57,  etc
                Console.WriteLine("____Task 1, create 3 objects via 3 different constructors");
                Vector Z1 = new Vector(); //using default constructor
                Vector Z2 = new Vector(1, 3.14); //using params
                Vector Z3 = new Vector(Z2);//copying

                Console.WriteLine($"Vector 1: angle = {Z1.PolarAngle}, radius = {Z1.PolarRadius}");
                Console.WriteLine($"Vector 2: angle = {Z2.PolarAngle}, radius = {Z2.PolarRadius}");
                Console.WriteLine($"Vector 3: angle = {Z3.PolarAngle}, radius = {Z3.PolarRadius}");

                
                Console.WriteLine("\n____Task 2, increase radius of Z3 by 2");

                Z3 = Z3 * 2;
                Console.WriteLine($"Vector 3: angle = {Z3.PolarAngle}, radius = {Z3.PolarRadius}");
                
                
                Console.WriteLine("\n____Task 3, Z3 by 90 deg");

                Z3.Rotate(1.57);
                Console.WriteLine($"Vector 3: angle = {Z3.PolarAngle}, radius = {Z3.PolarRadius}");
                
                
                Console.WriteLine("\n____Task 4, Z1 = Z2 + Z3");

                Z1 = Z2 + Z3;
                
                Console.WriteLine($"Vector 1: angle = {Z1.PolarAngle}, radius = {Z1.PolarRadius}");




        }
    }
}