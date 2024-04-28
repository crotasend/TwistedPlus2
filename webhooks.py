import asyncio
import discord
from discord import Webhook
import aiohttp
import re
import configparser
import recog

def send_thermos_discord(thermos):
    async def anything(url, thermos):
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(url, session=session)
            
            code = recog.getCode()
            
            embed = discord.Embed(title="Server rolled: ", description=code)
        
            # Format the weather data
            weather_data = [
                f"***--- 3-DAY OUTLOOK ---***",
                f"",
                f"**Day 1**: {thermos.get('DAY1', 'N/A')} | **Day 2**: {thermos.get('DAY2', 'N/A')} | **Day 3**: {thermos.get('DAY3', 'N/A')}",
                f"",
                f"***--- Thermodynamics ---***",
                f"",
                f"**Temperature**: {thermos.get('TEMPERATURE', 'N/A')}F",
                f"**Dewpoint**: {thermos.get('DEWPOINT', 'N/A')}F",
                f"**CAPE**: {thermos.get('CAPE', 'N/A')} J/kg",
                f"**3CAPE**: {thermos.get('THREECAPE', 'N/A')} J/kg",
                f"**0-3km Lapse Rates**: {thermos.get('LLAPSE', 'N/A')} C/km",
                f"**3-6km Lapse Rates**: {thermos.get('HLAPSE', 'N/A')} C/km",
                f"**PWAT**: {thermos.get('PWAT', 'N/A')} in.",
                f"**700-500mb RH**: {thermos.get('MBRH', 'N/A')}%",
                f"**Surface RH**: {thermos.get('SURFACERH', 'N/A')}%",
                f"**SRH**: {thermos.get('SRH', 'N/A')}",
                f"",
                f"***--- Composites ---***",
                f"",
                f"**STP**: {thermos.get('STP', 'N/A')}",
                f"**VTP**: {thermos.get('VTP', 'N/A')}"
            ]
            embed.add_field(name="Weather Data", value="\n".join(weather_data))
            await webhook.send(embed=embed)
        
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config.get('Settings', 'webhooklink')
    
    if not url == "":
        loop = asyncio.new_event_loop()
        loop.run_until_complete(anything(url, thermos))
        loop.close()
        
