
int LEDr = 6; 

void setup()
{

pinMode(LEDr, OUTPUT); 
} 

void loop() 
  
     analogWrite(LEDr, (25));

    delay(1000);

    analogWrite(LEDr, (0));
    
    delay(1000);

}  
