#include <Servo.h>
Servo servo;
byte servoPin = 9;

void setup()
{
  Serial.begin(9600);
  servo.attach(servoPin);

  servo.writeMicroseconds(1500); //1500 is the stop signal for the ESC
  delay(5000); //Wait for ESC to recognize signal

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
      servo.writeMicroseconds(signalValue); // Send signal to ESC.
    }    
  }
}
