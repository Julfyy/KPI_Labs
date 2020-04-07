//
// Created by bohdan on 07.04.20.
//

#include "Rhombus.h"
#include "math.h"

Rhombus::Rhombus(float nodeCoordinates[4][2]) : Figure()
{
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 2; j++)
        {
            _nodeCoordinates[i][j] = nodeCoordinates[i][j];
        }
    }

    CalculateSides();
    CalculateDiagonals();
}


void Rhombus::CalculateSides()
{
    _sideLength = sqrt(pow(_nodeCoordinates[1][0] - _nodeCoordinates[0][0], 2) +
                            pow(_nodeCoordinates[1][1] - _nodeCoordinates[0][1], 2));
}
void Rhombus::CalculateDiagonals()
{
    _firstDiagonalLength = sqrt(pow(_nodeCoordinates[2][0] - _nodeCoordinates[0][0], 2) +
                                     pow(_nodeCoordinates[2][1] - _nodeCoordinates[0][1], 2));
    _secondDiagonalLength = sqrt(pow(_nodeCoordinates[3][0] - _nodeCoordinates[1][0], 2) +
                                      pow(_nodeCoordinates[3][1] - _nodeCoordinates[1][1], 2));
}

double Rhombus::GetArea()
{
    return _firstDiagonalLength * _secondDiagonalLength / 2;
}

double Rhombus::GetPerimeter()
{
    return _sideLength * 4;
}
