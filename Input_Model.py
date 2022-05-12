import streamlit as st
import pandas as pd
import numpy as np


st.write("""
# Heart Abnormality Checking  App
This app predicts the **Report Status** for the ECG Report!""")

st.sidebar.header('User Input Features')
date = st.sidebar.date_input('Date')
gender = st.sidebar.selectbox('Gender', ('Male', 'Female'))
agegroup = st.sidebar.radio(
    'AgeGroup', ('Children', 'Adult', 'Old'))
status = st.sidebar.selectbox(
    'DataStatus (Select Invalid Data if any value is missing) ', ('Valid Data', 'Invalid Data'))
heartrate = st.sidebar.slider('HeartRate(bpm)', 0, 200, 75)
rr_ms = st.sidebar.slider(
    'RR(ms)', 0, 1500, 900)
pr_ms = st.sidebar.slider('PR(ms)', 0, 500, 160)
qrs_ms = st.sidebar.slider('QRS(ms)', 0, 500, 90)
qt_ms = st.sidebar.slider('QT(ms)', 0, 500, 370)
qtc_ms = st.sidebar.slider('QTc(ms)', 0, 500, 400)
data = {'Gender': gender,
        'Date': date,
        'AgeGroup': agegroup,
        'DataStatus': status,
        'HeartRate(bpm)': heartrate,
        'RR(ms)': rr_ms,
        'PR(ms)': pr_ms,
        'QRS(ms)': qrs_ms,
        'QT(ms)': qt_ms,
        'QTc(ms)': qtc_ms}
features = pd.DataFrame(data, index=[0])

st.subheader('User Input parameters')
st.table(features)
st.subheader('Results')
intervals = []
difference = []
name = []
if (gender == "Male"):
    if(agegroup == "Children"):
        if heartrate <= 70 or heartrate >= 110:
            intervals.append("HeartRate")
            difference.append(85-int(heartrate))
            name.append(heartrate)
        if rr_ms <= 600 or rr_ms >= 1200:
            intervals.append("RR(ms)")
            difference.append(900-int(rr_ms))
            name.append(rr_ms)
        if pr_ms <= 120 or pr_ms >= 200:
            intervals.append("PR(ms)")
            difference.append(160-int(pr_ms))
            name.append(pr_ms)
        if qrs_ms <= 70 or qrs_ms >= 110:
            intervals.append("QRS(ms)")
            difference.append(90-int(qrs_ms))
            name.append(qrs_ms)
        if qt_ms <= 320 or qt_ms >= 410:
            intervals.append("QT(ms)")
            difference.append(365-int(qt_ms))
            name.append(qt_ms)
        if qtc_ms <= 330 or qtc_ms >= 445:
            intervals.append("QTc(ms)")
            difference.append(388-int(qtc_ms))
            name.append(qtc_ms)

    elif(agegroup == "Adult"):
        if heartrate <= 60 or heartrate >= 120:
            intervals.append("HeartRate")
            difference.append(90-int(heartrate))
            name.append(heartrate)
        if rr_ms <= 600 or rr_ms >= 1200:
            intervals.append("RR(ms)")
            difference.append(900-int(rr_ms))
            name.append(rr_ms)
        if pr_ms <= 119 or pr_ms >= 210:
            intervals.append("PR(ms)")
            difference.append(165-int(pr_ms))
            name.append(pr_ms)
        if qrs_ms <= 74 or qrs_ms >= 110:
            intervals.append("QRS(ms)")
            difference.append(92-int(qrs_ms))
            name.append(qrs_ms)
        if qt_ms <= 324 or qt_ms >= 441:
            intervals.append("QT(ms)")
            difference.append(383-int(qt_ms))
            name.append(qt_ms)
        if qtc_ms <= 350 or qtc_ms >= 450:
            intervals.append("QTc(ms)")
            difference.append(400-int(qtc_ms))
            name.append(qtc_ms)

    else:
        if heartrate <= 60 or heartrate >= 100:
            intervals.append("HeartRate")
            difference.append(80-int(heartrate))
            name.append(heartrate)
        if rr_ms <= 600 or rr_ms >= 1200:
            intervals.append("RR(ms)")
            difference.append(900-int(rr_ms))
            name.append(rr_ms)
        if pr_ms <= 119 or pr_ms >= 210:
            intervals.append("PR(ms)")
            difference.append(165-int(pr_ms))
            name.append(pr_ms)
        if qrs_ms <= 74 or qrs_ms >= 110:
            intervals.append("QRS(ms)")
            difference.append(92-int(qrs_ms))
            name.append(qrs_ms)
        if qt_ms <= 324 or qt_ms >= 441:
            intervals.append("QT(ms)")
            difference.append(383-int(qt_ms))
            name.append(qt_ms)
        if qtc_ms <= 350 or qtc_ms >= 450:
            intervals.append("QTc(ms)")
            difference.append(400-int(qtc_ms))
            name.append(qtc_ms)
