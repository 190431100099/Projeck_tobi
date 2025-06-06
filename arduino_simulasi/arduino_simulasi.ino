#include <SoftwareSerial.h>
#include <PZEM004Tv30.h>

// Inisialisasi SoftwareSerial untuk masing-masing PZEM
SoftwareSerial softSerial1(2, 3);  // RX, TX untuk PZEM R
SoftwareSerial softSerial2(4, 5);  // RX, TX untuk PZEM S
SoftwareSerial softSerial3(6, 7);  // RX, TX untuk PZEM T

PZEM004Tv30 pzemR(softSerial1);
PZEM004Tv30 pzemS(softSerial2);
PZEM004Tv30 pzemT(softSerial3);

void setup() {
  Serial.begin(9600); // Serial utama untuk komunikasi dengan PC
  softSerial1.begin(9600);
  softSerial2.begin(9600);
  softSerial3.begin(9600);

  delay(1000); // Waktu inisialisasi
}

void loop() {
  float teganganR = pzemR.voltage();
  float teganganS = pzemS.voltage();
  float teganganT = pzemT.voltage();
  float arusR = pzemR.current();
  float arusS = pzemS.current();
  float arusT = pzemT.current();

  Serial.print(teganganR); Serial.print(",");
  Serial.print(teganganS); Serial.print(",");
  Serial.print(teganganT); Serial.print(",");
  Serial.print(arusR); Serial.print(",");
  Serial.print(arusS); Serial.print(",");
  Serial.println(arusT);

  delay(1000);
}
