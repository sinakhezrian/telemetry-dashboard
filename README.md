# Telemetry Dashboard

A simple, real-time dashboard to monitor your telemetry data. Built with Flask, PostgreSQL, and WebSockets for live updates.

## What You Get

- 📊 Real-time data visualization
- 🔌 Live WebSocket updates - no page refresh needed
- 💾 PostgreSQL database to store your telemetry
- 🐳 Docker ready - just one command to run
- 🚀 Simple REST API to send data

## What You Need

Just Docker and Docker Compose installed on your machine. That's it!

## Getting Started

1. **Clone this repo:**
```bash
git clone https://github.com/sinakhezrian/telemetry-dashboard.git
cd telemetry-dashboard
```

2. **Set up your environment:**
Create a `.env` file in the project root:
```properties
DATABASE_URL=postgresql://postgres:12345@localhost:5432/telemetry
SECRET_KEY=your_secret_key_here
FLASK_APP=app.py
FLASK_ENV=development
PORT=5000
```

3. **Fire it up:**
```bash
docker-compose up --build
```

4. **Check it out:**
Open your browser and go to `http://localhost:5000`

5. **When you're done:**
```bash
docker-compose down
```

## How to Use It

### Send Telemetry Data

**POST** to `/telemetry`:
```json
{
  "sensor": "CPU Usage",
  "value": 45.5
}
```

You'll get back:
```json
{
  "status": "success"
}
```

### Other Endpoints

- **`/`** - Main dashboard (the good stuff)
- **`/db-connection-test`** - Check if your database is connected

## Configure It Your Way

You can tweak these in your `.env` file:

| Setting | What It Does | Default |
|---------|--------------|---------|
| `PORT` | Which port to run on | 5000 |
| `DATABASE_URL` | Where your database lives | Required |
| `SECRET_KEY` | Your app's secret (keep it secret!) | Required |
| `FLASK_ENV` | Development or production mode | development |
| `FLASK_APP` | App entry point | app.py |

## What's Inside

```
telemetry-dashboard/
├── app.py                     # Where the magic happens
├── models.py                  # Database stuff
├── requirements.txt           # Python packages we need
├── DockerFile                 # Docker setup
├── docker-compose.yml         # Makes everything work together
├── .env                       # Your settings
├── templates/                 # HTML pages
│   ├── dashboard.html         # The main dashboard
│   └── database-status.html   # Database check page
└── static/                    # Client-side files
    └── dashboard.js           # Makes the magic happen in your browser
```

## Built With

- **Flask** - Lightweight Python web framework
- **PostgreSQL** - Reliable database
- **Socket.IO** - Real-time communication
- **Tailwind CSS** - Modern styling
- **Docker** - Easy deployment
