//Example Sketch using multiple analog sensors into one analog input pin
//Tutorials and more at http://www.cabuu.com

#include <ESP8266WiFi.h>

int Value1;
int Value2;
int Pot1 = D7;
int Pot2 = D8;

String apiKey = "Y9JJDC82CRWPT9HT";     //  Enter your Write API key from ThingSpeak

const char *ssid =  "HUAWEI_E5577_6216";     // replace with your wifi ssid and wpa2 key
const char *pass =  "6Y0D6JALDB1";
const char* server = "api.thingspeak.com";

WiFiClient client;

void setup() {

  Serial.begin(9600);   //Start serial monitor
  pinMode(Pot1,OUTPUT);
  pinMode(Pot2,OUTPUT);
  pinMode(A0,INPUT);

  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, pass);
 
  while (WiFi.status() != WL_CONNECTED) {
     delay(500);
     Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  
}

void loop() {
  
  digitalWrite(Pot1, HIGH);     //Turn D7 On
  delay(100);                     //Wait for sensor
  Value1 = analogRead(0);       //Read Analog pin as D7
  digitalWrite(Pot1, LOW);      //Turn D7 Off

  //Repeat for D8
  digitalWrite(Pot2, HIGH);     //Turn D8 On
  delay(100);                     //Wait for sensor
  Value2 = analogRead(0);       //Read Analog pin as D8
  digitalWrite(Pot2, LOW);      //Turn D8 Off
  delay(100);                     //Wait for sensor
  
  //Print the results to the serial monitor
  Serial.print("Sensor1 = ");   
  Serial.print(Value1);
  Serial.print(" / Sensor2 = ");   
  Serial.println(Value2);

  if (client.connect(server,80)){   //   "184.106.153.149" or api.thingspeak.com         
     String postStr = apiKey;              
     postStr +="&field1=";
     postStr += String(Value1);
     postStr +="&field2=";
     postStr += String(Value2);

     client.print("POST /update HTTP/1.1\n");
     client.print("Host: api.thingspeak.com\n");
     client.print("Connection: close\n");
     client.print("X-THINGSPEAKAPIKEY: "+apiKey+"\n");
     client.print("Content-Type: application/x-www-form-urlencoded\n");
     client.print("Content-Length: ");
     client.print(postStr.length());
     client.print("\n\n");
     client.print(postStr);
     Serial.println("Send to Thingspeak.");
  }
  //client.stop();
 
  Serial.println("Waiting...");
  delay(10000);
}
