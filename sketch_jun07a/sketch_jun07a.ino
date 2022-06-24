//
int led1 = 9;
int led2 = 10;
int option;
void setup()
{
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
}

void loop()
{
  if(Serial.available() > 0){
    option = Serial.read();
    if(option == 'F'){
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
    }
    if(option == 'T'){
      digitalWrite(led2, HIGH);
      digitalWrite(led1, LOW);
    }
  }
}
