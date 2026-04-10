# 🖱️ FramePerfect Autoclicker

A no-nonsense autoclicker built for high refresh rate monitors. Uses a high-precision busy-wait loop to hit a consistent frame perfect click — no drift, no jitter.

Open source, ~50 lines of Python. No installers, no telemetry, no mystery.

**Platform:** Tested on Linux and Windows. macOS should work but is untested.

---

## Why this instead of anything else?

Most autoclickers are sketchy closed-source executables you just have to trust. This one:

- **Open source and auditable** — you can read the entire thing in under a minute
- **No servers, fully local** — runs entirely on your machine, no network calls whatsoever
- **High-precision timing** — uses `time.perf_counter()` busy-wait for consistent clicking, not OS sleep timers which drift
- **Lightweight** — simple PyQt5 window, no bloat

---

## Features

- 180 clicks per second (configurable by changing `1.0 / 180.0`)
- F6 hotkey to toggle on/off
- Status display (IDLE / RUNNING / STOPPED)
- Runs in background thread, UI stays responsive

---

## Requirements

### Python packages
```
pip install pyqt5 pynput keyboard
```

> ⚠️ On Linux, the `keyboard` library requires root for global hotkeys. Run with `sudo python AutoClicker.py` or set up uinput permissions.

### Full requirements at a glance
```
Python 3.8+
PyQt5
pynput
keyboard
```

---

## Usage

```bash
python AutoClicker.py
```

1. Window opens showing current status
2. Press **F6** to start clicking
3. Press **F6** again to stop

---

## Notes

- Click rate is set to 180Hz by default to match high refresh rate monitors — change `self.frame_time = 1.0 / 180.0` to whatever rate you want
- The busy-wait loop will use one CPU core at ~100% while active — this is intentional for timing precision

---

## License

Do whatever you want with it.
