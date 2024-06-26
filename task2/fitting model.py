
    # Fit the ARIMA model
    model = ARIMA(monthly_unemployment.dropna(), order=(5, 1, 0))
    model_fit = model.fit()

    # Forecast
    forecast = model_fit.forecast(steps=12)
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_unemployment, label='Historical')
    plt.plot(forecast, label='Forecast', color='red')
    plt.title(f'Unemployment Rate Forecast in {state}')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend()
    plt.show()

    # Save DataFrame to CSV
    output_file_path = r"D:\User\Downloads\Unemployment_in_India_cleaned.csv"
    df.to_csv(output_file_path, index=False)
    print(f"DataFrame successfully saved to '{output_file_path}'")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except KeyError as e:
    print(f"Error: {e}. Please check the structure of your CSV file.")
except Exception as e:
    print(f"An error occurred: {e}")