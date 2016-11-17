

/*
*******************************************
This code is in an evolution state, currently using the serial UART but will switch to direct input to trigger python script soon
it will make the arduino code compatible with all OS
*******************************************
*/

//define Arduino pin used, not mandatory but convenient,
int LEDr = 6; //I.E. red Positive is powered by pin 6 of the Arduino pro mini, this is a PWM compatible ( adjustable voltage )  3, 5, 6, 9, 10, and 11 are all PWM
int LEDg = 5;
int LEDb = 3;
int rst = 7;
int pwb = 8;
int pwrctrl = 9; // even if the 9 is pwm, we can still use this at full power using digitalWrite HIGH or 1 instead of analogWrite with a value
int retropie = 10; // use pin 10 to detect if RetroPie is booted
int kodi = 11; // use pin 10 to detect if kodi is booted
int rasbian = 12; // use pin 10 to detect if RetroPie is booted
 
//define logic variable used during setup and loops
int logged;
int off;
int killed;
int rsttime;
int firstboot;
String login;
String password;
String OS;
 
void setup() //This will run only once when powering the Arduino from the wall socket
{
 
Serial.begin(57600); // define serial baudrate, very important, also, raspberry pi /boot/cmdline.txt has to be changed to this same value
 
//define pinmode, mandatory
pinMode(LEDr, OUTPUT); // sends current when used with analogWrite or digitaWrite high or with a value, if value is low or 0, it connects to the ground/common, very important to know!
pinMode(LEDg, OUTPUT);
pinMode(LEDb, OUTPUT);
pinMode(rst, INPUT_PULLUP); // using the internal resistor of the arduino, while the value is higher than 0, it means there is no connection between the ground and the pin so, the button is released, when it hit 0
pinMode(pwb, INPUT_PULLUP);
pinMode(pwrctrl, OUTPUT);
digitalWrite(pwrctrl, LOW);
pinMode(kodi, INPUT_PULLUP); //if the pin get grounded the nes will know it needs to use a different password
 
/**** explanation of pinmode
OUTPUT sends voltage
INPUT received voltage
INPUT_PULLUP uses internal resistor and when connected to the ground, value drops to zero, which make a suitable logic value to use. 0 = ON, >0 = OFF
****/
 
// add a default logic value that will be altered while using the Arduino
logged = 0;
off = 1;
os = " "
rsttime = 0;
killed = 0;
firstboot=1;
 
} // end of setup
 
void loop()  // this loop will run in a loop until Arduino is unplugged
{
 
  if (digitalRead(pwb) > 0 && off == 1)
  {
   
/*************************
while the power button is released and the pi is on a off state it will determine which cartrige is in the slot
*********************** */
 
                if(digitalRead(retropie) == 0)      
                                {
                                                login = "pi\n";
                                                password = "raspberry\n";
                                }
 
                if(digitalRead(kodi) == 0)
                                {
                                                login = "root\n";
                                                password = "openelec\n";
                               
                                }             
                if(digitalRead(rasbian) == 0)        
                                {
                                                login = "pi\n";
                                                password = "raspberry\n";
                                }
 
                   analogWrite(LEDr, (0));
                   analogWrite(LEDg, (0));
                   analogWrite(LEDb, (0));
  }
 
 
  if (digitalRead(pwb) == 0 && off == 1)
  {
                if(retropie > 0 && kodi > 0 && rasbian > 0)
                {
                                analogWrite(LEDr, (25));
 
                                delay(1000);
 
                                analogWrite(LEDr, (0));
                               
                                delay(1000);
                }
 
                else{
               
 
    if (firstboot == 1)
    {
      digitalWrite(pwrctrl, HIGH); // will let the pi run.
      firstboot =0; // first boot only there will be no reset, pi will start even if power button is at off, it is intended as is
    }
    else
    {
    digitalWrite(pwrctrl, LOW); // will ground the "run" SQUARE PIN (on rpi 3 b+) and close the run chip on the pi forcing a reset
    delay(200);
    digitalWrite(pwrctrl, HIGH); // release the ground with a matching 3.3v to the run pin so it run normally
    }
   
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDr, (i));
          analogWrite(LEDb, (i));            
          delay(300);
        }
      analogWrite(LEDr, (0));
      analogWrite(LEDb, (0));     
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDb, (i));          
          analogWrite(LEDg, (i));
          delay(300);
        }
      analogWrite(LEDb, (0));
      analogWrite(LEDg, (0));     
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDr, (i));           
          analogWrite(LEDg, (i));
          delay(300);
        }
      analogWrite(LEDr, (0));
      analogWrite(LEDg, (0)); 
      analogWrite(LEDb, (0));
 
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDr, (i));
          delay(300);
        }
 
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDg, (i));
          delay(300);
        }
 
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDb, (i));
          delay(300);
        }
 
      analogWrite(LEDr, (0));
      analogWrite(LEDg, (0)); 
      analogWrite(LEDb, (0));
 
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDg, (i));
          delay(300);
        }
      analogWrite(LEDg, (0));
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDb, (i));
          delay(300);
        }
      analogWrite(LEDb, (0));
             
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDr, (i));
          delay(300);
        }
      
