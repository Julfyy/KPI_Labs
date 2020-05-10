using System;

namespace LibLab8
{
    public class Car
    {
        private readonly float _fuelTank;
        private readonly float _kiloPerLitreFuelConsumption;
        public float KilometresPassed { get; private set; }
        public float KilometersLimit { private get; set;}
        private bool _isEngineStarted;  
        public delegate void ActionHandler(string message);

        public event ActionHandler Notify;

        public Car(float fuel, float kiloPerLitreFuelConsumption)
        {
            _fuelTank = fuel;
            _kiloPerLitreFuelConsumption = kiloPerLitreFuelConsumption;
        }


        public void StartMoving()
        {
            _isEngineStarted = true;
            Notify?.Invoke("The car has started the engine!");
        }

        public void Move(int kilometers)
        {
            if (_isEngineStarted)
            {
                Notify?.Invoke("The car is now moving some kilometers!");
                for (int i = 0; i < kilometers; i++)
                {
                    if (i >= KilometersLimit)
                    {
                        Notify?.Invoke("The kilometres limit is exceeded!");
                        StopMoving();
                        break;
                    }

                    if (GetFuelConsumed() >= _fuelTank)
                    {
                        Notify?.Invoke("You`re out of fuel!");
                        StopMoving();
                        break;
                    }
                    
                    KilometresPassed++;
                }
            }
            else
            {
                Notify?.Invoke("Start the engine first!");
            }
        }

        public void StopMoving()
        {
            if (_isEngineStarted)
            {
                _isEngineStarted = false;
                Notify?.Invoke("The engine was stopped");                
            }

        }
        public float GetFuelConsumed()
        {
            return KilometresPassed / _kiloPerLitreFuelConsumption;
        }
    }
}