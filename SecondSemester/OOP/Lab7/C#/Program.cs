using System;

namespace Lab7
{
    static class Program
    {
        static void Main(string[] args)
        {
            LinkedList linkedList = new LinkedList();

            linkedList.InsertLast(7);
            linkedList.InsertLast(20);
            linkedList.InsertLast(21);
            linkedList.InsertLast(14);
            linkedList.InsertLast(1);
            linkedList.InsertLast(22);

            
            Console.WriteLine(linkedList.ToString());

            int number = 7;
            Console.WriteLine($"Number of multiples of number {number} is " + linkedList.GetNumberOfMultiples(number));


            Console.WriteLine($"Mean value is {linkedList.MeanValue:F2}");

            linkedList.ReplaceWithZeroIfMoreThen(linkedList.MeanValue);
            Console.WriteLine(linkedList.ToString());
        }
    }
}