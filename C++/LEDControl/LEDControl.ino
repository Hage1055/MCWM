#include <FastLED.h>
#define LEDPin     7 //Digital pin associated with LEDs
#define NumLEDS   17 //Number of LEDs on the strip you are controlling
CRGB leds[NumLEDS];

void setup() {
  FastLED.addLeds<WS2812, LEDPin, GRB>(leds, NumLEDS); //Setup LED, shouldnt need to change with variables
  
}
void loop() {
  
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
