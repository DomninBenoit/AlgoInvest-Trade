import csv

def create_dict():
    actions_dict = []

    with open('data/dataset2.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            name = row[0]
            cost = int(float(row[1]) * 100)
            profit = float(row[2])
            if cost > 0 and profit > 0:
                actions_dict.append({"name": name, "cost": cost, "profit": int(cost * profit)})

    return actions_dict

def maximize_profit(actions_dict, money_in_cents):
    actions_dict.sort(key=lambda x: x['profit'] / x['cost'], reverse=True)
    selected_actions = []

    for action in actions_dict:
        if action['cost'] <= money_in_cents:
            selected_actions.append(action)
            money_in_cents -= action['cost']

    return selected_actions

def main():
    actions_dict = create_dict()
    money = 500
    money_in_cents = money * 100

    selected_actions = maximize_profit(actions_dict, money_in_cents)
    print("Selected actions:")
    total_cost = 0
    total_profit = 0
    for action in selected_actions:
        print(f"Name: {action['name']}, Cost: {action['cost']}")
        total_cost += action['cost']
        total_profit += action['profit']

    print(f"Total Cost: {total_cost / 100}, Total Profit: {total_profit / 10000}")

if __name__ == "__main__":
    main()
