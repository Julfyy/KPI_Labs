using System;

namespace Lab5
{
    public class Circle : Figure
    {
        private float Radius { get; set; }

        public Circle(float radius)
        {
            Radius = radius;
        }

        public override double GetArea()
        {
            return Math.PI * Math.Pow(Radius, 2);
        }

        public override double GetPerimeter()
        {
            return 2 * Math.PI * Radius;
        }
    }
}