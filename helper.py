from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

extract = URLExtract()


# 1️⃣ Fetch stats of the user
def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]

    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


# 2️⃣ Fetch most busy users
def most_busy_users(df):

    x = df['user'].value_counts().head()

    percent_df = (
        (df['user'].value_counts() / df.shape[0]) * 100
    ).round(2).reset_index()

    percent_df.columns = ['user', 'percent']

    return x, percent_df


# 3️⃣ Create wordcloud
def create_wordcloud(selected_user, df):

    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    wc = WordCloud(
        width=600,
        height=600,
        min_font_size=10,
        background_color='white',
        colormap='viridis'
    )

    df_wc = wc.generate(" ".join(words))

    return df_wc


# 4️⃣ Most common words
def most_common_words(selected_user, df):

    with open('stop_hinglish.txt', 'r') as f:
        stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(
        Counter(words).most_common(15),
        columns=['Word', 'Frequency']
    )

    return most_common_df


# 5️⃣ Emoji Analysis
def emoji_helper(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []

    for message in df['message']:
        emojis.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(len(Counter(emojis))),
        columns=['Emoji', 'Count']
    )

    return emoji_df


# 6️⃣ Monthly timeline
def monthly_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(
        ['year', 'month_num', 'month']
    ).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(
            timeline['month'][i] + "-" + str(timeline['year'][i])
        )

    timeline['time'] = time

    return timeline


# 7️⃣ Daily timeline (corrected)
def daily_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('day').count()['message'].reset_index()

    return daily_timeline


# 8️⃣ Most Busy Month Graph
def most_busy_month(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()


# 9️⃣ Most Busy Day Graph
def most_busy_day(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()


# 🔟 Activity Heatmap (24 hour chat activity)
def activity_heatmap(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    heatmap = df.pivot_table(
        index='day_name',
        columns='period',
        values='message',
        aggfunc='count'
    ).fillna(0)

    # Proper weekday order
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    heatmap = heatmap.reindex(days)

    return heatmap
