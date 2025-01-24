import re
import sys

# Define variables from script arguments
ENV_ID = sys.argv[1]
REPO_OWNER = sys.argv[2]
REPO_NAME = sys.argv[3]
VALID_ENV = sys.argv[4]

# Determine IMAGE_URL and ENV_PARAM based on VALID
if VALID_ENV == "true":
    IMAGE_URL = "https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qbraid_with_env_white.png"
    ENV_PARAM = f"&envId={ENV_ID}"
else:
    IMAGE_URL = "https://qbraid-static.s3.amazonaws.com/logos/Launch_on_qBraid_white.png"
    ENV_PARAM = ""

QBRAID_PREFIX = "https://qbraid-static.s3.amazonaws.com/logos/Launch_on"

# Read the content of README.md
with open("README.md", "r") as file:
    content = file.read()

# Define the pattern to match
pattern = re.compile(rf'\[<img src="{QBRAID_PREFIX}[^"]*" width="150">\]\(https://account.qbraid.com\?gitHubUrl=https://github.com/[^"]*\)')

# Define the replacement string
replacement = f'[<img src="{IMAGE_URL}" width="150">](https://account.qbraid.com?gitHubUrl=https://github.com/{REPO_OWNER}/{REPO_NAME}.git{ENV_PARAM})'

# Perform the replacement
new_content = pattern.sub(replacement, content)

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(new_content)

print("README.md has been updated.")