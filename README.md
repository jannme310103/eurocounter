# 💰 Euro Coin & Banknote Counter

An interactive Python tool to calculate the total **value** and **weight** of Euro coins and banknotes. Perfect for quickly estimating how much cash you have – with a sleek terminal progress bar using `rich`.

---

## 🚀 Features

- Choose between:
  - **Coins only**
  - **Banknotes only**
  - **Both coins and banknotes**
- Input validation with retry option
- Calculates the **total value**
- Calculates the **total weight** of coins in grams
- Visual progress bar while counting

---

## 🧰 Tech Stack

- [Python 3.7+](https://www.python.org/)
- [rich](https://github.com/Textualize/rich) – for the terminal progress bar

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/coin-counter.git
   cd coin-counter
   ```
2. Install the required dependency:
   ```bash
   pip install rich
   ```

---

## ▶️ Usage

Launch the program with:
```bash
python main.py
```
Then follow the on-screen instructions to input the quantity of each coin or banknote.
The script will compute the total value and, in the case of coins, also the total weight.

---

## 🧪 Example Output

```bash
Welcome to the Coin Counter!
Please choose an option:

1. Only coins
2. Only banknotes
3. Both coins and banknotes

Enter 1, 2 or 3: 1

1 cent coins: 8 
2 cents coins: 4
5 cents coins: 6
10 cents coins: 0
20 cents coins: 0
50 cents coins: 0
1 euro coins: 0
2 euros coins: 0

Are you sure you entered the correct number of coins? (1=Yes / 2=No): 1
Counting coins... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00

Total weight of your coins: 54.16g
Total value of your coins: 0.46€
```

---

## ✅ Possible Future Enhancements

- 🗂 Export results to CSV

- 🖥 Add a GUI version (e.g. Tkinter or PyQt)

- 💱 Add support for multiple currencies

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributing

Found a bug or have a feature request?
Feel free to fork the project, open issues, or submit pull requests.

Made with ❤️ by Jann
