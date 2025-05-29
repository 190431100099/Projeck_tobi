import random
import pandas as pd

def generate_voltage(phasa='R', balanced=True, nominal=220, tolerance=0.05):
    if balanced:
        return round(random.uniform(nominal * (1 - tolerance), nominal * (1 + tolerance)), 2)
    else:
        # menghasilkan tegangan di luar batas toleransi
        if random.random() < 0.5:
            return round(random.uniform(0, nominal * (1 - tolerance - 0.01)), 2)
        else:
            return round(random.uniform(nominal * (1 + tolerance + 0.01), 300), 2)

def generate_dataset(jumlah_data=5000, persen_balance=0.5):
    data = []
    for _ in range(jumlah_data):
        is_balanced = random.random() < persen_balance
        if is_balanced:
            v_r = generate_voltage('R', balanced=True)
            v_s = generate_voltage('S', balanced=True)
            v_t = generate_voltage('T', balanced=True)
            label = '0' #Balance
        else:
            # Setidaknya satu phasa tidak balanced
            status = [True, True, True]
            idx_unbalance = random.randint(0, 2)
            status[idx_unbalance] = False
            v_r = generate_voltage('R', balanced=status[0])
            v_s = generate_voltage('S', balanced=status[1])
            v_t = generate_voltage('T', balanced=status[2])
            label = '1' # Unbalance
        
        data.append([v_r, v_s, v_t, label])
    
    df = pd.DataFrame(data, columns=['V_R', 'V_S', 'V_T', 'Kondisi'])
    return df

# Contoh penggunaan
df_dataset = generate_dataset(jumlah_data=5000, persen_balance=0.5)
print(df_dataset.head())

# Simpan ke file CSV
df_dataset.to_csv('dataset_tegangaan_RST.csv', index=False)
