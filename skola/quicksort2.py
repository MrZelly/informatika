import tkinter as tk
import random
import time
#import pyaudio
#import numpy as np

# def play_frequency(frequency, duration):
#     sample_rate = 44100  # Sample rate in samples per second
#     num_samples = int(sample_rate * duration)
#     t = np.linspace(0, duration, num_samples, False)
#     audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
    
#     p = pyaudio.PyAudio()
    
#     stream = p.open(format=pyaudio.paFloat32,
#                     channels=1,
#                     rate=sample_rate,
#                     output=True)
    
#     stream.write(audio_data.tobytes())
#     stream.stop_stream()
#     stream.close()
    
#     p.terminate()

# Function to perform quicksort and update the GUI
def quicksort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        root.update()
        #time.sleep(0.05)  # Add a small delay for visualization
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

# Function to partition the array
def partition(arr, left, right):
    global steps
    pivot_index = random.randint(left, right)  # Choose a random pivot
    pivot_value = arr[pivot_index]
    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]  # Move pivot to the end
    low = left - 1
    
    for i in range(left, right):
        if arr[i] < pivot_value:
            low += 1
            arr[i], arr[low] = arr[low], arr[i]  # Swap elements
            update_display(arr, left, right, low, i)
            steps += 1
    arr[low + 1], arr[right] = arr[right], arr[low + 1]
    update_display(arr, left, right, low + 1, right)
    
    return low + 1

# Function to update the displays
def update_display(arr, left, right, low, current):
    canvas.delete("all")
    bar_width = canvas_width / len(arr)
    
    for i, val in enumerate(arr):
        color = "lightblue" if i == current else "white"
        canvas.create_rectangle(
            i * bar_width, canvas_height, (i + 1) * bar_width, canvas_height - (val),
            fill=color, outline=""
        )
        canvas.create_text(10, 20, text="Current: " + str(current), fill = "white", font = "Arial 15", anchor="w")
        canvas.create_text(10, 40, text="Steps: " + str(steps), fill = "white", font = "Arial 15", anchor="w")
        #play_frequency(440 + current * 10, 2)

    
    root.update_idletasks()

steps = 0
# Create a random array for visualization
array_size = 500
#array = [random.randint(1, 1000) for _ in range(array_size)]
array = []
for i in range(array_size):
    array.append(i)

random.shuffle(array)

# Create the Tkinter window and canvas
root = tk.Tk()
root.title("Quicksort Visualization")
canvas_width = 1200
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
canvas.pack()

# Call the quicksort function
quicksort(array, 0, len(array) - 1)

root.mainloop()
