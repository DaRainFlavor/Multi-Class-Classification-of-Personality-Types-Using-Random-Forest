# MBTI Quiz Website

A modern, beautiful MBTI personality quiz website built with Next.js and powered by an XGBoost machine learning model.

![MBTI Quiz](https://img.shields.io/badge/MBTI-Quiz-purple)
![Next.js](https://img.shields.io/badge/Next.js-15-black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-CSS-blue)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange)

## Features

- 🎯 **60 Questions** - Comprehensive personality assessment
- 🤖 **AI-Powered** - XGBoost machine learning model for accurate predictions
- 🎨 **Beautiful UI** - Modern glassmorphism design with smooth animations
- 📊 **Detailed Results** - Personality type, confidence scores, and probability distribution
- 🌐 **Vercel Ready** - Deployable to Vercel with Python serverless functions

## Screenshots

The quiz features a stunning dark theme with purple accents:
- **Landing Page** - Introduction to the quiz with MBTI dimensions
- **Quiz Page** - Question navigation with progress tracking
- **Results Page** - Detailed personality breakdown with traits and strengths

## Getting Started

### Prerequisites

- Node.js 18+ 
- Python 3.8+
- npm or yarn

### Installation

1. **Install frontend dependencies:**
   ```bash
   cd mbti-quiz
   npm install
   ```

2. **Install Python dependencies:**
   ```bash
   cd api
   pip install -r requirements.txt
   ```

3. **Train the model (if not already trained):**
   ```bash
   cd api
   python train_model.py
   ```

### Development

1. **Start the Flask API (Terminal 1):**
   ```bash
   cd api
   python app.py
   ```
   The API will run on http://localhost:5000

2. **Start Next.js development server (Terminal 2):**
   ```bash
   npm run dev
   ```
   The website will run on http://localhost:3000

### Production Deployment (Vercel)

1. Push to GitHub
2. Connect repository to Vercel
3. Vercel will automatically:
   - Build the Next.js frontend
   - Deploy Python serverless functions from `/api`

**Note:** For Vercel deployment, ensure the model files (`xgb_model.joblib`, `label_encoder.joblib`) are committed to the repository.

## Project Structure

```
mbti-quiz/
├── src/
│   ├── app/
│   │   ├── page.tsx          # Landing page
│   │   ├── quiz/
│   │   │   └── page.tsx      # Quiz interface
│   │   ├── results/
│   │   │   └── page.tsx      # Results display
│   │   ├── layout.tsx        # Root layout
│   │   └── globals.css       # Global styles
│   └── data/
│       ├── questions.ts      # 60 MBTI questions
│       └── personalities.ts  # 16 personality types
├── api/
│   ├── app.py               # Flask API (local development)
│   ├── predict.py           # Vercel serverless function
│   ├── train_model.py       # Model training script
│   ├── requirements.txt     # Python dependencies
│   ├── xgb_model.joblib     # Trained XGBoost model
│   └── label_encoder.joblib # Label encoder
├── vercel.json              # Vercel configuration
└── package.json
```

## API Endpoints

### Local Flask API

- `GET /health` - Health check
- `POST /predict` - Get MBTI prediction
- `GET /types` - List all personality types

### Vercel Serverless

- `POST /api/predict` - Get MBTI prediction

### Request/Response

**Request:**
```json
{
  "answers": [3, -2, 1, 0, ...] // 60 values from -3 to +3
}
```

**Response:**
```json
{
  "predicted_type": "INFP",
  "confidence": 0.847,
  "probabilities": {
    "INFP": 0.847,
    "INFJ": 0.092,
    ...
  }
}
```

## Technologies

- **Frontend:** Next.js 15, React, TypeScript, Tailwind CSS
- **Backend:** Flask, Python
- **ML Model:** XGBoost
- **Deployment:** Vercel

## License

MIT License
