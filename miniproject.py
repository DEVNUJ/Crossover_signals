import matplotlib.pyplot as plt

def parse_string(user_input):
    user_input_to_string = str(user_input)
    string_splitted = user_input_to_string.split(',')
    interger_list = []
    for num in string_splitted:
        interger = int(num)
        interger_list.append(interger)
    return interger_list


def compute_sma(prices, window):
    listed_price = parse_string(prices)
    if len(listed_price) < window:
        print("Too Less prices to calculate with the given window peroid.")
    caculated_sma = []
    for price in range(window, len(listed_price) + 1):
        selected_prices = listed_price[price - window : price]
        final_sma = round(sum(selected_prices) / window, 2)
        caculated_sma.append(final_sma)
    return caculated_sma


def find_signals(short_sma, long_sma, long_window):
    day_difference = len(short_sma) - len(long_sma) #They are different lengths, so you can't compare index by index yet. 
    short_sma = short_sma[day_difference:]
    signals = []
    for i in range(1, len(long_sma)):
        previous_short_sma = short_sma[i - 1]
        previous_long_sma = long_sma[i - 1]

        current_short_sma = short_sma[i] #first value of the list is stored in previous_short_sma
        current_long_sma = long_sma[i]

        if previous_short_sma <= previous_long_sma and current_short_sma > current_long_sma:
            signals.append((i + long_window, "SELL"))
        elif previous_short_sma >= previous_long_sma and current_short_sma < current_long_sma:
            signals.append((i + long_window , "BUY"))
    return signals


def get_recommendation(signals, short_sma, long_sma):
    if len(signals) == 0:
        if short_sma[-1] > long_sma[-1]:
            print("No crossovers detected. Short SMA is currently above Long SMA — market is in an uptrend.")
        else:
            print("No crossovers detected. Short SMA is currently below Long SMA — market is in a downtrend.")
        return
    
    index, last_signal = signals[-1] #getting the BUY/SELL from the tuple consiting i(day) and the recommendation; for that we need to unpack the tuple first.
    
    if last_signal == "BUY":
        print("Recommendation: Buy! Look for the trading oppurtunities")
    elif last_signal == "SELL":
        print("Recommendation: Sell. Look for either exit or loss minimizing strategy.")
    
def plot_graph(prices, short_sma, long_sma, signals, short_window, long_window):
    listed_price = parse_string(prices)
    days = list(range(1, len(listed_price) + 1))

    short_days = list(range(short_window, len(listed_price) + 1))
    long_days  = list(range(long_window,  len(listed_price) + 1))

    plt.figure(figsize=(12, 6))

    plt.plot(days, listed_price, label="Price", color="gray", linewidth=1.5)
    plt.plot(short_days, short_sma, label=f"Short SMA ({short_window})", color="blue", linewidth=2)
    plt.plot(long_days,  long_sma,  label=f"Long SMA ({long_window})",  color="orange", linewidth=2)

    for day, signal in signals:
        if signal == "BUY":
            plt.scatter(day, listed_price[day - 1], marker="^", color="green", s=150, zorder=5)
        elif signal == "SELL":
            plt.scatter(day, listed_price[day - 1], marker="v", color="red", s=150, zorder=5)

    plt.title("SMA Crossover Chart")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def main():
    print("Welcome to MOVING AVERAGE CROSSOVER SIGNAL GENERATOR")
    price_string = input("Enter the historical prices seperated by commas: ")
    short_window = int(input("Enter the short window size: "))
    long_window = int(input("Enter the long window size: "))

    short_sma_show = compute_sma(price_string, short_window)
    long_sma_show = compute_sma(price_string, long_window)
    print(f"Short SMA with window {short_window}: {short_sma_show}")
    print(f"Long SMA with window {long_window}: {long_sma_show}")

    signals = find_signals(short_sma_show, long_sma_show, long_window)
    plot_graph(price_string, short_sma_show, long_sma_show, signals, short_window,long_window)
    print(f"Signals: {signals}")
    
    get_recommendation(signals, short_sma_show, long_sma_show)

main()