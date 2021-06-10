#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

SoftwareSerial mySoftwareSerial(10, 11); // RX, TX
DFRobotDFPlayerMini myDFPlayer;
int button1 = 2;
int button2 = 3;
int button3 = 4;
int button4 = 5;
int button5 = 6;
int button6 = 7;
int battIndicator = A0;


void setup() {
    pinMode(button1, INPUT);
    pinMode(button2, INPUT);
    pinMode(button3, INPUT);
    pinMode(button4, INPUT);
    pinMode(button5, INPUT);
    pinMode(button6, INPUT);
    pinMode(battIndicator, INPUT);
    mySoftwareSerial.begin(9600);
    Serial.begin(115200);
//  
//    Serial.println();
//    Serial.println(F("DFRobot DFPlayer Mini Demo"));
//    Serial.println(F("Initializing DFPlayer ... (May take 3~5 seconds)"));
  
    if (!myDFPlayer.begin(mySoftwareSerial)) {  //Use softwareSerial to communicate with mp3.
//      Serial.println(F("Unable to begin:"));
//      Serial.println(F("1.Please recheck the connection!"));
//      Serial.println(F("2.Please insert the SD card!"));
      while(true);
    }
//    Serial.println(F("DFPlayer Mini online."));   
    myDFPlayer.begin(mySoftwareSerial);
    myDFPlayer.setTimeOut(500); 
    myDFPlayer.volume(30);
    myDFPlayer.EQ(DFPLAYER_EQ_NORMAL);  
    myDFPlayer.outputDevice(DFPLAYER_DEVICE_SD);
}

void loop() {
  if (analogRead(battIndicator)< 760) {
    myDFPlayer.play(7); 
    delay(15000); 
  }
  else{
  if (digitalRead(button1) == HIGH) {
    myDFPlayer.play(1);  
//    Serial.println("Button Clicked(1)");                    
    delay(500);
  }
  if (digitalRead(button2) == HIGH) {
    myDFPlayer.play(2);
//    Serial.println("Button Clicked(2)");                    
    delay(500);
  }
  if (digitalRead(button3) == HIGH) {
    myDFPlayer.play(3);
//    Serial.println("Button Clicked(3)");                    
    delay(500);
  }
  if (digitalRead(button4) == HIGH) {
    myDFPlayer.play(4);
//    Serial.println("Button Clicked(4)");                        
    delay(500);
  }
  if (digitalRead(button5) == HIGH) {
    myDFPlayer.play(5);
//    Serial.println("Button Clicked(5)");                     
    delay(500);
  }
  if (digitalRead(button6) == HIGH) {
    myDFPlayer.play(6);
//    Serial.println("Button Clicked(6)");                     
    delay(500);
  }
}
}
