import asyncio

from src.handle_audio import get_transcript_async

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_transcript_async("audio_response.wav"))
