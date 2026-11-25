"""A small sales summary for a made-up company.

All the data is built in, so there is nothing to download or load.
"""

SALES = [
    {"product": "Laptop", "region": "East", "amount": 1200},
    {"product": "Laptop", "region": "West", "amount": 1100},
    {"product": "Phone", "region": "East", "amount": 800},
    {"product": "Phone", "region": "North", "amount": 750},
    {"product": "Tablet", "region": "West", "amount": 500},
    {"product": "Tablet", "region": "North", "amount": 450},
    {"product": "Monitor", "region": "East", "amount": 300},
    {"product": "Monitor", "region": "West", "amount": 320},
    {"product": "Headphones", "region": "North", "amount": 150},
    {"product": "Headphones", "region": "East", "amount": 180},
]


def total_revenue(sales):
    return sum(sale["amount"] for sale in sales)


def revenue_by_product(sales):
    totals = {}
    for sale in sales:
        totals[sale["product"]] = totals.get(sale["product"], 0) + sale["amount"]
    return totals


def revenue_by_region(sales):
    totals = {}
    for sale in sales:
        totals[sale["region"]] = totals.get(sale["region"], 0) + sale["amount"]
    return totals


def top_product(sales):
    by_product = revenue_by_product(sales)
    return max(by_product, key=by_product.get)


def main():
    print("Sales summary")
    print(f"Total revenue: ${total_revenue(SALES):,}")
    print(f"Top product: {top_product(SALES)}")
    print("Revenue by region:")
    for region, amount in sorted(revenue_by_region(SALES).items()):
        print(f"  {region}: ${amount:,}")


if __name__ == "__main__":
    main()
