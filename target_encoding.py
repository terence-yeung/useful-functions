def encode_static(df):
# Function to encode static features (SKU, product category etc.) by the expanding mean/SD of the sales (target)
# Params:
# df - Dataframe
# Returns dataframe with new features added
    # SKU
    df["SKU_Sales_Shift"] = df[["SKU", "Sales"]].groupby("SKU")["Sales"].shift()
    df["SKU_Encoded"] = df[["SKU", "SKU_Sales_Shift"]].groupby("SKU")["SKU_Sales_Shift"].transform(lambda x: x.expanding().mean())
    # Product_Category
    df["Product_Category_Sales_Shift"] = df[["Dates", "Product_Category", "Sales"]].groupby(["Dates", "Product_Category"])["Sales"].transform("mean")
    df["Product_Category_Sales_Shift"] = df[["SKU", "Product_Category_Sales_Shift"]].groupby(["SKU"])["Product_Category_Sales_Shift"].shift()
    df["Product_Category_Encoded"] = df[["SKU", "Product_Category_Sales_Shift"]].groupby(["SKU"])["Product_Category_Sales_Shift"].transform(lambda x: x.expanding().mean())
    # Drop sales shift columns
    df.drop(columns=["SKU_Sales_Shift", "Product_Category_Sales_Shift"], inplace=True)
    return df