#include <Servo.h>
Servo thruster1;
Servo thruster2;
byte t1Pin = 10;
byte t2Pin = 9;

void setup()
{
  Serial.begin(9600);
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

  int commandIndex;
  String command;

  int valueIndex;
  float value;  

  int signalValue;
  
  while (Serial.available())
  {
    if(Serial.available() > 0)
    {
      data = Serial.readStringUntil('\r');

      commandIndex = data.indexOf(',');
      command = data.substring(0, commandIndex);

      valueIndex = data.indexOf(':', commandIndex+1);
      value = (data.substring(commandIndex+1,valueIndex)).toFloat();
      
      
//      Serial.print("Command:");
//      Serial.print(command);
//      
//      Serial.print(" Value:");
//      Serial.println(value);
          
      //1700; // Set signal value, which should be between 1100 and 1900
      signalValue = (((1900-1500)*(value - 0))/(1-0)) + 1500;

      //Serial.print("Signal Value");
      Serial.println(signalValue);
      thruster1.writeMicroseconds(signalValue); // Send signal to ESC.
      thruster2.writeMicroseconds(signalValue);
    }    
  }
}
