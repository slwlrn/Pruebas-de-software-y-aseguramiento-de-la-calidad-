"""
Compute Sales Script

This script reads a product catalog and sales data from JSON files
and calculates the total sales amount, handling errors gracefully.
"""

import json
import sys
import time


def load_json_file(filename):
    """Loads and returns JSON data from a given file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")
        sys.exit(1)


def compute_sales(products_filename, sales_filename):
    """Computes total sales cost from product and sales records."""
    start_time = time.time()

    # Load product catalog and sales data
    products_data = load_json_file(products_filename)
    sales_data = load_json_file(sales_filename)

    # Create a price dictionary from product catalog
    price_dict = {
        product.get("title"): product.get("price")
        for product in products_data
        if product.get("title") and isinstance(product.get("price"), (int, float))
    }

    total_sales = sum(
        price_dict.get(sale.get("Product"), 0) * abs(sale.get("Quantity", 0))
        for sale in sales_data
        if sale.get("Product") in price_dict
    )

    total_sales_with_negatives = sum(
        price_dict.get(sale.get("Product"), 0) * sale.get("Quantity", 0)
        for sale in sales_data
        if sale.get("Product") in price_dict
    )

    invalid_entries = [
        f"Invalid product: {sale.get('Product')}"
        for sale in sales_data if sale.get("Product") not in price_dict
    ]

    end_time = time.time()
    execution_time = end_time - start_time

    # Print formatted results to console
    print("======== SALES REPORT ========")
    print(f"Total Sales (excluding negatives): ${total_sales:,.2f}")
    print(f"Total Sales (including negatives): ${total_sales_with_negatives:,.2f}")
    print(f"Execution Time: {execution_time:.4f} seconds")
    print("---------------------------------")
    if invalid_entries:
        print("Errors:")
        for error in invalid_entries:
            print(f"  - {error}")
    print("================================")

    # Append formatted results to file instead of overwriting
    with open("SalesResults.txt", 'a', encoding='utf-8') as result_file:
        result_file.write("======== SALES REPORT ========\n")
        result_file.write(f"Total Sales (excluding negatives):${total_sales:,.2f}\n")
        result_file.write(f"Total Sales (including negatives):${total_sales_with_negatives:,.2f}\n")
        result_file.write(f"Execution Time: {execution_time:.4f} seconds\n")
        result_file.write("---------------------------------\n")
        if invalid_entries:
            result_file.write("Errors:\n")
            for error in invalid_entries:
                result_file.write(f"  - {error}\n")
        result_file.write("================================\n")

    print("Results appended to SalesResults.txt")


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python compute_sales.py <ProductCatalog.json> <SalesRecord.json>")
        sys.exit(1)

    input_product_file = sys.argv[1]
    input_sales_file = sys.argv[2]
    compute_sales(input_product_file, input_sales_file)
