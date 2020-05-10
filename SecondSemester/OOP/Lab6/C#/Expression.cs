using System;

namespace Lab6
{
    public class Expression
    {
        private double _result;

        private double _c;
        
        public double A { private get; set; }
        public double B { private get; set; }
        public double C {
            private get
            {
                return _c ;
            }
            set
            {
                if (value == 0d)
                {
                    throw new DivideByZeroException("Division by zero exception!");
                }
                _c = value;
            }
        }
        public Expression(double a, double b, double c)
        {
            A = a;
            B = b;
            C = c;
        }

        public void Calculate()
        {
            if ((A * B + 2) <= 0)
            {
                throw new ArgumentOutOfRangeException("A and B", "Log(a * b + 2) has only positive range of argument values");
            } 
            if (Math.Abs((41 - (B / C) + 1)) < Double.Epsilon)
            {
                throw new DivideByZeroException("Division by zero exception!");
            }
            _result = (Math.Log(A * B + 2) * 2) / (41 - (B / C) + 1);
        }

        public double GetResult()
        {
            return _result;

        }
    }
}