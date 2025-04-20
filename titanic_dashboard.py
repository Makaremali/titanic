import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")

# Plot 1: Age Histogram
fig1, ax1 = plt.subplots()
sns.histplot(df['age'], kde=True, ax=ax1)
ax1.set_title("Age Distribution")

# Plot 2: Survival by Sex
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='sex', hue='survived', ax=ax2)
ax2.set_title("Survival by Sex")

# Plot 3: Fare by Class
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='class', y='fare', ax=ax3)
ax3.set_title("Fare by Class")

# Plot 4: Correlation Heatmap
fig4, ax4 = plt.subplots()
sns.heatmap(df[['age', 'fare', 'survived']].corr(), annot=True, cmap='coolwarm', ax=ax4)
ax4.set_title("Correlation Matrix")

# Layout in two rows
st.title("Titanic Patient Dashboard")

col1, col2 = st.columns(2)
with col1: st.pyplot(fig1)
with col2: st.pyplot(fig2)

col3, col4 = st.columns(2)
with col3: st.pyplot(fig3)
with col4: st.pyplot(fig4)
