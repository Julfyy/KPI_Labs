using System;

namespace Lab4
{
    public class Vector
    {
        public double PolarRadius {  get; private set;}
        public double PolarAngle { get; private set; }
        private double pi = Math.PI;
        
        
        //Default constructor
        public Vector()
        {
            PolarRadius = 0.0;
            PolarAngle = 0.0 * pi;
        }
        
        //Constructor with params
        public Vector(double polarRadius, double polarAngle)
        {
            PolarRadius = polarRadius;
            PolarAngle = polarAngle;
        }
        
        //Constructor for copying
        public Vector(Vector vec)
        {
            PolarRadius = vec.PolarRadius;
            PolarAngle = vec.PolarRadius;
        }

        public void Rotate(double angle)
        {
            //Rotating clockwise is adding a positive angle, and counterclockwise is adding a negative one
            PolarAngle += angle;
        }

        public static Vector operator +(Vector v1, Vector v2)
        {
            return new Vector(v1.PolarAngle + v2.PolarAngle, v1.PolarRadius + v2.PolarRadius);
        }

        public static Vector operator *(Vector v1, int scalar)
        {
            return new Vector(v1.PolarRadius * scalar, v1.PolarAngle);
        }

    }
}