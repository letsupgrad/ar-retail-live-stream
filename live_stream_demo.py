import streamlit as st
from PIL import Image

# Streamlit page configuration
st.set_page_config(page_title="Eco-Friendly Outdoor Displays", page_icon="🌱", layout="wide")

# Title and description of the app
st.title("Eco-Friendly, Sustainable Outdoor Displays")
st.header("Eco-Friendly Outdoor Branding and Display Concepts")
st.subheader("Highlighting sustainable materials and green initiatives")

# Section 1: Introduction to Eco-Friendly Branding
st.write("""
    **Eco-Friendly Outdoor Displays** are a powerful way to showcase sustainable practices while enhancing your brand's environmental responsibility. 
    Imagine outdoor billboards made from recycled wood or biodegradable materials, complemented by green features like live plant walls or vertical gardens.
    These displays attract eco-conscious consumers and improve your brand's perception.
""")

# Add a slider to choose display type: Wood, Biodegradable, or Vertical Garden
st.write("### Select Type of Eco-Friendly Display:")
display_type = st.selectbox("Choose your display material:", ["Recycled Wood", "Biodegradable Components", "Vertical Garden"])

# Section 2: Visualize the Concept (with Image of Selected Display Type)
if display_type == "Recycled Wood":
    st.image("recycled_wood_display.jpg", caption="Eco-Friendly Outdoor Billboard with Recycled Wood", use_container_width=True)
elif display_type == "Biodegradable Components":
    st.image("biodegradable_display.jpg", caption="Outdoor Billboard with Biodegradable Materials", use_container_width=True)
else:
    st.image("vertical_garden_display.jpg", caption="Outdoor Billboard with Vertical Garden", use_container_width=True)

# Section 3: Interactive Elements (Describe Materials and Benefits)
st.write("### Materials Used in Selected Display:")
if display_type == "Recycled Wood":
    st.markdown("""
    - **Recycled Wood**: Repurposed wood from old furniture, construction, or other sources.
    - **Durable & Long-Lasting**: Ideal for outdoor displays that need to withstand weathering.
    - **Low Environmental Impact**: Reduces the need for new timber and minimizes waste.
    """)
elif display_type == "Biodegradable Components":
    st.markdown("""
    - **Biodegradable Components**: Materials that decompose naturally, reducing landfill waste.
    - **Non-Toxic**: Safe for the environment and wildlife.
    - **Eco-Conscious Messaging**: Perfect for brands that want to show a commitment to sustainability.
    """)
else:
    st.markdown("""
    - **Vertical Garden**: A living wall made with plants and flowers that help improve air quality.
    - **Solar-Powered**: Powered by renewable energy to reduce carbon footprint.
    - **Aesthetic Appeal**: Adds beauty to the environment while contributing to sustainability.
    """)

# Section 4: Benefits of Eco-Friendly Branding
st.write("### Benefits of Eco-Friendly Outdoor Displays:")
st.markdown("""
- **Appeals to Eco-Conscious Consumers**: More and more people prefer brands that are committed to sustainability.
- **Improves Brand Perception**: Demonstrating a commitment to the environment can enhance a brand's image.
- **Supports Green Initiatives**: Outdoor displays with plants or solar power contribute to environmental conservation.
- **Stand Out in a Crowded Market**: Unique, eco-friendly designs catch the eye of passersby and stand out from traditional advertising.
""")

# Section 5: Interactive Slider to Visualize Plant Growth in Display
st.write("### How a Vertical Garden Can Grow Over Time:")
growth_time = st.slider("Select time for plant growth (months)", 1, 12, 6)
st.write(f"Growth stage: {growth_time} months")

# Simulate plant growth stages with images (replace with your own images)
if growth_time <= 3:
    st.image("plant_stage_1.jpg", caption="Early Growth Stage", use_container_width=True)
elif 4 <= growth_time <= 6:
    st.image("plant_stage_2.jpg", caption="Mid Growth Stage", use_container_width=True)
else:
    st.image("plant_stage_3.jpg", caption="Full Growth Stage", use_container_width=True)

# Section 6: Call to Action (CTA) for Eco-Conscious Consumers
st.markdown("""
    **Ready to Go Green?** 🌱
    Embrace eco-friendly branding by incorporating sustainable outdoor displays in your marketing strategy. 
    By using recycled materials and integrating plant life into your displays, you can engage with an environmentally conscious audience and make a positive impact.
""")
cta_button = st.button("Learn More About Sustainable Branding")
if cta_button:
    st.write("Thank you for your interest in sustainable branding! Please visit our website for more details.")

# Footer
st.markdown("---")
st.markdown("For more details, visit our website or follow us on social media.")

