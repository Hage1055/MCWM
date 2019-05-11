int motorPin = 3; //Digital pin for the DC motor controlling the grinding wheel
int IRSensorPin = 2; //Analog pin for the IR sensor
unsigned int dist = 0; //Set initial distance to 0

#include <FastLED.h>
#define LEDPin     7 //Digital pin associated with LEDs
#define NumLEDS   34 //Number of LEDs on the strip you are controlling
CRGB leds[NumLEDS];

void setup() 
{
  pinMode(motorPin, OUTPUT); //Set the assigned motor pin to an output
  FastLED.addLeds<WS2812, LEDPin, GRB>(leds, NumLEDS); //Setup LED, shouldnt need to change with variables
  Serial.begin(9600); //Start the serial monitor
}

void loop() 
{
   //int speed = 255; //set speed of motor 0 to 255
   //analogWrite(motorPin, speed); //Give the motor its speed
   
   dist =  (64 * dist - 10 * (dist - analogRead(IRSensorPin) ))/64; //Record the distance from the pin value
   Serial.println(dist); //Display the distance
   delay(400); //delay before printing next value

   if (dist >= 200) //Green section of lighting. Hopper has an acceptable amount of BC
   {
     for (int i = 0; i <= NumLEDS - 1; i++)
    {
      leds[i] = CRGB (0, 255, 0);
      FastLED.show();
    }
   }
   else if (dist < 200 && dist >= 140) //Solid Red section. Hopper should be refilled
   {
     for (int i = 0; i <= NumLEDS - 1; i++)
     {
      leds[i] = CRGB (255, 0, 0);
      FastLED.show();
     }
   }
   else //Blinking red. Something is wrong. Hopper is either empty or lid is off
   {
       for (int i = 0; i <= NumLEDS - 1; i++){
    leds[i] = CRGB (255, 0, 0);
    FastLED.show();
  }

  delay(400);

  for (int i = 0; i <= NumLEDS - 1; i++){
    leds[i] = CRGB (0, 0, 0);
    FastLED.show();
  }

  delay(400);
   }
}
