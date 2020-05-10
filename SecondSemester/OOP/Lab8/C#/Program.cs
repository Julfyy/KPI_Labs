using System;
using LibLab8;

namespace Lab8
{
    class Program
    {
        
        static void Main(string[] args)
        {
            //      Task 1
            Task2.LineOperation del = Task2.GetCharIndex;
            Console.WriteLine(del('l', "hello"));
            
            
            
            //Task2
            /*
            Car car1 = new Car(100, 60);
            car1.Notify += ActionHandler;
            car1.KilometersLimit = 20;
            car1.StartMoving();
            car1.Move(10);
            car1.StopMoving();
            
            */
            Car car2 = new Car(100, 10);
            car2.Notify += ActionHandler;
            car2.KilometersLimit = 20;
            car2.StartMoving();
            car2.Move(15);
            car2.StopMoving();
            Console.WriteLine("You've passed " + car2.KilometresPassed + " kilometres");
            Console.WriteLine("Consumed " + car2.GetFuelConsumed() + " l of fuel");


        }

        private static void ActionHandler(string message)
        {
            Console.WriteLine(message);
        }
    }
}