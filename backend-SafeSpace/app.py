from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL connection (update credentials as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:MonAsh201199@54.79.69.184:6543/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the model for the crime statistics data
class CrimeStatYearly(db.Model):
    _tablename_ = 'melb_crime_stat_yearly'
    _table_args_ = {'schema': 'safespace_schema'}
    
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
    _tablename_ = 'aus_victims_by_gender_yearly'
    _table_args_ = {'schema': 'safespace_schema'}
    
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

class StreetLightingData(db.Model):
    _tablename_ = 'street_lighting_data'
    _table_args_ = {'schema': 'safespace_schema'}

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(12, 9), nullable=False)
    longitude = db.Column(db.Numeric(12, 9), nullable=False)
    ext_id = db.Column(db.Integer)
    emitted_lux_level = db.Column(db.Numeric(10, 3))
    postcode = db.Column(db.String(10))
    locality = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'latitude': float(self.latitude),
            'longitude': float(self.longitude),
            'ext_id': self.ext_id,
            'emitted_lux_level': float(self.emitted_lux_level) if self.emitted_lux_level is not None else None,
            'postcode': self.postcode,
            'locality': self.locality
        }

class PedestrianCountByPeriod(db.Model):
    _tablename_ = 'pedestrian_count_by_period'
    _table_args_ = {'schema': 'safespace_schema'}

    id = db.Column(db.Integer, primary_key=True)
    location_id = db.Column(db.Integer, nullable=False)
    sensing_date = db.Column(db.Date, nullable=False)
    period_of_time = db.Column(db.Text, nullable=False)
    total_pedestrian_count = db.Column(db.Integer)
    hours_covered = db.Column(db.Integer)
    avg_hourly_pedestrian_count = db.Column(db.Numeric(10, 4))
    sensor_description = db.Column(db.Text)
    sensor_name = db.Column(db.Text)
    latitude = db.Column(db.Numeric(12, 9))
    longitude = db.Column(db.Numeric(12, 9))
    postcode = db.Column(db.String(10))
    locality = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'location_id': self.location_id,
            'sensing_date': self.sensing_date.strftime('%Y-%m-%d') if self.sensing_date else None,
            'period_of_time': self.period_of_time,
            'total_pedestrian_count': self.total_pedestrian_count,
            'hours_covered': self.hours_covered,
            'avg_hourly_pedestrian_count': float(self.avg_hourly_pedestrian_count) if self.avg_hourly_pedestrian_count else None,
            'sensor_description': self.sensor_description,
            'sensor_name': self.sensor_name,
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None,
            'postcode': self.postcode,
            'locality': self.locality
        }
        
class PoliceStation(db.Model):
    __tablename__ = 'police_stations'
    __table_args__ = {'schema': 'safespace_schema'}

    id = db.Column(db.Integer, primary_key=True)
    facility_name = db.Column(db.Text, nullable=False)
    suburb = db.Column(db.Text)
    postcode = db.Column(db.String(10))
    latitude = db.Column(db.Numeric(12, 9))
    longitude = db.Column(db.Numeric(12, 9))
    formatted_address = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'facility_name': self.facility_name,
            'suburb': self.suburb,
            'postcode': self.postcode,
            'latitude': float(self.latitude) if self.latitude else None,
            'longitude': float(self.longitude) if self.longitude else None,
            'formatted_address': self.formatted_address
        }
        
class SelfDefenseCenter(db.Model):
    __tablename__ = 'self_defense_centers'
    __table_args__ = {'schema': 'safespace_schema'}

    id = db.Column(db.Integer, primary_key=True)
    academy_name = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    address = db.Column(db.Text, nullable=False)
    contact = db.Column(db.Text)
    website = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'academy_name': self.academy_name,
            'type': self.type,
            'address': self.address,
            'contact': self.contact,
            'website': self.website
        }
       
@app.route('/ping')
def ping():
    return "Pong!"
 
# Fetch Crime Stats
@app.route('/api/crime', methods=['GET'])
def get_crime_stats():
    records = CrimeStatYearly.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

# Fetch Victims Data
@app.route('/api/victims', methods=['GET'])
def get_victims_data():
    records = VictimsByGenderYearly.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

# Fetch Street Lighting Data
@app.route('/api/street_lighting', methods=['GET'])
def get_street_lighting_data():
    records = StreetLightingData.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

# Fetch Pedestrian Count Data
@app.route('/api/pedestrian_count', methods=['GET'])
def get_pedestrian_count_data():
    records = PedestrianCountByPeriod.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

# Fetch police station data
@app.route('/api/police_stations', methods=['GET'])
def get_police_stations():
    records = PoliceStation.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

# Fetch Self defense locations data
@app.route('/api/self_defense_centers', methods=['GET'])
def get_self_defense_centers():
    records = SelfDefenseCenter.query.all()
    data = [record.to_dict() for record in records]
    return jsonify(data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)