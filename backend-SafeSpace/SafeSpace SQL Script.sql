CREATE SCHEMA IF NOT EXISTS safespace_schema;
SET search_path TO safespace_schema;

CREATE TABLE safespace_schema.melb_crime_stat_yearly (
    id SERIAL PRIMARY KEY,
    year INTEGER,
    local_government_area VARCHAR(255),
    postcode VARCHAR(20),
    suburb_town_name VARCHAR(255),
    offence_division VARCHAR(255),
    offence_subdivision VARCHAR(255),
    offence_subgroup VARCHAR(255),
    incidents_recorded FLOAT,
    offence_count FLOAT,
    lat NUMERIC(9,6),
    lon NUMERIC(9,6)
);

CREATE TABLE safespace_schema.aus_victims_by_gender_yearly (
    id SERIAL PRIMARY KEY,
    year INTEGER,
    sex VARCHAR(50),
    offence_division VARCHAR(255),
    offence_subdivision VARCHAR(255),
    victims INTEGER,
    total_victims INTEGER
);

CREATE TABLE safespace_schema.street_lighting_data (
    id SERIAL PRIMARY KEY,
    latitude NUMERIC(12, 9) NOT NULL,
    longitude NUMERIC(12, 9) NOT NULL,
    ext_id INTEGER NOT NULL,
    emitted_lux_level NUMERIC(10, 3),
    suburb TEXT,
    postcode VARCHAR(10)
);

CREATE TABLE safespace_schema.pedestrian_count_by_period (
    id SERIAL PRIMARY KEY,
    location_id INTEGER NOT NULL,
    period_of_time TEXT NOT NULL,
    total_pedestrian_count INTEGER,
    hours_covered INTEGER,
    days_covered INTEGER,
    sensor_description TEXT,
    sensor_name TEXT,
    latitude NUMERIC(12, 9),
    longitude NUMERIC(12, 9),
    suburb TEXT,
    postcode VARCHAR(10)
);

CREATE TABLE safespace_schema.police_stations (
    id SERIAL PRIMARY KEY,
    facility_name TEXT NOT NULL,
    suburb TEXT,
    postcode VARCHAR(10),
    latitude NUMERIC(12, 9),
    longitude NUMERIC(12, 9),
    formatted_address TEXT
);

CREATE TABLE safespace_schema.self_defense_centers (
    id SERIAL PRIMARY KEY,
    academy_name TEXT NOT NULL,
    type TEXT NOT NULL,
    address TEXT NOT NULL,
    contact TEXT,
    website TEXT
);

