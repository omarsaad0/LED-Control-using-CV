#define numOfValsRec 5
#define digitsPerValRec 1

int led1 = 9;
int led2 = 10;
int led3 = 11;
int led4 = 12;
int led5 = 13;

int valsRec[numOfValsRec];

int stringLength = numOfValsRec * digitsPerValRec +1;     //$00000
int counter = 0;
bool counterStart = false;
String receivedString;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  
  
}


void receieveData(){
  while (Serial.available())
  {
    char c = Serial.read();

    if (c=='$'){
      counterStart = true;
    }
    if (counterStart){
      if(counter < stringLength){
        receivedString = String(receivedString + c);
        counter++;
      }
      if (counter >=stringLength){
        //$00000
        //valsRec[0] = receivedString.substring(0,1).toInt;    //Hard Coded repeat for num of val rec
        for(int i = 0; i<numOfValsRec; i++){
          int num = (i*digitsPerValRec)+1; 
          valsRec[i] = receivedString.substring(num,num + digitsPerValRec).toInt();
        }
        receivedString = "";
        counter = 0;
        counterStart = false;   //reset
      }
    }
  }

  
}


void loop() {
   receieveData();
   if(valsRec[0] == 1){digitalWrite(led1, HIGH);}
   else if( valsRec[0] == 0){digitalWrite(led1, LOW);}
   
   if(valsRec[1] == 1){digitalWrite(led2, HIGH);}
   else if( valsRec[1] == 0){digitalWrite(led2, LOW);}
   
   if(valsRec[2] == 1){digitalWrite(led3, HIGH);}
   else if( valsRec[2] == 0){digitalWrite(led3, LOW);}
   
   if(valsRec[3] == 1){digitalWrite(led4, HIGH);}
   else if( valsRec[3] == 0){digitalWrite(led4, LOW);}
   
   if(valsRec[4] == 1){digitalWrite(led5, HIGH);}
   else if( valsRec[4] == 0){digitalWrite(led5, LOW);}








  

}
