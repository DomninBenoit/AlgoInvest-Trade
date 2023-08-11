import csv

def create_dict():
    actions_dict = []

    with open('data/forcebrute.csv', 'r') as csvfile:
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
    def recursive_search(index, remaining_money):
        if index >= len(actions_dict) or remaining_money <= 0:
            return 0, []

        # Exclude the current action
        profit_exclude, excluded_actions = recursive_search(index + 1, remaining_money)

        # Include the current action if affordable
        if actions_dict[index]['cost'] <= remaining_money:
            profit_include, included_actions = recursive_search(index + 1, remaining_money - actions_dict[index]['cost'])
            profit_include += actions_dict[index]['profit']

            # Compare and return the maximum profit and associated actions
            if profit_include > profit_exclude:
                return profit_include, [actions_dict[index]] + included_actions
            else:
                return profit_exclude, excluded_actions

        # Return the maximum profit and associated actions
        return profit_exclude, excluded_actions

    best_profit, best_actions = recursive_search(0, money_in_cents)
    return best_actions

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







