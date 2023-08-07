import csv

def create_dict():
    actions_dict = []
    actions_name = []
    actions_cost = []
    actions_profit = []

    with open ('data/forcebrute.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            actions_name.append(row[0])
            actions_cost.append(row[1])
            actions_profit.append(row[2])

    for i in range(len(actions_cost)):
        action_cost = float(actions_cost[i])
        actions_cost[i] = int(action_cost * 100)

    for i in range (len(actions_profit)):
        actions_profit[i] = float(actions_profit[i])

    for i in range (len(actions_name)):
        if actions_cost[i] and actions_profit[i] > 0:
            actions_dict.append({"name": actions_name[i], "cost": actions_cost[i], "profit": int((actions_cost[i] * actions_profit[i]) / 100)})
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
    for action in selected_actions:
        print(f"Name: {action['name']}, Cost: {action['cost']}, Profit: {action['profit']}")


if __name__ == "__main__":
    main()






