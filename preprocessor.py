import re
import pandas as pd


def preprocess(data):

    # Pattern to split messages
    pattern = r"\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s[ap]m\s-\s"
    messages = re.split(pattern, data)[1:]

    # Extract dates
    date_pattern = r"\d{1,2}/\d{1,2}/\d{4},\s\d{1,2}:\d{2}\s[ap]m"
    dates = re.findall(date_pattern, data)

    # Create DataFrame
    df = pd.DataFrame({
        'user_message': messages,
        'date': dates
    })

    # Convert to datetime
    df['date'] = pd.to_datetime(
        df['date'],
        format="%d/%m/%Y, %I:%M %p"
    )

    # Extract user and message
    users = []
    messages_clean = []

    for message in df['user_message']:
        entry = re.split(r'([^:]+):\s', message)

        if len(entry) > 2:
            users.append(entry[1])
            messages_clean.append(entry[2])
        else:
            users.append('group_notification')
            messages_clean.append(entry[0])

    df['user'] = users
    df['message'] = messages_clean

    # Remove system messages
    df = df[df['user'] != 'group_notification']

    # Feature Engineering
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # 24-hour period creation (for heatmap)
    period = []

    for hour in df['hour']:
        if hour == 23:
            period.append("23-00")
        elif hour == 0:
            period.append("00-1")
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    # Drop only unused column
    df.drop(columns=['user_message'], inplace=True)

    return df
