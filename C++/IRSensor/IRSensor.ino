int IRSensorPin = 2; //Analog pin for the IR sensor
unsigned int dist = 0; //Set initial distance to 0


void setup() 
{
   Serial.begin(9600); //Start the serial monitor
}

void loop() 
{
   dist =  (64 * dist - 10 * (dist - analogRead(IRSensorPin) ))/64; //Record the distance from the pin value
   Serial.println(dist); //Display the distance
   delay(400); //delay before printing next value
}
