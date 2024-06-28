from sys import prefix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime, pytz
import glob, os
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import zipfile
from bing_image_downloader import downloader


# ==========================================================================================================================================

excel_type =["vnd.ms-excel","vnd.openxmlformats-officedocument.spreadsheetml.sheet", "vnd.oasis.opendocument.spreadsheet", "vnd.oasis.opendocument.text"]


def data(data, file_type, seperator=None):

    if file_type == "csv":
        data = pd.read_csv(data)

    elif file_type == "json":
        data = pd.read_json(data)
        data = (data["devices"].apply(pd.Series))
    
    elif file_type in excel_type:
        data = pd.read_excel(data)
        st.sidebar.info("If you are using Excel file so there could be chance of getting minor error(temporary sollution: avoid the error by removing overview option from input box) so bear with it. It will be fixed soon")
    
    elif file_type == "plain":
        try:
            data = pd.read_table(data, sep=seperator)
        except ValueError:
            st.info("If you haven't Type the separator then dont worry about the error this error will go as you type the separator value and hit Enter.")

    return data
# ==========================================================================================================================================

def seconddata(data, file_type, seperator=None):

    if file_type == "csv":
        data = pd.read_csv(data)

    elif file_type == "json":
        data = pd.read_json(data)
        data = (data["devices"].apply(pd.Series))
    
    elif file_type in excel_type:
        data = pd.read_excel(data)
        st.sidebar.info("If you are using Excel file so there could be chance of getting minor error(temporary sollution: avoid the error by removing overview option from input box) so bear with it. It will be fixed soon")
    
    elif file_type == "plain":
        try:
            data = pd.read_table(data, sep=seperator)
        except ValueError:
            st.info("If you haven't Type the separator then dont worry about the error this error will go as you type the separator value and hit Enter.")

    return data

# ==========================================================================================================================================

def match_elements(list_a, list_b):
    non_match = []
    for i in list_a:
        if i  in list_b:
            non_match.append(i)
    return non_match

# ==========================================================================================================================================

def download_data(data, label):
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    current_time = "{}.{}-{}-{}".format(current_time.date(), current_time.hour, current_time.minute, current_time.second)
    export_data = st.download_button(
                        label="Download {} data as CSV".format(label),
                        data=data.to_csv(),
                        file_name='{}{}.csv'.format(label, current_time),
                        mime='text/csv',
                        help = "When You Click On Download Button You can download your {} CSV File".format(label)
                    )
    return export_data
# ==========================================================================================================================================


def download_images(query, limit):
    # Download images
    downloader.download(query, limit=int(limit), output_dir='image_dataset', adult_filter_off=True, force_replace=False, timeout=60)
    
    # Create a zip file of the downloaded images
    zip_filename = f'{query}_images.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for foldername, subfolders, filenames in os.walk(f'image_dataset/{query}'):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, f'image_dataset/{query}'))
    
    return zip_filename
# ==========================================================================================================================================

def describe(data):
    global num_category, str_category
    num_category = [feature for feature in data.columns if data[feature].dtypes != "O"]
    str_category = [feature for feature in data.columns if data[feature].dtypes == "O"]
    column_with_null_values = data.columns[data.isnull().any()]
    return data.describe(), data.shape, data.columns, num_category, str_category, data.isnull().sum(),data.dtypes.astype("str"), data.nunique(), str_category, column_with_null_values


# ==========================================================================================================================================

def outliers(df, columns):
    figs = []
    for col in columns:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        ax.set_title(f'Boxplot of {col}')
        figs.append(fig)
    return figs
# ==========================================================================================================================================

def drop_items(data, selected_name):
    droped = data.drop(selected_name, axis = 1)
    return droped
# ==========================================================================================================================================


def filter_data(data, selected_column, selected_name):
    if selected_name == []:
        filtered_data = data
    else:
        filtered_data = data[~ data[selected_column].isin(selected_name)]
    return filtered_data
# ==========================================================================================================================================


def num_filter_data(data, start_value, end_value, column, param):
    if param == "Delete data inside the range":
        if column in num_category:
            num_filtered_data = data[~data[column].isin(range(int(start_value), int(end_value)+1))]
    else:
        if column in num_category:
            num_filtered_data = data[data[column].isin(range(int(start_value), int(end_value)+1))]
    
    return num_filtered_data

# ==========================================================================================================================================

def rename_columns(data, column_names):
    rename_column = data.rename(columns=column_names)
    return rename_column

# ==========================================================================================================================================

def handling_missing_values(data, option_type, dict_value=None):
    if option_type == "Drop all null value rows":
        data = data.dropna()

    elif option_type == "Only Drop Rows that contanines all null values":
        data = data.dropna(how="all")
    
    elif option_type == "Filling in Missing Values":
        data = data.fillna(dict_value)
    
    return data

# ==========================================================================================================================================

def data_wrangling(data1, data2, key, usertype):
    if usertype == "Merging On Index":
        data = pd.merge(data1, data2, on=key, suffixes=("_extra", "_extra0"))
        data = data[data.columns.drop(list(data.filter(regex='_extra')))]
        return data
    
    elif usertype == "Concatenating On Axis":
        data = pd.concat([data1, data2], ignore_index=True)
        return data

# ==========================================================================================================================================


def clear_image_cache():
    removing_files = glob.glob('temp/*.png')
    for i in removing_files:
        os.remove(i)
# ==========================================================================================================================================

def plot_3d_scatter(df, x, y, z):
    fig = px.scatter_3d(df, x=x, y=y, z=z)
    return fig
# ==========================================================================================================================================

def plot_3d_bar(df, x, y, z):
    fig = px.bar_3d(df, x=x, y=y, z=z)
    return fig
# ==========================================================================================================================================

def plot_3d_line(df, x, y, z):
    fig = px.line_3d(df, x=x, y=y, z=z)
    return fig
# ==========================================================================================================================================

def plot_3d_area(df, x, y, z):
    fig = go.Figure(data=go.Scatter3d(x=df[x], y=df[y], z=df[z], mode='lines', surfaceaxis=2))
    return fig
# ==========================================================================================================================================

def plot_3d_pie(df, x, y, z):
    fig = go.Figure(data=[go.Pie(labels=df[x], values=df[y], textinfo='label+percent', hole=.3)])
    return fig
# ==========================================================================================================================================

def plot_3d_bubble(df, x, y, z):
    fig = go.Figure(data=[go.Scatter3d(
        x=df[x], y=df[y], z=df[z],
        mode='markers',
        marker=dict(size=df[z], sizemode='diameter')
    )])
    return fig
# ==========================================================================================================================================

def plot_3d_treemap(df, x, y, z):
    fig = px.treemap(df, path=[x, y], values=z)
    return fig
# ==========================================================================================================================================

def plot_3d_heatmap(df, x, y, z):
    fig = go.Figure(data=go.Heatmap(
        x=df[x],
        y=df[y],
        z=df[z]
    ))
    return fig
# ==========================================================================================================================================

# Additional visualization functions
def plot_3d_surface(df, x, y, z):
    fig = go.Figure(data=[go.Surface(z=df.pivot(index=y, columns=x, values=z).values)])
    return fig
# ==========================================================================================================================================

def plot_3d_contour(df, x, y, z):
    fig = go.Figure(data=[go.Contour(z=df.pivot(index=y, columns=x, values=z).values)])
    return fig

# ==========================================================================================================================================

# Save Plot as Image Function
def save_plot_as_image(fig, filename):
    pio.write_image(fig, filename)

# ==========================================================================================================================================

