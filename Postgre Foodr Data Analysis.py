# Required Libraries
import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus

def main():
    try:
        # Step 1: Connect to PostgreSQL
        db_user = "postgres"
        db_pass = "Efficiency@25"  # Contains @ symbol
        db_host = "localhost"
        db_port = "5432"
        db_name = "Foodr"

        # URL-encode the password
        encoded_password = quote_plus(db_pass)
        engine = create_engine(f"postgresql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}")

        # Test connection
        with engine.connect() as conn:
            print("✅ Connected to the database successfully!")

            # Step 2: Load tables into Pandas DataFrames
            meals_df = pd.read_sql("SELECT * FROM meals", engine)
            orders_df = pd.read_sql("SELECT * FROM orders", engine)
            stock_df = pd.read_sql("SELECT * FROM stock", engine)

            print("\nMeals data sample:")
            print(meals_df.head())
            print("\nOrders data sample:")
            print(orders_df.head())
            print("\nStock data sample:")
            print(stock_df.head())

            # Task 1: Unique meals and eateries
            print("\n✅ Task 1: Unique counts")
            print(f"Unique meals: {meals_df['meal_id'].nunique()}")
            print(f"Unique eateries: {meals_df['eatery'].nunique()}")

            # Task 2: Revenue per meal
            meals_price_map = meals_df.set_index('meal_id')['meal_price']
            orders_df['order_revenue'] = orders_df['order_quantity'] * orders_df['meal_id'].map(meals_price_map)

            revenue_per_meal = (orders_df.groupby('meal_id')['order_revenue'].sum()
                                .reset_index()
                                .merge(meals_df[['meal_id', 'eatery']], on='meal_id'))

            print("\n✅ Task 2: Top 5 revenue-generating meals:")
            print(revenue_per_meal.nlargest(5, 'order_revenue'))

            # Task 3: Profit analysis
            meals_df['profit_margin'] = meals_df['meal_price'] - meals_df['meal_cost']

            orders_df = orders_df.merge(meals_df[['meal_id', 'meal_cost', 'meal_price', 'eatery']],
                                        on='meal_id', how='left')

            orders_df['total_cost'] = orders_df['order_quantity'] * orders_df['meal_cost']
            orders_df['total_price'] = orders_df['order_quantity'] * orders_df['meal_price']
            orders_df['profit'] = orders_df['total_price'] - orders_df['total_cost']

            profit_by_eatery = (orders_df.groupby('eatery')['profit'].sum()
                                .sort_values(ascending=False)
                                .reset_index())

            print("\n✅ Task 3: Total profit by eatery:")
            print(profit_by_eatery)

            # Task 4: Stock analysis
            stocked = stock_df.groupby('meal_id')['stocked_quantity'].sum()
            ordered = orders_df.groupby('meal_id')['order_quantity'].sum()

            stock_vs_orders = pd.DataFrame({
                'stocked': stocked,
                'ordered': ordered
            }).fillna(0)

            stock_vs_orders['leftover'] = stock_vs_orders['stocked'] - stock_vs_orders['ordered']
            oversold = stock_vs_orders[stock_vs_orders['leftover'] < 0]

            print("\n✅ Task 4: Meals with negative leftover stock (oversold):")
            print(oversold)

            # Task 5: Revenue trend
            daily_revenue = (orders_df.groupby('order_date')['total_price'].sum()
                             .reset_index()
                             .sort_values('order_date'))

            daily_revenue['7_day_avg'] = daily_revenue['total_price'].rolling(window=7).mean()

            print("\n✅ Task 5: Revenue trend (last 10 days):")
            print(daily_revenue.tail(10))

        except SQLAlchemyError as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
    finally:
        if 'engine' in locals():
            engine.dispose()
            print("Database connection closed.")


if __name__ == "__main__":
    main()