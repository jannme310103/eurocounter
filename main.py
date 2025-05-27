from rich.progress import Progress
import time

one_cent = 0.01
two_cents = 0.02
five_cents = 0.05
ten_cents = 0.10
twenty_cents = 0.20
fifty_cents = 0.50
one_euro = 1.00
two_euros = 2.00

five_euros = 5.00
ten_euros = 10.00
twenty_euros = 20.00
fifty_euros = 50.00
hundred_euros = 100.00
twohundred_euros = 200.00
fivehundred_euros = 500.00

weight_one_cent = 2.30
weight_two_cents = 3.06
weight_five_cents = 3.92
weight_ten_cents = 4.10
weight_twenty_cents = 5.74
weight_fifty_cents = 7.80
weight_one_euro = 7.50
weight_two_euros = 8.50


def main():
    print("Welcome to the Coin Counter!")

    print("Please choose an option:")
    print("\n1. Only coins")
    print("2. Only banknotes")
    print("3. Both coins and banknotes")

    choice = input("\nEnter 1, 2 or 3: ")

    if choice == '1':
        coins = coin_inputs()
        coin_weight = weight_coins(coins)
        total_value_coins = count_coins(coins)
        total_weight_coins = weight_coins(coins)

        total_coins = coins.count(0) + coins.count(1) + coins.count(2) + coins.count(3) + \
                      coins.count(4) + coins.count(5) + coins.count(6) + coins.count(7)

        with Progress() as p1:
            t1 = p1.add_task("[green]Counting coins...", total=total_coins)
            while not p1.finished:
                p1.update(t1, advance=1)
                time.sleep(0.1)

        print(f"\nTotal weight of your coins: {total_weight_coins:.2f}g")
        print(f"Total value of your coins: {total_value_coins:.2f}€")

    elif choice == '2':
        banknotes = banknote_inputs()
        total_value_banknotes = count_banknotes(banknotes)

        total_banknotes = banknotes.count(0) + banknotes.count(1) + banknotes.count(2) + \
                        banknotes.count(3) + banknotes.count(4) + banknotes.count(5) + \
                        banknotes.count(6)

        with Progress() as p2:
            t2 = p2.add_task("[green]Counting banknotes...", total=total_banknotes)
            while not p2.finished:
                p2.update(t2, advance=1)
                time.sleep(0.1)

        print(f"\nTotal value of your banknotes: {total_value_banknotes:.2f}€")

    elif choice == '3':
        coins = coin_inputs()
        coin_weight = weight_coins(coins)
        banknotes = banknote_inputs()
        total_weight_coins = weight_coins(coins)
        total_value = count_coins(coins) + count_banknotes(banknotes)

        total_coins_and_banknotes = coins.count(0) + coins.count(1) + coins.count(2) + coins.count(3) + \
                                    coins.count(4) + coins.count(5) + coins.count(6) + coins.count(7) + \
                                    banknotes.count(0) + banknotes.count(1) + banknotes.count(2) + \
                                    banknotes.count(3) + banknotes.count(4) + banknotes.count(5) + \
                                    banknotes.count(6)

        with Progress() as p3:
            t3 = p3.add_task("[green]Counting coins and banknotes...", total=total_coins_and_banknotes)
            while not p3.finished:
                p3.update(t3, advance=1)
                time.sleep(0.1)

        print(f"\nTotal weight of your coins: {total_weight_coins:.2f}g")
        print(f"Total value: {total_value:.2f}€")

    else:
        print("Invalid option. Please restart the program.")

def coin_inputs():
    try:
        num_one_cent = float(input("\n1 cent coins: "))
        num_two_cents = float(input("2 cents coins: "))
        num_five_cents = float(input("5 cents coins: "))
        num_ten_cents = float(input("10 cents coins: "))
        num_twenty_cents = float(input("20 cents coins: "))
        num_fifty_cents = float(input("50 cents coins: "))
        num_one_euro = float(input("1 euro coins: "))
        num_two_euros = float(input("2 euros coins: "))

        coins = (num_one_cent, num_two_cents, num_five_cents,
                 num_ten_cents, num_twenty_cents, num_fifty_cents,
                 num_one_euro, num_two_euros)

        confirmation = input("\nAre you sure you entered the correct number of coins? (1=Yes / 2=No): ")
        if confirmation == '2':
            print("Let's try again.")
            return coin_inputs()
        return coins

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return coin_inputs()
    
def banknote_inputs():
    """Get user input for the number of banknotes."""
    try:
        num_five_euros = float(input("\n5 euro banknotes: "))
        num_ten_euros = float(input("10 euro banknotes: "))
        num_twenty_euros = float(input("20 euro banknotes: "))
        num_fifty_euros = float(input("50 euro banknotes: "))
        num_hundred_euros = float(input("100 euro banknotes: "))
        num_twohundred_euros = float(input("200 euro banknotes: "))
        num_fivehundred_euros = float(input("500 euro banknotes: "))
        
        banknotes = (num_five_euros, num_ten_euros, num_twenty_euros, 
                num_fifty_euros, num_hundred_euros, 
                num_twohundred_euros, num_fivehundred_euros)
    
        confirmation = input("\nAre you sure you entered the correct number of coins? (1=Yes / 2=No): ")
        if confirmation == '2':
            print("Let's try again.")
            return banknote_inputs()
        return banknotes

    except ValueError:
        print("Invalid input. Please enter integers only.")
        return banknote_inputs()
    
def count_coins(coins):
    """Calculate the total value of coins."""

    total_value_coins = (coins[0] * one_cent + coins[1] * two_cents + 
                   coins[2] * five_cents + coins[3] * ten_cents + 
                   coins[4] * twenty_cents + coins[5] * fifty_cents + 
                   coins[6] * one_euro + coins[7] * two_euros)
    
    return total_value_coins
    
def count_banknotes(banknotes):
    """Calculate the total value of banknotes."""

    total_value_banknotes = (banknotes[0] * five_euros + banknotes[1] * ten_euros + 
                   banknotes[2] * twenty_euros + banknotes[3] * fifty_euros + 
                   banknotes[4] * hundred_euros + 
                   banknotes[5] * twohundred_euros + 
                   banknotes[6] * fivehundred_euros)
    
    return total_value_banknotes

def weight_coins(coins):
    """Calculate the total weight of coins."""
    
    total_weight_coins = (coins[0] * weight_one_cent + coins[1] * weight_two_cents +
                   coins[2] * weight_five_cents + coins[3] * weight_ten_cents + 
                   coins[4] * weight_twenty_cents + coins[5] * weight_fifty_cents + 
                   coins[6] * weight_one_euro + coins[7] * weight_two_euros)
    
    return total_weight_coins

if __name__ == "__main__":
    main()