delay(5000);
 
    Serial.print(login);
    delay(1000);
    Serial.print(password);
    delay(1000);
    logged  = 1;   
    off = 0;
  }}
   
 
  if(logged == 1 && off == 0)
  {
                if(kodi == 1) 
                                {
                                                analogWrite(LEDr, 0);   
                                                analogWrite(LEDg, 0);
                                                analogWrite(LEDb, 25);
                                }
                if(retropie == 1) 
                {
                                analogWrite(LEDr, 25);   
                                analogWrite(LEDg, 0);
                                analogWrite(LEDb, 0);
                }
                if(rasbian == 1) 
                {
                                analogWrite(LEDr, 0);   
                                analogWrite(LEDg, 25);
                                analogWrite(LEDb, 0);
                }
  }
 
  while(digitalRead(rst) == 0 && off == 0) // start a reset sequence, quick press kill the app and return to emulationstation, holding 3 sec will hard reboot
    {
      if(killed == 0)
        {
          analogWrite(LEDr, 0);
          analogWrite(LEDb, (25));
          Serial.print("pkill retroarch\n"); // close any emulator made for Libretro (starts with lr-) default for everyone except N64 need to download one
          delay (500);
          killed = 1;
        }
 
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDb, (25-i));
          delay(10);
        }
 
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDb, (i));
          delay(10);
        }
 
      delay(500); // 500 ms + 2x 25*10ms = 1 sec
      rsttime++;   // add 1 to the counter
 
      if(rsttime >= 3)  // 3 seconds count
        {
          analogWrite(LEDr, 0);
          analogWrite(LEDg, 0);
          analogWrite(LEDb, 0);
          Serial.print("sudo reboot\n");
          delay(7500);
          logged = 0;
          off = 1;
          firstboot = 1;
        }
    }
 
  rsttime = 0;
  killed = 0;
 
  if (digitalRead(pwb) > 0 && off == 0) // start a shutdown if its already started
    {
      delay(200);
      Serial.print("sudo halt\n"); // command to safely shutdown the pi
      //trigger a 15 seconds Led fade in fade out
      for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDr, (25-i));
          delay(50);
        }
      for (int i=0; i <= 25; i++)       
        {
          analogWrite(LEDr, (25-i));
          delay(50);
        }
      for (int i=0; i <= 25; i++)       
        {
          analogWrite(LEDr, (25-i));
          delay(50);
        }
      for (int i=0; i <= 25; i++)       
        {
          analogWrite(LEDr, (25-i));
          delay(50);
        }
       
      analogWrite(LEDr, (0));
            for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDg, (25-i));
          delay(200);
        }
      analogWrite(LEDg, (0));
            for (int i=0; i <= 25; i++)
        {
          analogWrite(LEDb, (25-i));
          delay(200);
        }
      analogWrite(LEDb, (0));
       
      logged = 0;
      off = 1;
 
     
      
 
    }
 
 
}  // end of loop
