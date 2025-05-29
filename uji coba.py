import numpy as np
import joblib
from tensorflow.keras.models import load_model

# 1. Load model dan scaler
model = load_model ('model_ann.h5')
scaler = joblib.load('scaler.pkl')

# 2. Input manual data tegangan RST
print("Masukkan nilai tegangan R, S, dan T:")
v_r = float(input("V_R: "))
v_s = float(input("V_S: "))
v_t = float(input("V_T: "))

# 3. Susun input dan normalisasi
input_data = np.array([[v_r, v_s, v_t]])
input_scaled = scaler.transform(input_data)

# 4. Lakukan prediksi
prediction = model.predict(input_scaled)[0][0]
predicted_class = int(prediction > 0.5)
confidence = prediction if predicted_class == 1 else 1 - prediction

# 5. Interpretasi hasil
kondisi = "UNBALANCE" if predicted_class == 1 else "BALANCE"
print(f"\nHasil Klasifikasi: {kondisi}")
print(f"Confidence (probabilitas): {confidence:.2f}")
