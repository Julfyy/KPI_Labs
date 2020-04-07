using System;

namespace Lab5
{
    public class Rhombus : Figure
    {
        private float[,] _nodeCoordinates;
        private double _sideLength;
        private double _firstDiagonalLength;
        private double _secondDiagonalLength;
        public Rhombus(float[,] nodeCoordinates)
        {
            _nodeCoordinates = nodeCoordinates;
            CalculateSides();
            CalculateDiagonals();
        }

        private void CalculateSides()
        {
            _sideLength = Math.Sqrt(Math.Pow(_nodeCoordinates[1, 0] - _nodeCoordinates[0, 0], 2) +
                          Math.Pow(_nodeCoordinates[1, 1] - _nodeCoordinates[0, 1], 2));
        }
        private void CalculateDiagonals()
        {
            _firstDiagonalLength = Math.Sqrt(Math.Pow(_nodeCoordinates[2, 0] - _nodeCoordinates[0, 0], 2) +
                                         Math.Pow(_nodeCoordinates[2, 1] - _nodeCoordinates[0, 1], 2));
            _secondDiagonalLength = Math.Sqrt(Math.Pow(_nodeCoordinates[3, 0] - _nodeCoordinates[1, 0], 2) +
                                         Math.Pow(_nodeCoordinates[3, 1] - _nodeCoordinates[1, 1], 2));
        }

        public override double GetArea()
        {
            return _firstDiagonalLength * _secondDiagonalLength / 2;
        }

        public override double GetPerimeter()
        {
            return _sideLength * 4;
        }
    }
}