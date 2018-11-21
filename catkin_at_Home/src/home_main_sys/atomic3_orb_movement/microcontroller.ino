// RoBorregos 2018
//
// Arduino Uno
//
// I2C addresses
// IMU: 0x28
//
// Motor definitions
// MLF: Left Front
// MRF: Right Front
// MRB: Right Back
// MLB: Left Back

//--------------------- Libraries --------------------------//
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

//--------------------- Pins -------------------------------//
const uint8_t MLFE = 9;  // Enable
const uint8_t MLFF = 7;  // Forward
const uint8_t MLFB = 8;  // Backward

const uint8_t MRFE = 3;  // Enable
const uint8_t MRFF = 2;  // Forward
const uint8_t MRFB = 13;  // Backward

const uint8_t MRBE = 6;  // Enable
const uint8_t MRBF = 4;  // Forward
const uint8_t MRBB = 5;  // Backward

const uint8_t MLBE = 10;  // Enable
const uint8_t MLBF = 11;  // Forward
const uint8_t MLBB = 12;  // Backward

//--------------------- IMU --------------------------------//
Adafruit_BNO055 bno = Adafruit_BNO055(55);

//--------------------- Constants -------------------------//
const float PRECISION_IMU = 2.0;
const byte LEFT_FRONT_SPEED = 155;
const byte RIGHT_FRONT_SPEED = 155;
const byte RIGHT_BACK_SPEED = 155;
const byte LEFT_BACK_SPEED = 155;

//--------------------- Global variables ------------------//
unsigned long clk;  //used to measure time

//--------------------- Control movements -----------------//
void moveForward(unsigned int distance)
{
  clk = millis();

  digitalWrite(MLFF, HIGH);
  digitalWrite(MLFB, LOW);
  
  digitalWrite(MRFF, HIGH);
  digitalWrite(MRFB, LOW);

  digitalWrite(MRBF, HIGH);
  digitalWrite(MRBB, LOW);

  digitalWrite(MLBF, HIGH);
  digitalWrite(MLBB, LOW);

  analogWrite(MLFE, LEFT_FRONT_SPEED);
  analogWrite(MRFE, RIGHT_FRONT_SPEED);
  analogWrite(MRBE, RIGHT_BACK_SPEED);
  analogWrite(MLBE, LEFT_BACK_SPEED);

  while(millis() - clk <= distance);

  stopMotors();
}

void moveBackward(unsigned int distance)
{
  clk = millis();

  digitalWrite(MLFF, LOW);
  digitalWrite(MLFB, HIGH);

  digitalWrite(MRFF, LOW);
  digitalWrite(MRFB, HIGH);
  
  digitalWrite(MRBF, LOW);
  digitalWrite(MRBB, HIGH);
  
  digitalWrite(MLBF, LOW);
  digitalWrite(MLBB, HIGH);
  
  analogWrite(MLFE, LEFT_FRONT_SPEED);
  analogWrite(MRFE, RIGHT_FRONT_SPEED);
  analogWrite(MRBE, RIGHT_BACK_SPEED);
  analogWrite(MLBE, LEFT_BACK_SPEED);

  while(millis() - clk <= distance);

  stopMotors();
}

void stopMotors()
{
  analogWrite(MLFE, 0);
  analogWrite(MRFE, 0);
  analogWrite(MRBE, 0);
  analogWrite(MLBE, 0);

  delay(20);
}

void turnRight(int angle)
{
  float oPos = getOrientation();
  float ePos = oPos + angle > 360 ? oPos - 360 + angle : oPos + angle;
  float iLim = ePos - PRECISION_IMU <= 0 ? ePos + 360 - PRECISION_IMU : ePos - PRECISION_IMU;
  float oLim = ePos + PRECISION_IMU > 360 ? ePos - 360 + PRECISION_IMU : ePos + PRECISION_IMU;

  digitalWrite(MLFF, HIGH);
  digitalWrite(MLFB, LOW);

  digitalWrite(MRFF, LOW);
  digitalWrite(MRFB, HIGH);
  
  digitalWrite(MRBF, LOW);
  digitalWrite(MRBB, HIGH);
  
  digitalWrite(MLBF, HIGH);
  digitalWrite(MLBB, LOW);
  
  analogWrite(MLFE, LEFT_FRONT_SPEED);
  analogWrite(MRFE, RIGHT_FRONT_SPEED);
  analogWrite(MRBE, RIGHT_BACK_SPEED);
  analogWrite(MLBE, LEFT_BACK_SPEED);

  if(oLim > iLim)
    while(!(oPos >= iLim && oPos <= oLim))
      oPos = getOrientation();
  else
    while(!(oPos >= iLim || oPos <= oLim))
      oPos = getOrientation();

  stopMotors();
}

