# SIHSportsbook (Stuck In Highschool Sportsbook)

<div style="display: flex; flex-wrap: wrap; gap: 5px;">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS"/>
  <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
</div>

## The Project That Changed Everything

SIHSportsbook holds a special place in my heart as the project that truly helped me break free from tutorial hell and establish myself as a developer. This was my first substantial application where I went beyond basic scripts and notebooks, tackling real challenges and creating something uniquely interesting... Well not actually, I did play test this with some of my friends and feedback was pretty good, but before I actually got the whole league into it, sleeper stopped supporting their projections API. Oh well, now I know how to make fun stuff anyway.

## What It Does

SIHSportsbook transforms fantasy football projections into a true betting experience for fantasy league members. The system:

- Takes Sleeper app projections and win rate predictions
- Converts fantasy metrics into realistic betting odds
- Generates moneyline, spread, and over/under bets
- Presents a clean, intuitive betting interface for league members
- Tracks performance and standings within the betting community

## Why It Matters

Beyond the technical achievements, this project represents a personal milestone. It was born from a passion for both fantasy sports and coding, combining two worlds in a way that created genuine enjoyment for friends. The late nights debugging database issues, the breakthrough moments figuring out the odds algorithms, and the satisfaction of seeing league mates use something I built from scratch - all of these experiences solidified my identity as a developer.

## Technical Details

### Core Components
- **Django Backend**: Handles data processing, odds calculation, and user management
- **Sleeper API Integration**: Pulls player projections and matchup data
- **Odds Calculation Engine**: Custom algorithm to convert projections to betting lines
- **Responsive Frontend**: Built with JavaScript, HTML, and CSS
- **AWS Deployment**: Hosted on EC2 and Lightsail for reliability
- **Containerized**: Docker implementation for consistent deployment

### Key Features
- **Automated Odds Generation**: Weekly calculation of betting lines based on latest projections
- **User Account System**: Personalized tracking of bets and performance
- **League Leaderboard**: Competitive standings based on betting success
- **Responsive Design**: Mobile-friendly interface for betting on the go
- **Admin Controls**: Special commissioner features for league management

## Development Journey

What started as a simple script to convert projections into odds quickly evolved into a full-stack application. Learning to deploy on AWS, managing database migrations, and implementing responsive design were all challenges that pushed my skills forward. Each problem solved was a stepping stone toward confidence as a developer.

## Deployment

The application is containerized with Docker and deployed on AWS using:
- **EC2**: Main application hosting
- **Lightsail**: Database and supporting services
- **S3**: Static file storage

## Future Ideas

While the project accomplished its goals, some ideas for future enhancements include:
- Implementing real-time updates based on injury news
- Adding prop-bet style wagers for individual player performances
- Creating historical analysis of betting performance
- Adding social features for trash talk and discussion

## Getting Started

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- AWS account (for deployment)

### Local Setup
1. Clone the repository
```bash
git clone https://github.com/yourusername/SIHSportsbook.git
cd SIHSportsbook
```

2. Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

### Docker Setup
```bash
docker-compose up -d
```

## License
MIT License

---

*This project represents more than code - it's the moment I truly became a developer.*
