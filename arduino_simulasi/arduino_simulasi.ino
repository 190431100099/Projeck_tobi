void setup() {
  Serial.begin(9600);
  // Mulai komunikasi serial dengan baudrate 9600
  randomSeed(analogRead(0)); // Inisialisasi random berdasarkan noise analog
}

void loop() {
  // Buat nilai tegangan random antara 210.0 - 230.0
  float teganganR = random(2100, 2301) / 10.0;
  float teganganS = random(2100, 2301) / 10.0;
  float teganganT = random(2100, 2301) / 10.0;
  String V_R, V_S, V_T;

  V_R = teganganR;
  V_S = teganganS;
  V_T = teganganT;
  // Kirim data ke serial dalam format: R,S,T
  Serial.print(V_R);
  Serial.print(",");
  Serial.print(V_S);
  Serial.print(",");
  Serial.println(V_T);

  delay(1000); // kirim setiap 1 detik
}