void turnLeft(int angle)
{
  float oPos = getOrientation();
  float ePos = oPos - angle < 0 ? oPos + 360 - angle : oPos - angle;
  float iLim = ePos - PRECISION_IMU <= 0 ? ePos + 360 - PRECISION_IMU : ePos - PRECISION_IMU;
  float oLim = ePos + PRECISION_IMU > 360 ? ePos - 360 + PRECISION_IMU : ePos + PRECISION_IMU;

  digitalWrite(MLFF, LOW);
  digitalWrite(MLFB, HIGH);

  digitalWrite(MRFF, HIGH);
  digitalWrite(MRFB, LOW);
  
  digitalWrite(MRBF, HIGH);
  digitalWrite(MRBB, LOW);
  
  digitalWrite(MLBF, LOW);
  digitalWrite(MLBB, HIGH);
  
  analogWrite(MLFE, LEFT_FRONT_SPEED);
  analogWrite(MRFE, RIGHT_FRONT_SPEED);
  analogWrite(MRBE, RIGHT_BACK_SPEED);
  analogWrite(MLBE, LEFT_BACK_SPEED);

  if(oLim > iLim)
    while(!(oPos >= iLim && oPos <= oLim))
      oPos = getOrientation();
  else
    while(!(oPos >= iLim || oPos <= oLim))
      oPos = getOrientation();

  stopMotors();
}

void turnTo(int angle)
{
    int angleNeeded = angle - getOrientation();
    if(angleNeeded > 180)
      turnLeft(360-angle+getOrientation());
    else if(angleNeeded > 0)
      turnRight(angleNeeded);
    else if(angleNeeded > -180)
      turnLeft(-angleNeeded);
    else
      turnRight(360-getOrientation()+angle);
}

//--------------------- IMU utilities ---------------------//
byte getIMUCalStatus()
{
  uint8_t system, gyro, accel, mag;
  system = gyro = accel = mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  return gyro;
}

float getOrientation()
{
  sensors_event_t event;
  bno.getEvent(&event);
  return event.orientation.x;
}

//--------------------- Initial Setup ---------------------//
void setup() {
  // init serial
  Serial.begin(9600);

  // init motors
  pinMode(MLFE, OUTPUT);
  pinMode(MLFF, OUTPUT);
  pinMode(MLFB, OUTPUT);

  pinMode(MRFE, OUTPUT);
  pinMode(MRFF, OUTPUT);
  pinMode(MRFB, OUTPUT);

  pinMode(MRBE, OUTPUT);
  pinMode(MRBF, OUTPUT);
  pinMode(MRBB, OUTPUT);

  pinMode(MLBE, OUTPUT);
  pinMode(MLBF, OUTPUT);
  pinMode(MLBB, OUTPUT);

  stopMotors();

  // init IMU
  if(!bno.begin())
  {
    delay(1000);
  }

  bno.setExtCrystalUse(true);
  while(getIMUCalStatus() <= 0);
  
  // waiting for computer connection
  while(Serial.available() <= 0);

  Serial.print(Serial.readString());
}

//--------------------- Main program ----------------------//
void loop() {
  if(Serial.available() > 0)
  {
    switch(Serial.read() - 48)
    {
      // 1.- Movement rutine
      case 1:
      {
        delay(3000);
        moveForward(2000);
        delay(1000);
        turnTo(315);
        delay(1000);
        turnTo(45);
        delay(1000);
        turnTo(0);
        delay(1000);
        moveBackward(2000);
        
        Serial.print("0");
      }
      break;
      default:
        // return 't' meaning no correct value received, resend.
        Serial.print('t');
    }
  }
}
