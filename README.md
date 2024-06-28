# DataPulse Image Export Web Application

![DataPulse Banner](https://via.placeholder.com/800x200.png?text=DataPulse+Image+Export+Web+Application)

## 🚀 Overview

Welcome to **DataPulse Image Export Web Application**! This application allows you to analyze and visualize data like never before. With a user-friendly interface and powerful data processing capabilities, you can easily explore insights from various data sources and export images for your dataset.

## 🎨 Features

- **Data Overview**: Get a comprehensive summary of your dataset, including basic information, column types, and missing values.
- **Outlier Detection**: Identify and visualize outliers in your numerical data.
- **Data Cleaning**: Drop unnecessary columns, filter rows, handle missing values, and rename columns with ease.
- **3D Visualizations**: Create stunning 3D scatter plots, bar charts, line graphs, and more.
- **Data Wrangling**: Merge and concatenate datasets effortlessly.
- **Image Dataset Downloader**: Download images related to your dataset queries.

## 🛠️ Installation

To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AdityaJoshi187-ADITORIUM/DataPulse-Image-Export-Web-Application.git
    cd DataPulse-Image-Export-Web-Application
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## 📋 How to Use

### Upload Your Data

1. Upload your file in formats like CSV, TXT, XLS, XLSX, ODS, or ODT.
2. If your file is in plain text format, specify the separator used in your data.

### Data Analysis and Visualization

1. **Overview**: Get a preview and summary of your dataset.
2. **Outliers**: Select numerical columns to detect and visualize outliers.
3. **Drop Columns/Rows**: Drop unnecessary columns or filter rows based on categorical or numerical values.
4. **Rename Columns**: Rename columns as needed.
5. **Handling Missing Data**: Choose to drop or fill missing values.
6. **Data Wrangling**: Merge or concatenate datasets.
7. **3D Visualizations**: Select plot type and axes to create 3D visualizations.

### Download Images

1. Enter a query related to your dataset.
2. Specify the number of images to download.
3. Download the images in a zipped file.

## 📂 File Structure
├── app.py # Main application file


├── helper.py # Helper functions for data processing and visualization

├── requirements.txt # Dependencies required to run the application

└── README.md # Project documentation

### License

  This project is licensed under the MIT License.