else:
    if(agegroup == "Children"):
        if heartrate <= 70 or heartrate >= 110:
            intervals.append("HeartRate")
            difference.append(85-int(heartrate))
            name.append(heartrate)
        if rr_ms <= 600 or rr_ms >= 1200:
            intervals.append("RR(ms)")
            difference.append(900-int(rr_ms))
            name.append(rr_ms)
        if pr_ms <= 120 or pr_ms >= 200:
            intervals.append("PR(ms)")
            difference.append(160-int(pr_ms))
            name.append(pr_ms)
        if qrs_ms <= 70 or qrs_ms >= 110:
            intervals.append("QRS(ms)")
            difference.append(90-int(qrs_ms))
            name.append(qrs_ms)
        if qt_ms <= 320 or qt_ms >= 410:
            intervals.append("QT(ms)")
            difference.append(365-int(qt_ms))
            name.append(qt_ms)
        if qtc_ms <= 330 or qtc_ms >= 445:
            intervals.append("QTc(ms)")
            difference.append(388-int(qtc_ms))
            name.append(qtc_ms)

    elif(agegroup == "Adult"):
        if heartrate <= 60 or heartrate >= 120:
            intervals.append("HeartRate")
            difference.append(80-int(heartrate))
            name.append(heartrate)
        if rr_ms <= 600 or rr_ms >= 1200:
            intervals.append("RR(ms)")
            difference.append(900-int(rr_ms))
            name.append(rr_ms)
        if pr_ms <= 120 or pr_ms >= 202:
            intervals.append("PR(ms)")
            difference.append(161-int(pr_ms))
            name.append(pr_ms)
        if qrs_ms <= 70 or qrs_ms >= 104:
            intervals.append("QRS(ms)")
            difference.append(87-int(qrs_ms))
            name.append(qrs_ms)
        if qt_ms <= 314 or qt_ms >= 438:
            intervals.append("QT(ms)")
            difference.append(376-int(qt_ms))
            name.append(qt_ms)
        if qtc_ms <= 360 or qtc_ms >= 460:
            intervals.append("QTc(ms)")
            difference.append(410-int(qtc_ms))
            name.append(qtc_ms)

    else:
        if heartrate <= 60 or heartrate >= 100:
            intervals.append("HeartRate")
            difference.append(80-int(heartrate))
            name.append(heartrate)
        if rr_ms <= 600 or rr_ms >= 1200:
            intervals.append("RR(ms)")
            difference.append(900-int(rr_ms))
            name.append(rr_ms)
        if pr_ms <= 120 or pr_ms >= 202:
            intervals.append("PR(ms)")
            name.append(pr_ms)
            difference.append(161-int(pr_ms))
        if qrs_ms <= 70 or qrs_ms >= 104:
            intervals.append("QRS(ms)")
            difference.append(87-int(qrs_ms))
            name.append(qrs_ms)
        if qt_ms <= 314 or qt_ms >= 438:
            intervals.append("QT(ms)")
            difference.append(376-int(qt_ms))
            name.append(qt_ms)
        if qtc_ms <= 360 or qtc_ms >= 460:
            intervals.append("QTc(ms)")
            difference.append(410-int(qtc_ms))
            name.append(qtc_ms)


healthy_result = "Kuddos!! Your ECG Report is Normal."
negative_result = "All of the following interval/intervals are out of the normal ranges for a healthy person:-"
if st.button("Get Results"):
    if (status == "Valid Data"):
        if len(intervals) >= 1:
            st.write(negative_result)
            cols = st.columns(6)
            for i in range(len(intervals)):
                cols[i].metric(
                    intervals[i], name[i], difference[i])
            col0, col1, col2, col3, col4, col5 = st.columns(6)
        else:
            st.write(healthy_result)
    else:
        st.write("The data entered is invalid. Please check the ECG Report!")
st.markdown("---")
st.write("""To view a diagram representing the **ECG intervals** click the button below.""")
if st.button("ECG Graph"):
    st.image("https://litfl.com/wp-content/uploads/2018/10/ECG-waves-segments-and-intervals-LITFL-ECG-library-3.jpg",
             caption="A Graph that shows how the intervals are read.")
