# FreshAI Service

A modern full-stack ticket management system that integrates with FreshService API. Built with FastAPI (backend) and React (frontend), featuring server-side filtering, pagination, and intelligent ticket management capabilities.

## 🚀 Features

- **Ticket Management**: View, filter, and manage support tickets from FreshService
- **Smart Filtering**: Filter tickets by group with server-side optimization
- **Pagination**: Efficient pagination with "Load More" functionality
- **Real-time Updates**: Dynamic ticket updates and filtering
- **AI Analysis Panel**: Analyze tickets with AI-powered insights
- **Responsive UI**: Modern glass-morphism design with smooth interactions
- **Search Functionality**: Quick search across tickets by ID, subject, or status

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.8+ ([Download](https://www.python.org/downloads/))
- **Node.js** 18+ and npm ([Download](https://nodejs.org/))
- **Git** ([Download](https://git-scm.com/))
- **FreshService API Key** ([Get one](https://support.freshservice.com/en/articles/1144525-freshservice-api-key))

## 🔧 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/SantiagoSC1999/FreshAI-Service.git
cd FreshAI-Service
```

### Step 2: Backend Setup

#### 2.1 Create Python Virtual Environment

```bash
cd backend
python -m venv venv
```

**On Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**

```cmd
venv\Scripts\activate.bat
```

**On macOS/Linux:**

```bash
source venv/bin/activate
```

#### 2.2 Install Python Dependencies

```bash
pip install -r requirements.txt
```

#### 2.3 Configure Environment Variables

Create a `.env` file in the `backend` folder:

```bash
cp .env.example .env
```

Edit `.env` and add your FreshService credentials:

```env
FRESHSERVICE_API_KEY=your_api_key_here
FRESHSERVICE_DOMAIN=your_domain_here
```

**Example:**

```env
FRESHSERVICE_API_KEY=abc123def456
FRESHSERVICE_DOMAIN=alliance
```

> 💡 **Where to get these values?**
>
> - API Key: Go to FreshService Admin → API Tokens
> - Domain: The subdomain in your FreshService URL (e.g., `https://alliance.freshservice.com` → `alliance`)

#### 2.4 Start Backend Server

```bash
python main.py
```

You should see:

```
✅ Tickets routes registered
🚀 Starting server...
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Backend is now running at **http://localhost:8000**

### Step 3: Frontend Setup

#### 3.1 Navigate to Client Folder

```bash
cd ../client
```

#### 3.2 Install Node Dependencies

```bash
npm install
```

#### 3.3 Configure Environment Variables

Create a `.env` file in the `client` folder (if not already present):

```env
VITE_API_URL=http://localhost:8000/api
```

#### 3.4 Start Frontend Development Server

```bash
npm run dev
```

You should see:

```
VITE v7.2.4  ready in X.XXX ms

➜  Local:   http://localhost:5173/
```

Frontend is now running at **http://localhost:5173**

## 📱 Accessing the Application

1. Open your browser and navigate to **http://localhost:5173**
2. The dashboard will load with your FreshService tickets
3. Use the filters to manage tickets by group and status
4. Click "Load More" to paginate through tickets

## 📁 Project Structure

```
FreshAI-Service/
│
├── backend/                          # Python FastAPI Backend
│   ├── api/
│   │   ├── routes/
│   │   │   └── tickets.py           # Ticket endpoints
│   │   └── freshservice_client.py   # FreshService API client
│   ├── config.py                    # Configuration
│   ├── main.py                      # Entry point
│   └── requirements.txt             # Python dependencies
│
├── client/                           # React Frontend
│   ├── src/
│   │   ├── components/              # React components
│   │   ├── pages/                   # Page components
│   │   ├── hooks/                   # Custom React hooks
│   │   ├── services/                # API client service
│   │   ├── store/                   # Zustand state management
│   │   └── styles/                  # Global styles
│   ├── package.json                 # Node dependencies
│   └── vite.config.ts              # Vite configuration
│
└── README.md                         # This file
```

## 🔌 API Endpoints

### Tickets

**Get Paginated Tickets**

```
GET /api/tickets?page=1&per_page=30&group_id=26000250424
```

**Get Single Ticket**

```
GET /api/tickets/{id}
```

**Get Ticket Conversations**

```
GET /api/tickets/{id}/conversations
```

**Search Tickets**

```
GET /api/tickets/search?query=keyword
```

## 🛠️ Available Commands

### Backend

```bash
# Start development server (from backend folder)
python main.py

# Run tests
python -m pytest tests/
```

### Frontend

```bash
# Start development server (from client folder)
npm run dev

# Build for production
npm run build

# Run linting
npm run lint

# Preview production build
npm run preview
```

## 🌐 Environment Variables

### Backend (.env)

| Variable               | Description               | Example        |
| ---------------------- | ------------------------- | -------------- |
| `FRESHSERVICE_API_KEY` | Your FreshService API key | `abc123def456` |
| `FRESHSERVICE_DOMAIN`  | Your FreshService domain  | `alliance`     |

### Frontend (.env)

| Variable       | Description     | Default                     |
| -------------- | --------------- | --------------------------- |
| `VITE_API_URL` | Backend API URL | `http://localhost:8000/api` |

## 📦 Dependencies

### Backend

- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **Requests** - HTTP library
- **Python-dotenv** - Environment variables

### Frontend

- **React** 19.2 - UI library
- **Vite** 7.2 - Build tool
- **TypeScript** 5.9 - Type safety
- **Axios** - HTTP client
- **Zustand** - State management
- **React Router** - Routing

## 🐛 Troubleshooting

### Backend Issues

**Error: "vite is not recognized"**

```bash
cd client
npm install
npm run dev
```

**Error: "FreshService credentials not configured"**

- Verify `.env` file exists in `backend` folder
- Check `FRESHSERVICE_API_KEY` and `FRESHSERVICE_DOMAIN` are set correctly

**Error: "Port 8000 already in use"**

```bash
# On Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# On macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Frontend Issues

**Error: "Cannot find module"**

```bash
npm install
npm run build  # Check for TypeScript errors
```

**Port 5173 already in use**

```bash
# On Windows
netstat -ano | findstr :5173
taskkill /PID <PID> /F

# On macOS/Linux
lsof -ti:5173 | xargs kill -9
```

## 🚀 Production Deployment

### Build Frontend

```bash
cd client
npm run build
```

This creates a `dist` folder with optimized production files.

### Backend Deployment

For production, use a production-grade ASGI server:

```bash
pip install gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## 📝 Git Workflow

```bash
# Check status
git status

# Stage changes
git add .

# Commit
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

## 🔐 Security Notes

- Never commit `.env` files (already in `.gitignore`)
- Keep API keys and sensitive data private
- Use environment variables for all credentials
- Rotate API keys regularly

## 📚 Documentation

- [FreshService API Documentation](https://api.freshservice.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

## 🤝 Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Santiago Sánchez - [GitHub](https://github.com/SantiagoSC1999)

## 💬 Support

For issues or questions, please open an issue on [GitHub Issues](https://github.com/SantiagoSC1999/FreshAI-Service/issues).

## 🔄 Updates & Maintenance

To pull the latest updates:

```bash
git pull origin main
cd backend && pip install -r requirements.txt
cd ../client && npm install
```

---

**Last Updated**: December 2, 2025

Happy coding! 🚀
