using System;
using ClassLibrary;

namespace Lab2
{
    static class Program
    {
        static void Main(string[] args)
        {
            TextShape text = new TextShape();

            text.AddLine(Line.InputLine());
            text.AddLine(Line.InputLine());
            text.AddLine(Line.InputLine());
            text.ShowText();
            Console.WriteLine(text.GetLettersNumber());
            Console.WriteLine(text.findLine(Line.InputLine()));

            text.ShowText();
        }
    }
}