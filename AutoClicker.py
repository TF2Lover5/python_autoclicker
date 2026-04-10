import sys
import threading
import time
from pynput.mouse import Button, Controller
import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

# Use pynput for lower overhead than pyautogui
mouse = Controller()

class HighSpeedClicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("180Hz Autoclicker")
        self.is_clicking = False
        
        # 180Hz = ~0.005555 seconds per frame
        self.frame_time = 1.0 / 180.0 

        layout = QVBoxLayout()
        self.label = QLabel("Status: IDLE\nPress F6 to Start/Stop")
        layout.addWidget(self.label)
        self.setLayout(layout)

        keyboard.add_hotkey("F6", self.toggle_clicking)

    def click_loop(self):
        next_click = time.perf_counter()
        
        while self.is_clicking:
            # High-precision busy-wait
            while time.perf_counter() < next_click:
                pass 
            
            mouse.click(Button.left, 1)
            next_click += self.frame_time

    def toggle_clicking(self):
        self.is_clicking = not self.is_clicking
        if self.is_clicking:
            self.label.setText("Status: RUNNING (180Hz)")
            threading.Thread(target=self.click_loop, daemon=True).start()
        else:
            self.label.setText("Status: STOPPED")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HighSpeedClicker()
    window.show()
    sys.exit(app.exec_())