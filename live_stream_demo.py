import streamlit as st
import cv2
import time

# Title of the app
st.title("Live-Streamed Events & Product Demos")

# Sidebar for controls
st.sidebar.header("Stream Controls")
event_description = st.sidebar.text_area("Event Description", "Live Demo of Product XYZ")
stream_status = st.sidebar.radio("Stream Status", ("Not Started", "Streaming"))

# Video capture setup (can be from webcam or external camera)
cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path

# Function to display video stream
def stream_video():
    frame_window = st.image([], use_column_width=True)  # Create placeholder for live video feed

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video")
            break

        # Display the frame (OpenCV to Streamlit conversion)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

        time.sleep(0.1)  # To simulate stream delay (adjust as needed)

# Product Demo Streaming
if stream_status == "Streaming":
    st.header("Live Streaming: " + event_description)
    st.subheader("Watch our latest product demo live!")
    stream_video()

else:
    st.info("Press 'Streaming' on the sidebar to start broadcasting!")

# Footer
st.markdown("---")
st.markdown("For more details about our events, visit our website or follow us on social media.")
