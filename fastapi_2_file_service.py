from io import BytesIO
import pandas as pd
from fastapi.responses import FileResponse

def read_file(file):
    contents = file.file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
    buffer.close()
    file.file.close()
    return df.to_dict(orient='records')

def csv_to_df(file):
    contents = file.file.read()
    buffer = BytesIO(contents)
    df = pd.read_csv(buffer)
    buffer.close()
    file.file.close()
    return df

def summarize_sale(file):
    df = csv_to_df(file)
    df['total'] = df["amount"] * df["unitPrice"]
    summary_df = df.groupby('productId', as_index=False).agg(
                                                        totalAmount=('amount', 'sum'),
                                                        grandTotal=('total', 'sum')
                                                    )
    return summary_df.to_dict(orient='records')

def summarize_sale_to_csv(file):
    df = csv_to_df(file)
    df['total'] = df["amount"] * df["unitPrice"]
    summary_df = df.groupby('productId', as_index=False).agg(
                                                        totalAmount=('amount', 'sum'),
                                                        grandTotal=('total', 'sum')
                                                    )
    filename = 'summary.csv'
    summary_df.to_csv(filename)
    return FileResponse(filename)

# EOF
