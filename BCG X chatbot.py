import pandas as pd
import time

# Load the CSV dataset
db = pd.read_csv('Updated Datasheet.csv')
db.drop(db.columns[0], axis=1, inplace=True)

def simple_chatbot(company, year, user_query):
    """A function that simulates a chatbot.
    param: company, company that data is required on, e.g. Microsoft
    param: year, the required year e.g. 2021
    param: user_query, required data e.g. 'What is the total revenue?'
    """
    # Query the dataset based on the company and year
    query_result = db.query(f"Company == '{company}' & Year == {year}")
    
    if query_result.empty:
        return "Sorry, no data available for the requested company and year."

    if user_query == "What is the total revenue?":
        total_revenue = query_result['Total Revenue'].values[0]
        return f"The total revenue for {company} is ${total_revenue} million for {year}."

    elif user_query == "What is the net income?":
        net_income = query_result['Net Income'].values[0]
        return f"The net income for {company} is ${net_income} million for {year}."

    elif user_query == "What are the total assets?":
        total_assets = query_result['Total Assets'].values[0]
        return f"The total assets for {company} are ${total_assets} million for {year}."

    elif user_query == "What are the total liabilities?":
        total_liabilities = query_result['Total Liabilities'].values[0]
        return f"The total liabilities for {company} are ${total_liabilities} million for {year}."

    elif user_query == "What is the cash flow from operating activities?":
        cash_flow = query_result['Cash Flow from Operating Activities'].values[0]
        return f"The cash flow from operating activities for {company} is ${cash_flow} million for {year}."

    elif user_query == "How has revenue changed?":
        revenue_growth = query_result['Revenue Growth (%)'].values[0]
        return f"Revenue for {company} changed by {revenue_growth}% in {year}."

    elif user_query == "How has net income changed?":
        net_income_growth = query_result['Net Income Growth (%)'].values[0]
        return f"Net income for {company} changed by {net_income_growth}% in {year}."

    else:
        return "Sorry, I can only provide information on predefined queries."

def main():
    YEARS = db['Year'].unique()
    COMPANIES = db['Company'].unique()

    while True:
        print('-'*50)
        print('Financial Data Chatbot v.1.0\n')
        print('-'*50)

        prompt = "\nEnter the company you would like data on (e.g., Microsoft, Tesla, Apple): "
        company = str(input(prompt).title()) 
        try:
            if company.lower() == 'exit':
                break

            year = int(input("\nEnter a valid year (e.g., 2021, 2022, 2023): "))

            assert company in COMPANIES, 'You have entered an invalid company'
            assert year in YEARS, 'You have entered an invalid year'

            user_query = str(input('\nEnter a query: '))

            print("\nLet me try and retrieve that data...\n")
            time.sleep(2)

            print(simple_chatbot(company, year, user_query))

        except AssertionError as error_message:
            print(error_message)

    print('\nGoodbye, have a nice day!')

if __name__ == "__main__":
    main()
