 # Remove leading and trailing whitespaces from column names
    df.columns = df.columns.str.strip()

    # Fill missing values with forward fill method
    df.ffill(inplace=True)

    # Convert date column to datetime
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        raise KeyError("'Date' column not found in DataFrame.")

    # Unemployment rate over time for different states
    plt.figure(figsize=(14, 8))
    for state in df['Region'].unique():
        state_data = df[df['Region'] == state]
        plt.plot(state_data['Date'], state_data['Estimated Unemployment Rate (%)'], label=state)

    plt.title('Unemployment Rate Over Time by State')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    plt.xticks(rotation=45)
    plt.show()

    # Boxplot of unemployment rate by state
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)
    plt.title('Unemployment Rate by State')
    plt.xlabel('State')
    plt.ylabel('Unemployment Rate (%)')
    plt.xticks(rotation=90)
    plt.show()

    # Pairplot to explore relationships
    sns.pairplot(df[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']])
    plt.show()

    # Select a state for time series analysis
    state = 'Maharashtra'
    state_data = df[df['Region'] == state]

    # Resample data to monthly average
    state_data.set_index('Date', inplace=True)
    monthly_unemployment = state_data['Estimated Unemployment Rate (%)'].resample('M').mean()

    # Plot the resampled data
    plt.figure(figsize=(10, 6))
    monthly_unemployment.plot()
    plt.title(f'Monthly Average Unemployment Rate in {state}')
    plt.xlabel('Date')
    plt.ylabel('Unemployment Rate (%)')
    plt.show()