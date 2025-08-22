# ⏰ Time Calculator

A tiny utility that adds a duration to a start time in 12-hour format, with optional weekday handling and “next day / days later” labeling.

It was created as part of my **Scientific Computing with Python Certification**.  
👉 [View my certification here](https://freecodecamp.org/certification/lucawaldvogel/scientific-computing-with-python-v7)

---

## 🚀 Features

- Adds a duration (`HH:MM`) to a start time (`H:MM AM/PM`)
- 12-hour clock with correct AM/PM flips
- Optional weekday input (case-insensitive) → returns the resulting weekday
- Labels day rollovers: **(next day)** or **(\<n> days later)**
- Simple, dependency-free implementation

---

## 📖 Example

### Input
```python
add_time('11:55 AM', '12:07', 'Monday')
```
**Parameters:** start: e.g. "11:55 AM", duration: e.g. "12:07", weekday (optional): e.g. "Monday" (any case)

### Output
```python
12:02 AM, Tuesday (next day)
```
