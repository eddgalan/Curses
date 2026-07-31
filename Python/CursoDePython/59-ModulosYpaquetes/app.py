import reports

if __name__ == '__main__':
    sales_report = reports.generate_sales_report('Enero', 100000)
    expenses_report = reports.generate_expenses_report('Enero', 6000)

    print(sales_report)
    print(expenses_report)
