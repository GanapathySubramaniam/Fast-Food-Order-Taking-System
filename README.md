
---

# 🛠️ Fast Food Order-Taking System 🍔
```

__________             _____     __________           _________   _______       _________                  ________      ______ _____                    ________              _____                 
___  ____/_____ _________  /_    ___  ____/_________________  /   __  __ \____________  /____________      ___  __/_____ ___  /____(_)_____________ _    __  ___/____  __________  /____________ ___ 
__  /_   _  __ `/_  ___/  __/    __  /_   _  __ \  __ \  __  /    _  / / /_  ___/  __  /_  _ \_  ___/________  /  _  __ `/_  //_/_  /__  __ \_  __ `/    _____ \__  / / /_  ___/  __/  _ \_  __ `__ \
_  __/   / /_/ /_(__  )/ /_      _  __/   / /_/ / /_/ / /_/ /     / /_/ /_  /   / /_/ / /  __/  /   _/_____/  /   / /_/ /_  ,<  _  / _  / / /  /_/ /     ____/ /_  /_/ /_(__  )/ /_ /  __/  / / / / /
/_/      \__,_/ /____/ \__/      /_/      \____/\____/\__,_/      \____/ /_/    \__,_/  \___//_/           /_/    \__,_/ /_/|_| /_/  /_/ /_/_\__, /      /____/ _\__, / /____/ \__/ \___//_/ /_/ /_/ 
                                                                                                                                            /____/              /____/                               

```

This project is an AI-based fast food order-taking system designed to handle customer interactions in a friendly and efficient manner. Built using **LiveKit Agents** and **OpenAI's language models**, it provides a conversational interface where users can place orders, inquire about menu items, and customize their selections. The AI is designed to maintain a natural, human-like tone while assisting customers through the entire order process.

## Features 🎯

- **Friendly AI Interaction:** The AI greets customers, takes orders, and suggests complementary items.
- **Menu Integration:** Retrieves and dynamically updates menu items from a database.
- **Customization Options:** Supports order modifications and customization for dietary preferences.
- **Order Management:** Confirms and repeats orders, ensuring accuracy.
- **Payment Handling:** Offers payment options to the user (cash/card).
- **Voice Assistant Support:** Incorporates voice-activated assistance for hands-free order placement.

## Setup and Installation 🛠️

### Prerequisites
Before running the project, make sure you have the following installed:
- Python 3.x
- AWS credentials set up for DynamoDB integration
- **[OpenAI API Key](https://beta.openai.com/signup/)** for using language models

### Required Python Packages
Install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

> Dependencies are listed in the `requirements.txt`:
> - `livekit-agents>=0.8.7`
> - `livekit-plugins-openai>=0.8.1`
> - `livekit-plugins-silero>=0.6.4`
> - `python-dotenv~=1.0`

### Environment Setup
You must create a `.env` file to store your AWS credentials securely:

```env
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_KEY
AWS_DEFAULT_REGION=YOUR_AWS_REGION
```

### Running the Application 🚀

1. Ensure you have the correct AWS credentials to connect to DynamoDB.
2. The system retrieves menu items from a DynamoDB table called **menu**. Ensure that the table is set up with items and prices.
3. Run the Python file using the command:

```bash
python app.py
```

This will start the voice assistant, ready to take orders and interact with customers!

## System Architecture 🏗️

The AI system is structured around the **LiveKit** framework, integrating **OpenAI's** language model for natural language understanding and generation, and **Silero** for voice activity detection and speech-to-text functionality. Here's a breakdown of the core components:

- **VoiceAssistant:** Handles user interaction with speech and text.
- **Boto3 (AWS SDK):** Used to connect to AWS DynamoDB to fetch menu data.
- **LLM Integration:** The system uses OpenAI's LLM for generating human-like responses during customer interactions.
  
### Files Overview

- `app.py`: The main entry point, responsible for fetching menu items from DynamoDB and running the voice assistant logic.
- `system.txt`: Contains system-level instructions guiding the AI's behavior and customer interaction guidelines.
- `requirements.txt`: Specifies the dependencies needed to run the application.

## Demo 🎥

<video src="[v1.mp4](https://github.com/GanapathySubramaniam/restaurant-kiosk/blob/main/v1.mp4)"></video>
https://github.com/GanapathySubramaniam/restaurant-kiosk/blob/main/v1.mp4
  
## Customizing the System ⚙️

- **Menu Customization:** Modify the **DynamoDB** entries to update menu items, prices, and descriptions.
- **Assistant Behavior:** Update the `system.txt` file to change how the AI interacts with customers (greetings, order processing, etc.).
- **Voice Settings:** You can customize voice settings or switch text-to-speech and speech-to-text models by modifying the assistant initialization in `app.py`.

