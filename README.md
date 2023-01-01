# Boat Listing Case Study

## Background
Nearly New Nautical is a website that allows users to advertise their used boats for sale. When users list their boat, they have to provide a range of information about their boat. Boats that get lots of views bring more traffic to the website, and more potential customers.

To boost traffic to the website, the product manager wants to prevent listing boats that do not receive many views.

## Customer Question
The product manager wants to know the following:
- Can the number of views a listing will receive based on the boat's features be predicted?

## Success Criteria
The product manager would consider using the model if, on average, the predictions were only 50% off of the true number of views a listing would receive.

## Result
CatBoostRegressor model gives a MAPE result of 0.5 (50%).
