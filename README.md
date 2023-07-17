# Pyrogram Simple Template

This repository provides a basic template for writing Pyrogram code, which is a Python library to interact with the Telegram API. The template includes a simple script that initializes a Pyrogram client and runs it.

## Prerequisites

Before running the Pyrogram code, make sure you have the following installed:

- Python (3.10 or higher)
- Pip (Python package manager)

## Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/pyrogram-template.git
cd pyrogram-template
```

2. Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Configuration

1. Rename the `example.env` file to `.env`:

```bash
mv example.env .env
```

2. Open the `.env` file and fill in your Telegram API credentials:

```plaintext
API_ID=your_api_id
API_HASH=your_api_hash
```

Replace `your_api_id` and `your_api_hash` with the credentials obtained from the [Telegram API website](https://my.telegram.org/apps).

## Running the Script

To run the Pyrogram script, execute the following command:

```bash
python app.py
```

The script will initialize a Pyrogram client with the provided credentials and start running it.

## Customization

You can customize the Pyrogram client by modifying the `main.py` script. The provided code initializes the client with the following options:

- `name`: The name for the session file (can be customized as per your preference).
- `api_id`: The Telegram API ID obtained from the `.env` file.
- `api_hash`: The Telegram API hash obtained from the `.env` file.
- `workdir`: The directory where session files will be stored (default is `sessions`).
- `plugins`: The root directory where your Pyrogram plugins are located (default is `src`).

Feel free to adjust these options according to your specific use case.

## Contributing

If you find any issues with this template or have suggestions for improvements, please feel free to open an issue or submit a pull request.

Happy coding! 😄