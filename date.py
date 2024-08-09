from datetime import datetime , timedelta

start_date = datetime(2024,5,1)
end_date = datetime(2024,6,30)

while start_date <= end_date:
    cust_date = start_date.strftime("%Y-%m-%d")
    print(cust_date)
    start_date += timedelta(days=1)