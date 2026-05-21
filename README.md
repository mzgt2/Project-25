# Project-25

# Miles to Kilometers Converter 🛣️

A simple GUI application built with Tkinter that converts miles to kilometers with a single click.

## Requirements

```bash
# Built-in library (no installation needed)
from tkinter import *
```

## How to Run

```bash
python miles_to_km_converter.py
```

## Features

✅ Clean GUI interface  
✅ Real-time conversion  
✅ Accurate calculation (1 mile = 1.609344 km)  
✅ Rounded to 2 decimal places  
✅ Simple and intuitive design  

## How to Use

1. Enter a number in the input field (miles)
2. Click the **Calculate** button
3. Result displays in kilometers

## Example
Input: 10 Miles
Output: 16.09 Km
Input: 26.2 Miles (marathon distance)
Output: 42.16 Km
Input: 100 Miles
Output: 160.93 Km


## Conversion Formula
Kilometers = Miles × 1.609344

## Customization

### Change Window Size
```python
window.minsize(width=400, height=150)
```

### Different Decimal Precision
```python
km = round(float(user_input * 1.609344), 3)  # 3 decimal places
```

### Reverse Conversion (Km to Miles)
```python
def calculate():
    user_input = float(entry.get())
    miles = round(float(user_input / 1.609344), 2)
    label_4.config(text=f"{miles}")
```

### Add Window Icon
```python
window.iconbitmap('icon.ico')
```

## What I Learned

- **Tkinter basics** - Creating GUI windows and widgets
- **Widget positioning** - Using `.grid()` for layout management
- **Event handling** - Button commands with `command=calculate`
- **Entry widgets** - Getting user input with `.get()`
- **Label updates** - Dynamic text changes with `.config()`
- **Type conversion** - Converting strings to floats for calculations
- **Rounding** - Using `round()` for clean output

Simple and functional distance converter! 📏
