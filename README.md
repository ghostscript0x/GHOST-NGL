# Ghost NGL 🌑

**Anonymous Messaging from the Shadows**

[![GitHub stars](https://img.shields.io/github/stars/ghostscript0x/ghost-ngl?style=social)](https://github.com/ghostscript0x/ghost-ngl)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1+-red.svg)](https://flask.palletsprojects.com/)

Ghost NGL is a privacy-focused anonymous messaging platform where users can send and receive secret messages without revealing their identities. Built with modern web technologies, it offers a sleek, mobile-first experience with PWA support.

## ✨ Features

- 🔒 **Anonymous Messaging**: Send and receive messages without identity disclosure
- 📱 **PWA Support**: Install as a web app with offline capabilities
- 🌙 **Dark/Light Mode**: Toggle between themes for comfortable viewing
- 📸 **Screenshot Sharing**: Share messages as beautiful images via WhatsApp
- 👤 **Custom Email Domains**: Unique @ghostngl.com emails for registration
- 📨 **Read Receipts**: Track message status in your inbox
- 🔄 **Responsive Design**: Optimized for mobile and desktop
- 🚀 **Fast & Secure**: Built with Flask and modern security practices

## 🚀 Demo

![Ghost NGL Demo](https://via.placeholder.com/800x400?text=Demo+Screenshot+Coming+Soon)

*Live demo available at: [https://ghost-ngl.vercel.app](https://ghost-ngl.vercel.app)*

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Git
- PostgreSQL (recommended for production) or SQLite (for development)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ghostscript0x/ghost-ngl.git
   cd ghost-ngl
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Open in browser:**
   Navigate to `http://localhost:5000`

## 📖 Usage

### For Users

1. **Register:** Create an account with a unique handle and @ghostngl.com email
2. **Share Your Link:** Copy your anonymous link and share it anywhere
3. **Receive Messages:** View messages in your inbox with read receipts
4. **Reply:** Share messages as screenshots on WhatsApp

### For Developers

- **API Endpoints:** Check `/api/unread-count` for unread messages
- **Customization:** Modify templates in `templates/` and styles in Tailwind classes

## 🚀 Deployment

### Vercel (Recommended)

1. Connect your GitHub repo to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push

### Other Platforms

- **Heroku:** Use the `Procfile` and `requirements.txt`
- **Railway:** Connect repo and set environment variables
- **Docker:** Build from the included Dockerfile

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**ghostscript0x**
- GitHub: [@ghostscript0x](https://github.com/ghostscript0x)
- Email: ghostscript0x@gmail.com

---

⭐ If you like this project, give it a star on GitHub!

*Designed and developed by [ghostscript0x](https://github.com/ghostscript0x)*