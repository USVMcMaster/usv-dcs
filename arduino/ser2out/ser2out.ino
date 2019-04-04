//#include <Servo.h>
//Servo myservo;
//byte servoPin = 9;

void setup()
{
  Serial.begin(9600);
  //servo.attach(servoPin);

  //servo.writeMicroseconds(1500); //1500 is the stop signal for the ESC
  //delay(2500) //Wait for ESC to recognize signal
}

void loop()
{
  String data="";
  while (Serial.available())
  {
    if(Serial.available() > 0)
    {
      data = Serial.readStringUntil('\r');
      Serial.println(data);

      //TODO:
      //Parse signal from serial and write to int variable (call it signal)
      //Then do: servo.writeMicroseconds(signal)
    }    
  }
}
