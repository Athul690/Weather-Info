#!/usr/bin/env python3
"""
================================================================================
                          WEATHER FORGE - PROFESSIONAL EDITION
                          Forging Weather Intelligence
                            by PELICAN HACKERS
================================================================================
"""

import urllib.request
import json
from datetime import datetime
import time
import os

# ============================================================================
# COLOR SCHEME - Purple, Red & White Theme
# ============================================================================
class Colors:
    RED = '\033[91m'
    BRIGHT_RED = '\033[91m'
    DARK_RED = '\033[31m'
    PURPLE = '\033[95m'
    DARK_PURPLE = '\033[35m'
    WHITE = '\033[97m'
    BRIGHT_WHITE = '\033[97m'
    GRAY = '\033[90m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# ============================================================================
# CUSTOM BANNER
# ============================================================================
def show_banner():
    """Display custom professional banner"""
    os.system('clear' if os.name == 'posix' else 'cls')

    banner = f"""
{Colors.PURPLE}┏┓┏┓┓ ┳┏┓┏┓┳┓  ┓ ┏┏┓┏┓┏┳┓┓┏┏┓┳┓  ┏┓┏┓┳┓┏┓┏┓
{Colors.DARK_PURPLE}┃┃┣ ┃ ┃┃ ┣┫┃┃  ┃┃┃┣ ┣┫ ┃ ┣┫┣ ┣┫  ┣ ┃┃┣┫┃┓┣
{Colors.PURPLE}┣┛┗┛┗┛┻┗┛┛┗┛┗  ┗┻┛┗┛┛┗ ┻ ┛┗┗┛┛┗  ┻ ┗┛┛┗┗┛┗┛{Colors.RESET}
"""
    print(banner)
    print(Colors.PURPLE + "═" * 80 + Colors.RESET)
    print(Colors.RED + Colors.BOLD + " " * 28 + "WEATHER FORGE" + Colors.RESET)
    print(Colors.WHITE + Colors.DIM + " " * 28 + "Forging Weather Intelligence" + Colors.RESET)
    print(Colors.RED + Colors.BOLD + " " * 32 + "by PELICAN HACKERS" + Colors.RESET)
    print(Colors.PURPLE + "═" * 80 + Colors.RESET)
    print()

# ============================================================================
# BOX DRAWING FUNCTIONS
# ============================================================================
def draw_top_border(title=""):
    """Draw top border with optional title"""
    print(Colors.PURPLE + "┌" + "─" * 78 + "┐" + Colors.RESET)
    if title:
        print(Colors.PURPLE + "│" + Colors.BOLD + Colors.WHITE + title.center(78) + Colors.PURPLE + "│" + Colors.RESET)
        print(Colors.PURPLE + "├" + "─" * 78 + "┤" + Colors.RESET)

def draw_bottom_border():
    """Draw bottom border"""
    print(Colors.PURPLE + "└" + "─" * 78 + "┘" + Colors.RESET)

def draw_separator():
    """Draw separator line"""
    print(Colors.PURPLE + "├" + "─" * 78 + "┤" + Colors.RESET)

def draw_line(content, color=Colors.WHITE):
    """Draw a line with content"""
    print(Colors.PURPLE + "│" + color + " " + content.ljust(77) + Colors.PURPLE + "│" + Colors.RESET)

# ============================================================================
# WEATHER FUNCTIONS
# ============================================================================
def get_weather(city):
    """Fetch weather data from API"""
    try:
        url = f"https://wttr.in/{city},Kerala,India?format=j1"
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req, timeout=10) as response:
            data = response.read()
            return json.loads(data)
    except:
        return None

