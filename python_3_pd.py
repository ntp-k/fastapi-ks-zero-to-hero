import pandas as pd
from IPython.display import display

def read_csv(file_path):
    return pd.read_csv(file_path, index_col=False)

def summary_sale_per_product(df):
    df['total'] = df["amount"] * df["unitPrice"]
    summary_df = df.groupby('productId', as_index=False).agg(
                                                        totalAmount=('amount', 'sum'),
                                                        grandTotal=('total', 'sum')
                                                    )
    return summary_df

def get_row_max_sale_amount(df):
    df = summary_sale_per_product(df=df)
    return df[df.totalAmount == df.totalAmount.max()]

def get_row_max_grand_total(df):
    df = summary_sale_per_product(df=df)
    return df[df.grandTotal == df.grandTotal.max()]

if __name__ == "__main__":
    df = read_csv('sales.csv')
    # df = summary_sale_per_product(df=df)
    # df = get_row_max_sale_amount(df=df)
    df = get_row_max_grand_total(df=df)

    display(df)

    # 