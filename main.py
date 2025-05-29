import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QTimer
from ui_main import *
import serial
import serial.tools.list_ports

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.serial_port = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.read_serial_data)

        # State koneksi
        self.serial_connected = False

        # Event handler
        self.ui.Button_Start.clicked.connect(self.toggle_connection)
        self.ui.Box_port.showPopup = self.update_port_list_then_show
        
        self.ui.line_R.setReadOnly(True)
        self.ui.line_S.setReadOnly(True)
        self.ui.line_T.setReadOnly(True)
        self.ui.line_Status.setReadOnly(True)

    def update_port_list_then_show(self):
        self.update_port_list()
        QComboBox.showPopup(self.ui.Box_port)

    def update_port_list(self):
        self.ui.Box_port.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.Box_port.addItem(port.device)

    def toggle_connection(self):
        if not self.serial_connected:
            self.start_serial()
        else:
            self.stop_serial()

    def start_serial(self):
        selected_port = self.ui.Box_port.currentText()
        if selected_port == "":
            QMessageBox.warning(self, "Peringatan", "Silakan pilih port terlebih dahulu.")
            return

        try:
            self.serial_port = serial.Serial(port=selected_port, baudrate=9600, timeout=1)
            self.timer.start(1000)  # Baca data setiap 1 detik
            self.ui.Button_Start.setText("Stop")
            self.serial_connected = True
            QMessageBox.information(self, "Info", f"Koneksi berhasil ke {selected_port}")
        except serial.SerialException as e:
            QMessageBox.critical(self, "Error", f"Gagal membuka port:\n{e}")

    def stop_serial(self):
        self.timer.stop()
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        self.ui.Button_Start.setText("Start")
        self.serial_connected = False
        QMessageBox.information(self, "Info", "Koneksi serial dihentikan.")

    def read_serial_data(self):
        if self.serial_port and self.serial_port.is_open:
            try:
                raw_data = self.serial_port.readline()
                line = raw_data.decode("utf-8", errors="ignore").strip()
                print("Data diterima:", line)

                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        self.ui.line_R.setText(parts[0])
                        self.ui.line_S.setText(parts[1])
                        self.ui.line_T.setText(parts[2])
                        self.evaluate_voltage(parts)
            except Exception as e:
                print(f"Error saat membaca data serial: {e}")


    def evaluate_voltage(self, parts):
        try:
            r = float(parts[0])
            s = float(parts[1])
            t = float(parts[2])
            if 210 <= r <= 230 and 210 <= s <= 230 and 210 <= t <= 230:
                status = "Normal"
            else:
                status = "Tidak Normal"
            self.ui.line_Status.setText(status)
        except ValueError:
            self.ui.line_Status.setText("Data Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
