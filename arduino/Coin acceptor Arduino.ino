//Pin In
int OpticalCountPin = 3;
volatile byte CoinPulseCount = 0;
byte NewCoinInserted;
volatile unsigned long PulseTime;

//Pin Out
const int LED1BATH = 4;
const int LED2BATH = 5;
const int LED3BATH = 6;
const int LED4BATH = 7;
 
String OnePulse = "10 Bath";
String TwoPulses = "5 Bath";
String ThreePulses = "new 1 Bath";
String FourPulses = "old 1 Bath";

void setup(){
 
  Serial.begin(9600);
  Serial.println("Waiting...");
  Serial.println();
  
  pinMode(OpticalCountPin, INPUT);
   pinMode(LED1BATH, OUTPUT);
    pinMode(LED2BATH, OUTPUT);
     pinMode(LED3BATH, OUTPUT);
      pinMode(LED4BATH, OUTPUT);
      
attachInterrupt(1, CoinPulse, RISING);
}
 
void loop(){
  digitalWrite (LED1BATH, LOW);
  digitalWrite (LED2BATH, LOW);
  digitalWrite (LED3BATH, LOW);
  digitalWrite (LED4BATH, LOW);
  
  if(CoinPulseCount > 0 && millis() - PulseTime > 200){
    NewCoinInserted = CoinPulseCount;
    CoinPulseCount = 0;
  }
        switch(NewCoinInserted){
          case 1:
            Serial.println(OnePulse + " inserted");
            digitalWrite (LED1BATH, HIGH);
            delay (500);
            
            NewCoinInserted = 0;
            break;
          case 2:
            Serial.println(TwoPulses + " inserted");
            digitalWrite (LED2BATH, HIGH);
            delay (500);
        
            NewCoinInserted = 0;
            break;
          case 3:
            Serial.println(ThreePulses + " inserted");
              digitalWrite (LED3BATH, HIGH);
              delay (500);
            NewCoinInserted = 0;
            break;
          case 4:
            Serial.println(FourPulses + " inserted");
              digitalWrite (LED4BATH, HIGH);
              delay (500);
              
            NewCoinInserted = 0;
            break;
     
        }
}
 
void CoinPulse(){
  CoinPulseCount ++;
  PulseTime = millis();
}
