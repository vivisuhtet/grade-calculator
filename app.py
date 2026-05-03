import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Grade Calculator", page_icon="🎓")
st.title("🎓 Student Grade Calculator")
st.markdown("Calculate your GPA and visualise your performance!")

grade_map = {'A+': 4.0, 'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
             'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D': 1.0, 'F': 0.0}

st.subheader("Enter Your Modules")
num = st.number_input("How many modules?", min_value=1, max_value=10, value=4)

modules, grades, credits = [], [], []
for i in range(num):
    col1, col2, col3 = st.columns(3)
    with col1: m = st.text_input(f"Module {i+1}", value=f"Module {i+1}", key=f"m{i}")
    with col2: g = st.selectbox(f"Grade", list(grade_map.keys()), key=f"g{i}")
    with col3: c = st.number_input(f"Credits", min_value=1, max_value=6, value=3, key=f"c{i}")
    modules.append(m); grades.append(g); credits.append(c)

if st.button("Calculate GPA"):
    points = [grade_map[g] * c for g, c in zip(grades, credits)]
    gpa = sum(points) / sum(credits)
    st.success(f"Your GPA is: **{gpa:.2f}**")
    if gpa >= 3.7: st.info("🏆 First Class Honours!")
    elif gpa >= 3.3: st.info("🥈 Upper Second Class!")
    elif gpa >= 2.7: st.info("🥉 Lower Second Class!")
    else: st.info("📚 Keep working hard!")

    df = pd.DataFrame({'Module': modules, 'Grade': grades, 'Credits': credits,
                       'Points': [grade_map[g] for g in grades]})
    fig, ax = plt.subplots()
    ax.bar(df['Module'], df['Points'], color='teal')
    ax.set_ylabel('Grade Points')
    ax.set_title('Grade Points by Module')
    plt.xticks(rotation=45)
    st.pyplot(fig)
