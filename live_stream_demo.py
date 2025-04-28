import streamlit as st
import cv2
import time

# Streamlit page configuration
st.set_page_config(page_title="Live Product Demo", page_icon="📦", layout="wide")

# Title and header for the demo
st.title("Live-Streamed Events & Product Demos")
st.header("Live Streaming: Live Demo of Product XYZ")
st.subheader("Watch our latest product demo live!")

# Video path (Replace with your own video file path or URL)
video_path = "path_to_your_video.mp4"  # Example: "product_demo.mp4"

# Function to stream video from a file using OpenCV
def stream_video(video_path):
    # Create a placeholder for the video
    frame_window = st.image([], use_container_width=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if video was opened successfully
    if not cap.isOpened():
        st.error("Error: Could not access the video file")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video")
            break

        # Convert the frame from BGR to RGB (OpenCV uses BGR)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame
        frame_window.image(frame_rgb)

        # Add a small delay to simulate real-time streaming
        time.sleep(0.1)

    cap.release()

# Start streaming the video
stream_video(video_path)

# Footer with additional information
st.markdown("---")
st.markdown("For more details about our events, visit our website or follow us on social media.")
