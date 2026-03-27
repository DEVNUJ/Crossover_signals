# Moving Average Crossover Signal Generator

A Python-based trading signal tool that analyzes historical stock prices using **Simple Moving Averages (SMA)** to identify potential **Buy** and **Sell** signals — complete with an interactive chart visualization.

---

## What It Does

This tool implements a classic **SMA crossover strategy** used in technical analysis:

- Computes a **short-term SMA** and a **long-term SMA** from user-provided historical prices
- Detects **crossover points** where the short SMA crosses above or below the long SMA
- Generates **BUY / SELL signals** based on those crossovers
- Plots an annotated price chart with both SMAs and signal markers
- Prints a final **trading recommendation** based on the most recent signal

---

## Built With

- **Python 3**
- **Matplotlib** — for chart visualization

---

## Getting Started

### Prerequisites

Make sure you have Python 3 and Matplotlib installed:

```bash
pip install matplotlib
```

### Run the Program

```bash
python miniproject.py
```

You will be prompted to enter:
1. **Historical prices** — comma-separated integers (e.g. `100,102,105,103,108,112,110`)
2. **Short window size** — e.g. `3`
3. **Long window size** — e.g. `5`

---

## Example

```
Enter the historical prices separated by commas: 100,102,101,105,110,108,112,115,113,118
Enter the short window size: 3
Enter the long window size: 5

Short SMA (3): [101.0, 102.67, 105.33, 107.67, 110.0, 111.67, 113.33, 115.33]
Long SMA  (5): [103.6, 105.2, 107.2, 109.6, 111.6, 113.2]

Signals: [(8, 'BUY')]
Recommendation: Buy! Look for trading opportunities.
```

A chart will pop up showing:
- Gray line — raw price
- Blue line — Short SMA
- Orange line — Long SMA
- Green triangle — BUY signal
- Red triangle — SELL signal

---

## How the Strategy Works

| Crossover Event | Signal |
|---|---|
| Short SMA crosses **above** Long SMA | SELL |
| Short SMA crosses **below** Long SMA | BUY |

> Note: This tool is for educational purposes only and does not constitute financial advice.

---

## Project Structure

```
miniproject.py       # Main script — all logic and visualization
README.md            # Project documentation
```

---

## Author

Made by [Anuj Paudel (https://github.com/DEVNUJ)]
Feel free to fork, use, or suggest improvements!
