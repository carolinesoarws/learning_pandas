import pandas as pd

purchase_orders = {
    "PurchaseOrders": [
        {
            "PurchaseOrderNo": 1,
            "Address": [
                {
                    "Type": "Shipping",
                    "Name": "Ellen Adams",
                    "Street": "123 Maple Street",
                    "City": "Mill Valley",
                    "State": "CA",
                    "Zip": 10999,
                    "Country": "USA"
                },
                {
                    "Type": "Billing",
                    "Name": "Tai Yee",
                    "Street": "8 Oak Avenue",
                    "City": "Old Town",
                    "State": "PA",
                    "Zip": 95819,
                    "Country": "USA"
                }
            ],
            "DeliveryNotes": "Please leave packages in shed by driveway.",
            "Items": {
                "Item": [
                    {
                        "PartNumber": "872-AA",
                        "ProductName": "Lawnmower",
                        "Quantity": 1,
                        "USPrice": 148.95,
                        "Comment": "Confirm this is electric"
                    },
                    {
                        "PartNumber": "926-AA",
                        "ProductName": "Baby Monitor",
                        "Quantity": 2,
                        "USPrice": 39.98,
                        "ShipDate": "1999-05-21"
                    }
                ]
            }
        },
        {
            "PurchaseOrderNo": 2,
            "Address": [
                {
                    "Type": "Shipping",
                    "Name": "Cristian Osorio",
                    "Street": "456 Main Street",
                    "City": "Buffalo",
                    "State": "NY",
                    "Zip": 98112,
                    "Country": "USA"
                },
                {
                    "Type": "Billing",
                    "Name": "Cristian Osorio",
                    "Street": "456 Main Street",
                    "City": "Buffalo",
                    "State": "NY",
                    "Zip": 98112,
                    "Country": "USA"
                }
            ],
            "DeliveryNotes": "Please notify me before shipping.",
            "Items": {
                "Item": {
                    "PartNumber": "456-NM",
                    "ProductName": "Power Supply",
                    "Quantity": 1,
                    "USPrice": 45.99
                }
            }
        },
        {
            "PurchaseOrderNo": 3,
            "Address": [
                {
                    "Type": "Shipping",
                    "Name": "Jessica Arnold",
                    "Street": "4055 Madison Ave",
                    "City": "Seattle",
                    "State": "WA",
                    "Zip": 98112,
                    "Country": "USA"
                },
                {
                    "Type": "Billing",
                    "Name": "Jessica Arnold",
                    "Street": "4055 Madison Ave",
                    "City": "Buffalo",
                    "State": "NY",
                    "Zip": 98112,
                    "Country": "USA"
                }
            ],
            "Items": {
                "Item": [
                    {
                        "PartNumber": "898-AZ",
                        "ProductName": "Computer Keyboard",
                        "Quantity": 1,
                        "USPrice": 29.99
                    },
                    {
                        "PartNumber": "898-AM",
                        "ProductName": "Wireless Mouse",
                        "Quantity": 1,
                        "USPrice": 14.99
                    }
                ]
            }
        }
    ]
}


def flatten_json(my_json):
    new_dict = {}

    def flatten(data, name=''):
        if type(data) is dict:
            for item in data:
                flatten(data[item], name + item + '_')
        elif type(data) is list:
            i = 0
            for item in data:
                flatten(item, name + str(i) + '_')
                i += 1
        else:
            new_dict[name[:-1]] = data

    flatten(my_json)
    return new_dict


"""
  First i break the json into a list of dict with the 3 orders. 
"""
# Separating the dicts
separated_dicts = purchase_orders["PurchaseOrders"]
flatten_purchese_orders = []

for item in separated_dicts:
    flatten_purchese_orders.append(flatten_json(item))
print(flatten_purchese_orders)

# Creating my DataFrame using pandas
df = pd.json_normalize(flatten_purchese_orders)

# if you see the print of the dataframe some of the information will be null because not all the purchase orders has
# many items
print(df.to_string())

# The problem is that to generate the csv wouldn't be a good solution because some of the information will be as NaN
# To fix that we can use fillna to changed the NaN (Null values) to 0.
df_normalized = df.fillna(0)
print(df_normalized.to_string())

# After that we can generate our csv with no problem
df_normalized.to_csv("purchase_orders.csv", sep=",")