def display_weather(city):
    """Display weather with professional formatting"""
    print()
    draw_top_border(f"{city.upper()}, KERALA")

    weather = get_weather(city)

    if not weather:
        draw_line("WEATHER DATA UNAVAILABLE", Colors.RED)
        draw_bottom_border()
        return False

    try:
        current = weather['current_condition'][0]
        forecast = weather['weather'][0]

        temp = current['temp_C']
        feels = current['FeelsLikeC']
        humidity = current['humidity']
        wind = current['windspeedKmph']
        desc = current['weatherDesc'][0]['value']
        max_temp = forecast['maxtempC']
        min_temp = forecast['mintempC']
        rain = forecast['hourly'][0].get('chanceofrain', '0')

        # Date and Time
        draw_line(f"Date: {datetime.now().strftime('%A, %B %d, %Y')}", Colors.GRAY)
        draw_line(f"Time: {datetime.now().strftime('%I:%M %p')}", Colors.GRAY)

        draw_separator()

        # Temperature Section
        draw_line("[ TEMPERATURE ]", Colors.BOLD + Colors.WHITE)
        draw_line(f"+ Current    --> {temp}°C")
        draw_line(f"+ Feels Like --> {feels}°C")
        draw_line(f"+ Min/Max    --> {min_temp}°C / {max_temp}°C")

        draw_separator()

        # Atmosphere Section
        draw_line("[ ATMOSPHERE ]", Colors.BOLD + Colors.WHITE)
        draw_line(f"+ Humidity    --> {humidity}%")
        draw_line(f"+ Wind Speed  --> {wind} km/h")
        draw_line(f"+ Rain Chance --> {rain}%")

        draw_separator()

        # Conditions
        draw_line("[ CONDITIONS ]", Colors.BOLD + Colors.WHITE)
        draw_line(f"+ Weather --> {desc}")

        draw_separator()

        # Advisory
        draw_line("[ ADVISORY ]", Colors.BOLD + Colors.WHITE)

        if int(temp) >= 35:
            draw_line("+ Extreme heat detected", Colors.RED)
            draw_line("  --> Stay hydrated, avoid direct sunlight")
        elif int(temp) >= 32:
            draw_line("+ Hot conditions", Colors.YELLOW)
            draw_line("  --> Use umbrella, wear light clothes")
        elif int(temp) <= 24:
            draw_line("+ Pleasant weather", Colors.GREEN)
            draw_line("  --> Perfect for outdoor activities")

        if int(rain) > 70:
            draw_line("+ Heavy rain expected", Colors.BLUE)
            draw_line("  --> Carry umbrella, drive carefully")
        elif int(rain) > 40:
            draw_line("+ Light rain possible", Colors.CYAN)
            draw_line("  --> Better to carry umbrella")

        if int(humidity) > 80:
            draw_line("+ High humidity", Colors.MAGENTA)
            draw_line("  --> Stay in cool places")

        draw_bottom_border()
        return True

    except Exception as e:
        draw_line(f"Error: {str(e)[:50]}", Colors.RED)
        draw_bottom_border()
        return False

# ============================================================================
# CITY LIST
# ============================================================================
def show_cities():
    """Display all available cities in Kerala"""
    cities = [
        "Thiruvananthapuram", "Kochi", "Kozhikode", "Kollam",
        "Thrissur", "Palakkad", "Alappuzha", "Kannur",
        "Kottayam", "Pathanamthitta", "Malappuram", "Wayanad",
        "Idukki", "Kasargod"
    ]

    print()
    draw_top_border("AVAILABLE CITIES IN KERALA")

    # Display cities in 2 columns
    for i in range(0, len(cities), 2):
        line = f"  {i+1:2}. {cities[i]:<22}"
        if i+1 < len(cities):
            line += f"  {i+2:2}. {cities[i+1]:<22}"
        draw_line(line)

    draw_bottom_border()
    print()

# ============================================================================
# MAIN MENU
# ============================================================================
def main():
    """Main program entry point"""
    show_banner()
    show_cities()

    while True:
        draw_top_border("MAIN MENU")
        draw_line("[1]  Search City Weather")
        draw_line("[2]  List All Cities")
        draw_line("[3]  Exit")
        draw_bottom_border()

        print()
        choice = input(Colors.WHITE + "    --> Choose option [1-3]: " + Colors.RESET).strip()

        if choice == '1':
            print()
            draw_top_border("SEARCH WEATHER")
            draw_bottom_border()

            print()
            city = input(Colors.WHITE + "    --> Enter city name: " + Colors.RESET).strip().title()

            if city:
                display_weather(city)
            else:
                print(Colors.RED + "\n    [!] Invalid city name" + Colors.RESET)

            print()
            input(Colors.GRAY + "    --> Press Enter to continue..." + Colors.RESET)
            show_banner()
            show_cities()

        elif choice == '2':
            show_cities()
            input(Colors.GRAY + "    --> Press Enter to continue..." + Colors.RESET)
            show_banner()
            show_cities()

        elif choice == '3':
            print()
            draw_top_border("")
            draw_line("THANK YOU FOR USING WEATHER FORGE", Colors.GREEN)
            draw_line("GOODBYE!", Colors.WHITE)
            draw_bottom_border()
            print()
            break

        else:
            print(Colors.RED + "\n    [!] Invalid choice! Please select 1, 2, or 3" + Colors.RESET)
            time.sleep(1)

# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.YELLOW + "\n\n    [!] Program interrupted" + Colors.RESET)
        print(Colors.WHITE + "    --> Goodbye!" + Colors.RESET)
        print()
    except Exception as e:
        print(Colors.RED + f"\n    [!!] Fatal Error: {e}" + Colors.RESET)
