from flask import Flask, jsonify, Response,request
from flask_sqlalchemy import SQLAlchemy
from visualisations import generate_aggregated_map, get_insights_text
from visualisations import generate_trend_chart
from visualisations import fetch_trend_data, create_summary_table, create_plotly_table
from datetime import datetime

app = Flask(__name__)

# Configure the PostgreSQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MonAsh%40201199@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the model for the crime statistics data
class CrimeStatYearly(db.Model):
    __tablename__ = 'melb_crime_stat_yearly'
    __table_args__ = {'schema': 'safespace_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    local_government_area = db.Column(db.String(255))
    postcode = db.Column(db.String(20))
    suburb_town_name = db.Column(db.String(255))
    offence_division = db.Column(db.String(255))
    offence_subdivision = db.Column(db.String(255))
    offence_subgroup = db.Column(db.String(255))
    incidents_recorded = db.Column(db.Float)
    offence_count = db.Column(db.Float)
    lat = db.Column(db.Numeric(9, 6))
    lon = db.Column(db.Numeric(9, 6))
    
    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'local_government_area': self.local_government_area,
            'postcode': self.postcode,
            'suburb_town_name': self.suburb_town_name,
            'offence_division': self.offence_division,
            'offence_subdivision': self.offence_subdivision,
            'offence_subgroup': self.offence_subgroup,
            'incidents_recorded': self.incidents_recorded,
            'offence_count': self.offence_count,
            'lat': float(self.lat) if self.lat is not None else None,
            'lon': float(self.lon) if self.lon is not None else None
        }
        
# Define the model for your victims data
class VictimsByGenderYearly(db.Model):
    __tablename__ = 'aus_victims_by_gender_yearly'
    __table_args__ = {'schema': 'safespace_schema'}
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    sex = db.Column(db.String(50))
    offence_division = db.Column(db.String(255))
    offence_subdivision = db.Column(db.String(255))
    victims = db.Column(db.Integer)
    total_victims = db.Column(db.Integer)
    
    def to_dict(self):
        return {
            'id': self.id,
            'year': self.year,
            'sex': self.sex,
            'offence_division': self.offence_division,
            'offence_subdivision': self.offence_subdivision,
            'victims': self.victims,
            'total_victims': self.total_victims
        }

# Home route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the SafeSpace API"})

# Endpoint to retrieve raw crime statistics data
@app.route('/api/crime', methods=['GET'])
def get_crime_stats():
    records = CrimeStatYearly.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

# Endpoint to serve the aggregated crime map visualization
@app.route('/api/aggregated_map', methods=['GET'])
def aggregated_map():
    selected_year = request.args.get('year', default=2015, type=int)
    map_object = generate_aggregated_map(db, CrimeStatYearly, year=selected_year)
    html_str = map_object.get_root().render()
    return Response(html_str, mimetype='text/html')

# Endpoint to fetch dynamic textual insights for the selected year.
@app.route('/api/insights', methods=['GET'])
def insights():
    selected_year = request.args.get('year', default=2015, type=int)
    insight_html = get_insights_text(db, CrimeStatYearly, year=selected_year)
    return Response(insight_html, mimetype='text/html')

# Endpoint to get trend chart visualization
@app.route('/api/trend_chart', methods=['GET'])
def trend_chart():
    html_str = generate_trend_chart(db, VictimsByGenderYearly)
    return Response(html_str, mimetype='text/html')

@app.route('/api/trend_table', methods=['GET'])
def trend_table():
    df_gender, df_overall = fetch_trend_data(db, VictimsByGenderYearly)
    summary_df = create_summary_table(df_gender, df_overall)
    table_fig = create_plotly_table(summary_df)
    html_str = table_fig.to_html(full_html=False)
    return Response(html_str, mimetype='text/html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)