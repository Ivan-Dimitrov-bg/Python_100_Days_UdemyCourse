# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import timedelta, datetime
from notification_manager import NotificationManager

# ORIGIN_CITY_IATA = "LON"
ORIGIN_CITY_IATA = "SOF"
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()
flight_search = FlightSearch()
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.



for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        print(sheet_data)
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes(row["city"])

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now() + timedelta(days=6*30)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = flight_search.find_the_best_price(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is not None and flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )