const int ledPin = 13;
volatile int rpmcount;
int sensorState = 0;
int rpm;
unsigned long timeold;
float set_speed = 800;
const int Mpwm = 7;
const int Mdir = 8;
float error = 0;


void rpm_fun()
{
  rpmcount++;
}

void pid_control(int feedback_speed) {
  error = set_speed - feedback_speed;
  //Serial.print("Error");
  //Serial.println(error);
  if (error > 0) {
    digitalWrite(Mdir, LOW);
    digitalWrite(Mpwm, 100);
  }
  else if (error < 0) {
    digitalWrite(Mdir, HIGH);
    digitalWrite(Mpwm, 100);
  }
  else {

    digitalWrite(Mdir, LOW);
    digitalWrite(Mpwm, 0);
  }
}

void setup() {
  Serial.begin(9600);
  attachInterrupt(0, rpm_fun, FALLING);

  pinMode(Mpwm, OUTPUT);
  pinMode(Mdir, OUTPUT);

  digitalWrite(Mdir, LOW);
  digitalWrite(Mpwm, 100);
  delay(50);
  digitalWrite(Mpwm, 0);

}

void loop() {

  if (rpmcount >= 2) {
    rpm = (60000 * rpmcount) / ( (millis() - timeold)); 
    pid_control(rpm);
    timeold = millis();
    rpmcount = 0;
    Serial.println(rpm, DEC);
  }
}

