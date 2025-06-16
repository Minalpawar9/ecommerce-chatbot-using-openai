import streamlit as st
from openai import OpenAI

# Load OpenAI API key from file
with open(r'C:\Users\appsl\OneDrive\Desktop\genai\Key.txt') as f:
    key = f.read().strip()

# Initialize OpenAI model
model = OpenAI(api_key=key)

# Set custom page config
st.set_page_config(page_title="Minal ShopBot", page_icon="🛍️")

# Apply custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #fdfcfc;
    }
    .stChatMessage {
        background-color: #f1f1f1;
        border-radius: 8px;
        padding: 8px;
        margin: 5px 0;
    }
    .title {
        font-size: 32px;
        color: #e91e63;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# Product list
product_list = '''
## 🛍️ Product Categories:

### 👗 Women's Clothing
- T-shirt ($20) — Sizes: S, M, L, XL | Colors: Red, White, Black
- Elegant Evening Gown ($150)
- Summer Dress, Blazer...

### 👔 Men's Clothing
- Classic Suit Set ($200), Jeans, Polo Shirts...

### 🎒 Accessories
- Sunglasses ($20), Handbags, Watches...

### 👟 Footwear
- Sneakers, Boots, Leather Shoes...

### 🧒 Kids' Collection
- Cartoon T-shirts, Onesies, Backpacks...

### 🧘 Activewear
- Yoga Leggings, Running Shoes, Sports T-shirts
'''

# ShopBot introduction
st.markdown("<div class='title'>Welcome to Minal Fashion Shop 👗</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your friendly AI assistant for shopping</div>", unsafe_allow_html=True)
st.divider()
st.markdown(product_list)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display past messages
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input
user_input = st.chat_input("How can I help you today?")

# Context for ShopBot
shopbot_context = [{
    'role': 'system',
    'content': f"""
You are ShopBot, an AI assistant for my online fashion shop - Minal.

Your role is to assist customers in browsing products, providing information, and guiding them through the checkout process.

Be friendly and helpful in your interactions.

Here’s a summary of product categories:

{product_list}

Encourage users to ask questions or explore our collections.
    """
}]

# If input received
if user_input:
    st.chat_message("user").write(user_input)

    response = model.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=shopbot_context + st.session_state["messages"] + [{"role": "user", "content": user_input}]
    )

    bot_reply = response.choices[0].message.content
    st.chat_message("assistant").write(bot_reply)

    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})
