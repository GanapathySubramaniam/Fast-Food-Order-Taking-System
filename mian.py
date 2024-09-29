import asyncio
import os
import inspect
from typing import Any, List
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero


load_dotenv()

import os

os.environ['AWS_ACCESS_KEY_ID'] = 'AKIAW3MEC3ZDZKDPBQ4B'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'c04XIpXu/JgqadpvDrwctTZP4QULFTKmwlWP1aZE'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

# AWS Credentials: Ensure your AWS credentials are configured securely
import boto3

def retrieve_all_menu_items():
    dynamodb = boto3.client('dynamodb')
    
    # Scan the table to retrieve all items
    response = dynamodb.scan(TableName='menu')
    items = response.get('Items', [])
    
    # Process and return all items
    result = []
    for item in items:
        result.append({
            'id': item.get('id', {}).get('N', ''),
            'cost': item.get('cost', {}).get('N', ''),
            'ingredients': item.get('ingredients', {}).get('S', ''),
            'item': item.get('item', {}).get('S', '')
        })
    
    return str(result)

async def entrypoint(ctx: JobContext):
    try:
        menu = retrieve_all_menu_items()
        with open('system.txt', 'r') as file:
            system_prompt = file.read()
            system_prompt = system_prompt.replace("{menu}", menu)
        initial_ctx = llm.ChatContext().append(
            role="system",
            text=(
               system_prompt
            ),
        )
        await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
        assistant = VoiceAssistant(
            vad=silero.VAD.load(),
            stt=openai.STT(),
            llm=openai.LLM(),
            tts=openai.TTS(),
            chat_ctx=initial_ctx
        )
        assistant.start(ctx.room)

        await asyncio.sleep(1)
        await assistant.say("Welcome to TASTY BITE! How can I help you today?", allow_interruptions=True)

        # Keep the assistant running
        while True:
            await asyncio.sleep(1)

    except Exception as e:
        print(f"An error occurred in entrypoint: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))