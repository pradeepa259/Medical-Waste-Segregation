import RPi.GPIO as GPIO

import time

# setting mode for GPIO
GPIO.setmode(GPIO.BCM)

# setting up motor driver pins
ENA_pin = 24
IN1_pin = 27
IN2_pin = 18

ENB_pin = 25
IN3_pin = 22
IN4_pin = 23

# setting up GPIO pins
GPIO.setup(ENA_pin, GPIO.OUT)
GPIO.setup(IN1_pin, GPIO.OUT)
GPIO.setup(IN2_pin, GPIO.OUT)
GPIO.setup(ENB_pin, GPIO.OUT)
GPIO.setup(IN3_pin, GPIO.OUT)
GPIO.setup(IN4_pin, GPIO.OUT)

# setting input pins for GPIO pin
GPIO.output(ENA_pin, GPIO.LOW)
GPIO.output(IN1_pin, GPIO.LOW)
GPIO.output(IN2_pin, GPIO.LOW)
GPIO.output(ENB_pin, GPIO.LOW)
GPIO.output(IN3_pin, GPIO.LOW)
GPIO.output(IN4_pin, GPIO.LOW)

# setting the PWM signals for ENA and ENB pins
pwm_ENA = GPIO.PWM(ENA_pin, 100)
pwm_ENB = GPIO.PWM(ENB_pin, 100)
pwm_ENA.start(0)
pwm_ENB.start(0)

# functions for motor control
def forward(speed):
    GPIO.output(IN1_pin, GPIO.HIGH)
    GPIO.output(IN2_pin, GPIO.LOW)
    GPIO.output(IN3_pin, GPIO.HIGH)
    GPIO.output(IN4_pin, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)
def backward(speed):
    GPIO.output(IN1_pin, GPIO.LOW)
    GPIO.output(IN2_pin, GPIO.HIGH)
    GPIO.output(IN3_pin, GPIO.LOW)
    GPIO.output(IN4_pin, GPIO.HIGH)
    pwm_ENA.ChangeDutyCycle(speed)
    pwm_ENB.ChangeDutyCycle(speed)

def stop():
    GPIO.output(IN1_pin, GPIO.LOW)
    GPIO.output(IN2_pin, GPIO.LOW)
    GPIO.output(IN3_pin, GPIO.LOW)
    GPIO.output(IN4_pin, GPIO.LOW)
    pwm_ENA.ChangeDutyCycle(0)
    pwm_ENB.ChangeDutyCycle(0)

try:
    # Run the motors forward
    forward(50)
    time.sleep(2)

    # Run the motors backward
    backward(50)
    time.sleep(2)

    # Stop the motors
    stop()

except KeyboardInterrupt:
    # Clean up GPIO pins on keyboard interrupt
    GPIO.cleanup()

# Clean up GPIO pins when program is finished
GPIO.cleanup()