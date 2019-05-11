int motorPin = 3; //Digital pin for the DC motor controlling the grinding wheel

void setup()
{
  pinMode(motorPin, OUTPUT); //Set the assigned motor pin to an output
}

void loop() 
{
    int speed = 255; //set speed of motor 0 to 255
    analogWrite(motorPin, speed);
}
