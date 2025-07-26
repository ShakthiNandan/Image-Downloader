# Image Downloader

A Flask-based web application that allows users to search for images using Google Custom Search API and download them directly to their local machine.

## Features

- 🔍 **Image Search**: Search for images using Google Custom Search API
- 📥 **Bulk Download**: Download multiple images with a single click
- 🎯 **Custom Naming**: Automatically sanitizes filenames for safe storage
- 🔒 **Secure Configuration**: API keys stored in environment variables
- 📱 **Responsive Design**: Clean and modern web interface

## Screenshots

![Image Search Interface](static/screenshots/search-interface.png)
*Search interface for finding images*

![Search Results](static/screenshots/search-results.png)
*Image search results with download options*

## Prerequisites

Before running this application, you need:

1. **Python 3.7+** installed on your system
2. **Google Custom Search API Key** - [Get it here](https://developers.google.com/custom-search/v1/introduction)
3. **Custom Search Engine ID** - [Create one here](https://cse.google.com/)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShakthiNandan/Image-Downloader.git
   cd Image-Downloader
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   .venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install flask requests python-dotenv
   ```

5. **Set up environment variables**
   
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   Edit the `.env` file and add your API credentials:
   ```env
   API_KEY=your_google_api_key_here
   CSE_ID=your_custom_search_engine_id_here
   ```

## Configuration

### Google Custom Search API Setup

1. **Get an API Key**:
   - Go to the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Custom Search API
   - Create credentials (API Key)

2. **Create a Custom Search Engine**:
   - Visit [Google Custom Search](https://cse.google.com/)
   - Click "Add" to create a new search engine
   - Enter `www.google.com` as the site to search
   - Get your Search Engine ID from the setup page

3. **Configure Image Search**:
   - In your Custom Search Engine settings
   - Go to "Search Features" → "Image Search" → Turn ON

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your web browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Search for images**:
   - Enter your search query in the search box
   - Click "Search Images"
   - Browse through the results

4. **Download images**:
   - Click the "Download" button under any image
   - Images will be saved to the `static/downloads/` folder
   - Filenames are automatically sanitized for safety

## Project Structure

```
Image-Downloader/
├── app.py                 # Main Flask application
├── .env                   # Environment variables (not in repo)
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── static/
│   ├── styles.css        # CSS styling
│   └── downloads/        # Downloaded images storage
└── templates/
    ├── index.html        # Home page template
    └── results.html      # Search results template
```

## API Endpoints

### `GET /`
- **Description**: Home page with search form
- **Response**: HTML template for image search

### `POST /`
- **Description**: Process search query
- **Parameters**: 
  - `query` (form data): Search term for images
- **Response**: HTML template with search results

### `POST /download`
- **Description**: Download an image from URL
- **Parameters**: 
  - `url` (JSON): Image URL to download
  - `name` (JSON): Optional custom filename
- **Response**: JSON with status and message

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `API_KEY` | Google Custom Search API Key | Yes |
| `CSE_ID` | Custom Search Engine ID | Yes |

## Dependencies

- **Flask**: Web framework for Python
- **requests**: HTTP library for making API calls
- **python-dotenv**: Load environment variables from .env file
- **pathlib**: Path manipulation utilities (built-in)
- **re**: Regular expressions (built-in)
- **os**: Operating system interface (built-in)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- ⚠️ Never commit your `.env` file to version control
- 🔑 Keep your API keys secure and rotate them regularly
- 🌐 Consider implementing rate limiting for production use
- 🛡️ Validate and sanitize all user inputs

## Troubleshooting

### Common Issues

1. **"No module named 'flask'" error**
   - Make sure you've activated your virtual environment
   - Install dependencies: `pip install flask requests python-dotenv`

2. **"API Key not found" error**
   - Check that your `.env` file exists and contains valid API keys
   - Ensure the `.env` file is in the project root directory

3. **"No search results" error**
   - Verify your Custom Search Engine is configured for image search
   - Check that your CSE_ID is correct
   - Ensure your API key has sufficient quota

4. **Download failures**
   - Some images may be protected by CORS policies
   - Check that the image URLs are accessible
   - Verify the `static/downloads/` directory exists and is writable

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google Custom Search API for providing image search capabilities
- Flask framework for the web application structure
- The Python community for excellent libraries and documentation

## Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Search existing issues on GitHub
3. Create a new issue with detailed information about your problem

---

**Happy image searching! 🖼️✨**
