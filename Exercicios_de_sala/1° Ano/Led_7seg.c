// Programa um display led de 7 segmentos (em arduino) a exibir um valor de 1 a 6 gerado por um botão


#define SEG_A 2
#define SEG_B 3
#define SEG_C 4
#define SEG_D 5
#define SEG_E 6
#define SEG_F 7
#define SEG_G 8
#define PONTO 9
#define BOTAO 13

void limpar(){
  for (int pino= SEG_A; pino <= PONTO; pino ++){
   digitalWrite(pino,HIGH);
    }
  }
  
void setup() {
  for (int pino= SEG_A; pino <= PONTO; pino ++){
  pinMode(pino, OUTPUT);
  }
  limpar();
  pinMode(BOTAO, INPUT);
  Serial.begin(9600);
}

void loop() {
  if (digitalRead(BOTAO) == 1){
    int botao = random(1,7);
  if (botao == 1){
    limpar(); 
  digitalWrite(SEG_B, LOW); 
  digitalWrite(SEG_C, LOW);
  }
  else {
      if (botao == 2){
    limpar();
    digitalWrite(SEG_A, LOW); 
    digitalWrite(SEG_B, LOW); 
    digitalWrite(SEG_D, LOW);  
    digitalWrite(SEG_E, LOW); 
    digitalWrite(SEG_G, LOW);
      }
      else {
       if (botao == 3){
        limpar();
        digitalWrite(SEG_A, LOW); 
        digitalWrite(SEG_B, LOW); 
        digitalWrite(SEG_C, LOW);
        digitalWrite(SEG_D, LOW);  
        digitalWrite(SEG_G, LOW); }
        else {
            if (botao == 4){
        limpar();
        digitalWrite(SEG_B, LOW); 
        digitalWrite(SEG_C, LOW);
        digitalWrite(SEG_F, LOW); 
        digitalWrite(SEG_G, LOW); 
          }
          else {
              if (botao == 5){
          limpar();
        digitalWrite(SEG_A, LOW); 
        digitalWrite(SEG_C, LOW);
        digitalWrite(SEG_D, LOW);  
        digitalWrite(SEG_F, LOW); 
        digitalWrite(SEG_G, LOW); 
            }
          else{
          limpar();
        digitalWrite(SEG_A, LOW); 
        digitalWrite(SEG_C, LOW);
        digitalWrite(SEG_D, LOW);
        digitalWrite(SEG_E, LOW);   
        digitalWrite(SEG_F, LOW); 
        digitalWrite(SEG_G, LOW); 
        }
          }
          }
        }
    }
  delay (1000);
  }
}