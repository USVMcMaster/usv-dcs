#include <Servo.h>
Servo thruster1;
Servo thruster2;
byte t1Pin = 10;
byte t2Pin = 9;

void setup()
{
  Serial.begin(9600);

//  Temporarily disabled since motors are not connected
  thruster1.attach(t1Pin);
  thruster2.attach(t2Pin);

  thruster1.writeMicroseconds(1500); //1500 is the stop signal for the ESC
  thruster2.writeMicroseconds(1500);
  delay(2500); //Wait for ESC to recognize signal

  Serial.println("Ready");
}

void loop()
{
  String data;

  int eventIndex;
  String event;                                                       

  float state;
  int signalValue;

  String t1_code = String("ABS_Y");
  String t2_code = String("ABS_RY");

//  t1 and t2 output values used only for serial monitor
  int t1_output;
  int t2_output;

  while (Serial.available())
  {
    if(Serial.available() > 0)
    {
      data = Serial.readStringUntil('\r');

      eventIndex = data.indexOf(',');
      event = data.substring(0, eventIndex);

      state = (data.substring(eventIndex+1)).toFloat();

//      (new_sig_max-new_sig_min)*(input - min)/(max-min) + offset
      signalValue = ((1900-1500)*state) + 1500;

//      The following if statements are an abomination.
//      Please forgive me.
      if (event == t1_code)
      {
        thruster1.writeMicroseconds(signalValue);
        t1_output = signalValue;
      }

      else if (event == t2_code)
      {
        thruster2.writeMicroseconds(signalValue);
        t2_output = signalValue;
      }

      if ((event == t1_code) || (event == t2_code))
      {
        Serial.print("T1 Output:");
        Serial.print(" ");
        Serial.print(t1_output);

        Serial.print(" | T2 Output:");
        Serial.print(" ");
        Serial.println(t2_output);
      }
    }
  }
}
