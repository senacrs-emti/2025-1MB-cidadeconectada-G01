const int LED_A_VERMELHO = 2;
const int LED_A_AMARELO = 3;
const int LED_A_VERDE = 4;
const int LED_B_VERMELHO = 5;
const int LED_B_AMARELO = 6;
const int LED_B_VERDE = 7;
const int TRIGGER_A = 8;
const int ECHO_A = 9;
const int TRIGGER_B = 10;
const int ECHO_B = 11;

void setup() {
  Serial.begin(9600);
  pinMode(LED_A_VERMELHO, OUTPUT);
  pinMode(LED_A_AMARELO, OUTPUT);
  pinMode(LED_A_VERDE, OUTPUT);
  pinMode(LED_B_VERMELHO, OUTPUT);
  pinMode(LED_B_AMARELO, OUTPUT);
  pinMode(LED_B_VERDE, OUTPUT);
  pinMode(TRIGGER_A, OUTPUT);
  pinMode(ECHO_A, INPUT);
  pinMode(TRIGGER_B, OUTPUT);
  pinMode(ECHO_B, INPUT);
  digitalWrite(LED_A_VERMELHO, LOW);
  digitalWrite(LED_A_AMARELO, LOW);
  digitalWrite(LED_A_VERDE, LOW);
  digitalWrite(LED_B_VERMELHO, LOW);
  digitalWrite(LED_B_AMARELO, LOW);
  digitalWrite(LED_B_VERDE, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    
    if (cmd == 'S') {
      long distA = lerDistancia(TRIGGER_A, ECHO_A);
      long distB = lerDistancia(TRIGGER_B, ECHO_B);
      Serial.print(distA);
      Serial.print(",");
      Serial.println(distB);
    }
    else if (cmd == '1') digitalWrite(LED_A_VERMELHO, HIGH);
    else if (cmd == '2') digitalWrite(LED_A_AMARELO, HIGH);
    else if (cmd == '3') digitalWrite(LED_A_VERDE, HIGH);
    else if (cmd == '4') digitalWrite(LED_B_VERMELHO, HIGH);
    else if (cmd == '5') digitalWrite(LED_B_AMARELO, HIGH);
    else if (cmd == '6') digitalWrite(LED_B_VERDE, HIGH);
    else if (cmd == 'L') {
      digitalWrite(LED_A_VERMELHO, LOW);
      digitalWrite(LED_A_AMARELO, LOW);
      digitalWrite(LED_A_VERDE, LOW);
    }
    else if (cmd == 'M') {
      digitalWrite(LED_B_VERMELHO, LOW);
      digitalWrite(LED_B_AMARELO, LOW);
      digitalWrite(LED_B_VERDE, LOW);
    }
    else if (cmd == 'X') {
      digitalWrite(LED_A_VERMELHO, LOW);
      digitalWrite(LED_A_AMARELO, LOW);
      digitalWrite(LED_A_VERDE, LOW);
      digitalWrite(LED_B_VERMELHO, LOW);
      digitalWrite(LED_B_AMARELO, LOW);
      digitalWrite(LED_B_VERDE, LOW);
    }
  }
}

long lerDistancia(int trig, int echo) {
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);
  long dur = pulseIn(echo, HIGH, 30000);
  long dist = dur * 0.034 / 2;
  if (dist == 0 || dist > 400) return 999;
  return dist;
}