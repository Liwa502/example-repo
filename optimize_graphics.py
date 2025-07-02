import configparser
import os

# Path to your config file (for example)
config_path = "settings.cfg"

# Check if config file exists
if not os.path.exists(config_path):
    # Create a new one if it doesn't exist
    with open(config_path, "w") as f:
        f.write("[Graphics]\nResolution=1920x1080\nTextureQuality=High\nShadowQuality=High\n")

# Read existing config
config = configparser.ConfigParser()
config.read(config_path)

# If section doesn't exist, create it
if "Graphics" not in config:
    config["Graphics"] = {}

# Adjust settings for performance-quality balance
config["Graphics"]["Resolution"] = "1600x900"         # Slightly lower resolution for more FPS
config["Graphics"]["TextureQuality"] = "Medium"       # Lower textures save VRAM
config["Graphics"]["ShadowQuality"] = "Low"           # Shadows often hit FPS hardest

# Save changes
with open(config_path, "w") as configfile:
    config.write(configfile)

print("✅ Graphics settings optimized for better performance with decent quality!")
