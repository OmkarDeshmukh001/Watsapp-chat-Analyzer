import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="WhatsApp Chat Analyzer", layout="wide")

st.title("📊 WhatsApp Chat Analyzer")

st.sidebar.title("📂 Upload Chat File")

uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:

    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")

    df = preprocessor.preprocess(data)

    # Fetch users
    user_list = df['user'].unique().tolist()

    if 'group_notification' in user_list:
        user_list.remove('group_notification')

    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):

        # ======================
        # Chat Statistics
        # ======================
        st.header("📈 Chat Statistics")

        num_messages, words, num_media_messages, num_links = helper.fetch_stats(
            selected_user, df)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Messages", num_messages)

        with col2:
            st.metric("Total Words", words)

        with col3:
            st.metric("Media Shared", num_media_messages)

        with col4:
            st.metric("Links Shared", num_links)

        st.divider()

        # ======================
        # Most Busy Users
        # ======================
        if selected_user == 'Overall':

            st.subheader("👥 Most Busy Users")

            x, new_df = helper.most_busy_users(df)

            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots()
                ax.bar(x.index, x.values, color="#4CAF50")
                plt.xticks(rotation=45)
                ax.set_ylabel("Messages")
                ax.grid(alpha=0.3)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # ======================
        # Wordcloud
        # ======================
        st.subheader("☁️ Wordcloud")

        df_wc = helper.create_wordcloud(selected_user, df)

        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        ax.axis("off")

        st.pyplot(fig)

        # ======================
        # Most Common Words
        # ======================
        st.subheader("🔤 Most Common Words")

        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots()
        ax.bar(most_common_df['Word'],
               most_common_df['Frequency'], color="#FF6B6B")

        plt.xticks(rotation=45)
        ax.grid(alpha=0.3)

        st.pyplot(fig)

        # ======================
        # Emoji Analysis
        # ======================
        st.subheader("😀 Emoji Analysis")

        emoji_df = helper.emoji_helper(selected_user, df)

        st.dataframe(emoji_df)

        # ======================
        # Timelines
        # ======================
        st.subheader("📊 Chat Timelines")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📅 Monthly Timeline")

            timeline = helper.monthly_timeline(selected_user, df)

            fig, ax = plt.subplots()

            ax.plot(timeline['time'], timeline['message'],
                    marker='o', color="#4CAF50")

            plt.xticks(rotation=45)

            ax.set_xlabel("Time")
            ax.set_ylabel("Messages")

            ax.grid(alpha=0.3)

            st.pyplot(fig)

        with col2:
            st.subheader("📆 Daily Timeline")

            daily_timeline = helper.daily_timeline(selected_user, df)

            fig, ax = plt.subplots()

            ax.plot(daily_timeline['day'], daily_timeline['message'],
                    marker='o', color="#FF6B6B")

            ax.grid(alpha=0.3)

            st.pyplot(fig)

        # ======================
        # Most Active Time
        # ======================
        st.subheader("🔥 Most Active Time")

        col1, col2 = st.columns(2)

        with col1:

            month_counts = helper.most_busy_month(selected_user, df)

            fig, ax = plt.subplots()

            ax.bar(month_counts.index, month_counts.values, color="#4CAF50")

            plt.xticks(rotation=45)

            ax.set_xlabel("Month")
            ax.set_ylabel("Messages")

            ax.grid(alpha=0.3)

            st.pyplot(fig)

        with col2:

            day_counts = helper.most_busy_day(selected_user, df)

            fig, ax = plt.subplots()

            ax.bar(day_counts.index, day_counts.values, color="#FF6B6B")

            plt.xticks(rotation=45)

            ax.set_xlabel("Day")
            ax.set_ylabel("Messages")

            ax.grid(alpha=0.3)

            st.pyplot(fig)

        # ======================
        # Heatmap
        # ======================
        st.subheader("🔥 Weekly Activity Heatmap (24 Hours)")

        user_heatmap = helper.activity_heatmap(selected_user, df)

        fig, ax = plt.subplots(figsize=(12, 6))

        sns.heatmap(user_heatmap, cmap="YlOrRd", ax=ax)

        ax.set_xlabel("Hour of Day")
        ax.set_ylabel("Day of Week")

        st.pyplot(fig)
