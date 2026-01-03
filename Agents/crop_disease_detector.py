import google.generativeai as genai
from dotenv import load_dotenv
import os
from PIL import Image # <--- 1. IMPORT PILLOW LIBRARY

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Load Gemini Vision model
model = genai.GenerativeModel("gemini-2.5-flash")

# Analyze crop image
# In crop_disease_detector.py

from PIL import Image
import traceback # Import the traceback library

# ... (your other imports and config are fine) ...

def analyze_crop_image(uploaded_file):
    print("\n--- [AGENT START] ---")
    print("--- 1. Entered the analyze_crop_image function. ---")
    try:
        if uploaded_file is None:
            print("--- X. ERROR: No file provided. ---")
            return "❌ Error: No image file was provided."

        print(f"--- 2. Received file: {uploaded_file.name}, Size: {uploaded_file.size} bytes ---")

        print("--- 3. Attempting to open the image with PIL... ---")
        image = Image.open(uploaded_file)
        print("--- 4. Image opened successfully by PIL. ---")

        prompt = """
        This is a crop leaf image taken by a farmer.
        Please analyze if there are any visible signs of plant disease or pest.
        If yes:
        - Name the crop disease (if possible).
        - Mention symptoms seen in the image.
        - Suggest treatment or preventive remedy.
        - Mention whether it's serious or mild.
        - Mention if it can be treated at home or requires professional help.
        - Help the farmer understand the issue clearly.
        - Provide a friendly and informative response.
        If the image is not clear or no disease is detected, say please provide a clearer image.
        If no disease is detected, say it's healthy.
        explain in hindi and english both.
        """
        
        print("--- 5. Prompt is ready. Sending request to Gemini model... ---")
        response = model.generate_content([prompt, image])
        print("--- 6. Received a successful response from Gemini. ---")
        
        return response.text

    except Exception as e:
        # This will print the full, detailed error to your terminal
        print("\n--- XXX. AN EXCEPTION OCCURRED XXX ---")
        traceback.print_exc()
        print("--- XXX. END OF EXCEPTION ---")
        return f"❌ An error occurred inside the agent: {e}"



# Run the agent
if __name__ == "__main__":
    print("🌿 Crop Disease Detection Agent")
    image_path = input("Enter the path of image : ").strip().strip('"')


    result = analyze_crop_image(image_path)
    print("\n📋 Diagnosis Result:\n")
    print(result)
