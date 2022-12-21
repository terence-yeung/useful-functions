def create_sales_lag(df, lag_list, window_list):
# Function to create sales (target) lag and lagged rolling mean features
# Params:
# df - Dataframe
# lag_list (list) - List of timesteps to lag
# window_list (list) - List of windows over which to calculate rolling mean, using the same lags as in lag_list
# Returns dataframe with new features added

    lag_cols = [f"Sales_Lag_{lag}" for lag in lag_list]
    for lag, lag_col in zip(lag_list, lag_cols):
        df[lag_col] = df[["SKU", "Sales"]].groupby("SKU")["Sales"].shift(lag)

    for win in window_list:
        for lag, lag_col in zip(lag_list, lag_cols):
            df[f"Sales_RM_{lag}_{win}"] = df[["SKU", lag_col]].groupby("SKU")[lag_col].transform(lambda x: x.rolling(win).mean())
    print("Sales lag features created")
    return df

def create_price_windows(df, window_list):
# Function to create price rolling mean features
# Params:
# df - Dataframe
# window_list (list) - List of windows over which to calculate rolling mean
# Returns dataframe with new features added
    for win in window_list:
        df[f"Price_RM_{win}"] = df[["SKU","Sell_Price"]].groupby(["SKU"])["Sell_Price"].transform(lambda x : x.rolling(win).mean())
        df[f"Price_RM_{win}_Dif"] = ((df["Sell_Price"] - df[f"Price_RM_{win}"]) / df["Sell_Price"]).round(3) # Difference between rolling mean price and price (Rolling mean can be dropped if wanted)
    return df
