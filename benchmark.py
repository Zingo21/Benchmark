import tkinter as tk
import time
from turtle import end_fill, update
from unittest import result
import psutil
import cupy as cp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# save results in lists
cpu_results = []
ram_results = []
gpu_results = []

def benchmark_cpu():
    start = time.time()
    sum([i**2 for i in range(10**6)])
    end = time.time()
    cpu_time = end - start
    cpu_results.append(cpu_time)
    update_plot()
    result_label.config(text=f"CPU-test: {cpu_time:.4f} sec")

def benchmark_ram():
    ram_usage = psutil.virtual_memory().percent
    ram_results.append(ram_usage)
    update_plot()
    result_label.config(text=f"RAM-test: {ram_usage}%")

def benchmark_gpu():
    try:
        start = time.time()
        x = cp.ones((1000, 1000))
        x.dot(x)
        end = time.time()
        gpu_time = end - start
        gpu_results.append(gpu_time)
        update_plot()
        result_label.config(text=f"GPU-test: {gpu_time:.4f} sec")
    except Exception as e:
        result_label.config(text=f"GPU-test failed: {e}")


