//Libraries
#include <SoftwareSerial.h>
#include <Servo.h>
#include "I2Cdev.h"
#include "MPU6050_6Axis_MotionApps20.h"
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

//Variable declaration
//Multi-tasking
unsigned long previousSensorMillis = 0;
unsigned long previousServoMillis = 0;
const unsigned long intervalSensor = 100; // Read data every 100 miliseconds
//const unsigned long intervalServo = 2000; // Print message every 2 seconds

//For MPU-6050 Sensor
MPU6050 mpu;

#define OUTPUT_READABLE_YAWPITCHROLL

#define INTERRUPT_PIN 2  // use pin 2 on Arduino Uno & most boards
#define LED_PIN 13 // (Arduino is 13, Teensy is 11, Teensy++ is 6)
bool blinkState = false;

// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer

// Orientation/motion vars
Quaternion q;           // [w, x, y, z]         quaternion container
VectorInt16 aa;         // [x, y, z]            accel sensor measurements
VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
VectorFloat gravity;    // [x, y, z]            gravity vector
float euler[3];         // [psi, theta, phi]    Euler angle container
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector

// Packet structure for InvenSense teapot demo
uint8_t teapotPacket[14] = { '$', 0x02, 0,0, 0,0, 0,0, 0,0, 0x00, 0x00, '\r', '\n' };

//For servo motors
#define RX_PIN 0 // Connect the TXD cable from the USB TTL UART adapter to this pin
#define TX_PIN 1 // Connect the RXD cable from the USB TTL UART adapter to this pin

Servo servo1;  // Create a servo object for servo motor 1
Servo servo2;  // Create a servo object for servo motor 2

SoftwareSerial mySerial(RX_PIN, TX_PIN);


//INTERRUPT DETECTION ROUTINE (MPU-6050)
volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
    mpuInterrupt = true;
}

//Initial setup
void setup() {
    
    Serial.begin(115200);
    while (!Serial); // wait for Leonardo enumeration, others continue immediately
    //MPU-6050 setup

    // join I2C bus (I2Cdev library doesn't do this automatically)
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
        Wire.setClock(400000); // 400kHz I2C clock. Comment this line if having compilation difficulties
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

    // initialize device
    mpu.initialize();
    pinMode(INTERRUPT_PIN, INPUT);

    // wait for ready
    //Serial.println(F("\nSend any character to begin DMP programming and demo: "));
    while (Serial.available() && Serial.read()); // empty buffer
    //while (!Serial.available());                 // wait for data
    while (Serial.available() && Serial.read()); // empty buffer again

    // load and configure the DMP
    devStatus = mpu.dmpInitialize();

    // supply your own gyro offsets here, scaled for min sensitivity
      //Sensor (4 pins down)
      mpu.setXAccelOffset(-996);
      mpu.setYAccelOffset(-1948);
      mpu.setZAccelOffset(980);
      mpu.setXGyroOffset(88);
      mpu.setYGyroOffset(-66);
      mpu.setZGyroOffset(-51);

    // make sure it worked (returns 0 if so)
    if (devStatus == 0) {
        // Calibration Time: generate offsets and calibrate our MPU6050
        mpu.CalibrateAccel(6);
        mpu.CalibrateGyro(6);
        mpu.PrintActiveOffsets();
        // turn on the DMP, now that it's ready
        mpu.setDMPEnabled(true);

        // enable Arduino interrupt detection
        attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), dmpDataReady, RISING);
        mpuIntStatus = mpu.getIntStatus();

        // set our DMP Ready flag so the main loop() function knows it's okay to use it
        dmpReady = true;

        // get expected DMP packet size for later comparison
        packetSize = mpu.dmpGetFIFOPacketSize();
    }
    // configure LED for output
    pinMode(LED_PIN, OUTPUT);

    //Servo motors setup
    pinMode(RX_PIN, INPUT);
    pinMode(TX_PIN, OUTPUT);
    mySerial.begin(115200); // Start the SoftwareSerial communication
    servo1.attach(9);    // Attach servo motor 1 to digital pin 9
    servo2.attach(10);   // Attach servo motor 2 to digital pin 10
}

//Void loop
void loop(){
  //Initialization of counter
  unsigned long currentMillis = millis();

  //Task 1: Sensor
  if (currentMillis - previousSensorMillis >= intervalSensor) {

    if (!dmpReady) return;
    // read a packet from FIFO
    if (mpu.dmpGetCurrentFIFOPacket(fifoBuffer)) { // Get the Latest packet 

        #ifdef OUTPUT_READABLE_YAWPITCHROLL
            // display Euler angles in degrees
            mpu.dmpGetQuaternion(&q, fifoBuffer);
            mpu.dmpGetGravity(&gravity, &q);
            mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
            Serial.print(ypr[0] * 180/M_PI);
            Serial.print(",");
            Serial.print(ypr[1] * 180/M_PI);
            Serial.print(",");
            Serial.println(ypr[2] * 180/M_PI);
        #endif
    }
    previousSensorMillis = currentMillis;
  }

  //Task 2: Move servo motors
  if (mySerial.available()) {
    String command = Serial.readStringUntil('\n');  // Read the string from serial input
    int servoIndex = command.charAt(0) - '0';  // Extract the servo index from the string
    int position = command.substring(2).toInt()+90;  // Extract the position from the string

    // Move the specified servo motor to the specified position
    if (servoIndex == 1 && position >= 0 && position <= 180) {
      servo1.write(position);
    }
    else if (servoIndex == 2 && position >= 30 && position <= 150) {
      servo2.write(position);
    }
  }
}
