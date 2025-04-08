import folium
from folium.plugins import MiniMap
from sqlalchemy import func
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

def get_color(value):
    if value <= 20:
        return "#00FF00" 
    elif value <= 50:
        return "#66FF00" 
    elif value <= 100:
        return "#FFCC00"  
    else:
        return "#FF0000" 

def generate_aggregated_map(db, CrimeStatYearly, year=2015):

    aggregated = db.session.query(
        CrimeStatYearly.suburb_town_name,
        func.sum(CrimeStatYearly.offence_count).label('total_offence'),
        func.avg(CrimeStatYearly.lat).label('lat'),
        func.avg(CrimeStatYearly.lon).label('lon')
    ).filter(CrimeStatYearly.year == year) \
     .group_by(CrimeStatYearly.suburb_town_name).all()

    highest = db.session.query(
        CrimeStatYearly.suburb_town_name,
        func.sum(CrimeStatYearly.offence_count).label('total_offence')
    ).filter(CrimeStatYearly.year == year)\
     .group_by(CrimeStatYearly.suburb_town_name)\
     .order_by(func.sum(CrimeStatYearly.offence_count).desc())\
     .first()

    lowest = db.session.query(
        CrimeStatYearly.suburb_town_name,
        func.sum(CrimeStatYearly.offence_count).label('total_offence')
    ).filter(CrimeStatYearly.year == year)\
     .group_by(CrimeStatYearly.suburb_town_name)\
     .order_by(func.sum(CrimeStatYearly.offence_count))\
     .first()

    highest_suburb = highest.suburb_town_name if highest else "N/A"
    highest_offence = int(highest.total_offence) if highest else 0
    lowest_suburb = lowest.suburb_town_name if lowest else "N/A"
    lowest_offence = int(lowest.total_offence) if lowest else 0

    m = folium.Map(location=[-37.8136, 144.9631], zoom_start=12)

    minimap = MiniMap(toggle_display=True)
    m.add_child(minimap)

    # Add circle markers with gradient color coding based on total_offence.
    for suburb, total, lat, lon in aggregated:
        if lat is not None and lon is not None:
            color = get_color(total)
            tooltip_text = f"<strong>{suburb}</strong><br>Total Offences ({year}): {total}"
            folium.CircleMarker(
                location=[float(lat), float(lon)],
                radius=8,
                tooltip=tooltip_text,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.8
            ).add_to(m)

    legend_html = '''
    <div style="
        position: fixed; 
        bottom: 50px; left: 50px; width: 250px; height: 120px; 
        background-color: white; 
        border:2px solid grey; 
        z-index:9999; 
        font-size:14px;
        padding: 10px;
        ">
        <b>Color Scale Legend</b><br>
        <span style="color:#00FF00;">&#9679;</span> Low (<= 20)<br>
        <span style="color:#66FF00;">&#9679;</span> Moderate (21 - 50)<br>
        <span style="color:#FFCC00;">&#9679;</span> High (51 - 100)<br>
        <span style="color:#FF0000;">&#9679;</span> Very High (> 100)
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))

    insights_html = f'''
    <div style="
        position: fixed; 
        top: 10px; right: 10px; width: 220px; 
        background-color: white; 
        border:2px solid grey; 
        z-index:9999; 
        font-size:14px;
        padding: 10px;
    ">
        <b>Year: {year}</b><br>
        <b>Highest:</b> {highest_suburb} ({highest_offence})<br>
        <b>Lowest:</b> {lowest_suburb} ({lowest_offence})
    </div>
    '''
    m.get_root().html.add_child(folium.Element(insights_html))

    return m

def get_insights_text(db, CrimeStatYearly, year=2015):

    highest = db.session.query(
        CrimeStatYearly.suburb_town_name,
        func.sum(CrimeStatYearly.offence_count).label('total_offence')
    ).filter(CrimeStatYearly.year == year)\
     .group_by(CrimeStatYearly.suburb_town_name)\
     .order_by(func.sum(CrimeStatYearly.offence_count).desc())\
     .first()

    lowest = db.session.query(
        CrimeStatYearly.suburb_town_name,
        func.sum(CrimeStatYearly.offence_count).label('total_offence')
    ).filter(CrimeStatYearly.year == year)\
     .group_by(CrimeStatYearly.suburb_town_name)\
     .order_by(func.sum(CrimeStatYearly.offence_count))\
     .first()

    highest_suburb = highest.suburb_town_name if highest else "N/A"
    highest_offence = int(highest.total_offence) if highest else 0
    lowest_suburb = lowest.suburb_town_name if lowest else "N/A"
    lowest_offence = int(lowest.total_offence) if lowest else 0

    insight_text = f"""
    <p style="font-family: Arial, sans-serif; font-size: 16px;">
    In {year}, data shows that the suburb with the highest offence count was 
    <strong>{highest_suburb}</strong> with <strong>{highest_offence}</strong> offences, while the suburb with the lowest count was 
    <strong>{lowest_suburb}</strong> with <strong>{lowest_offence}</strong> offences. These insights reveal key local risk areas and can help you make informed decisions when planning your routes.
    You can use these insights stay aware—areas with higher reported incidents may require extra caution. Remember, even in zones with lower numbers, remaining alert and informed helps protect your personal safety.
    If you or someone you know experiences harassment or feels unsafe, help is 
    available—24 hours a day, 7 days a week—through the Victorian Government's 
    <strong>1800RESPECT</strong> service. You can 
    <strong>call 1800 737 732</strong>, or 
    <strong>text 0435 737 732</strong> 
    to speak with someone today. 
    Remember, staying informed about local safety data is just one part of protecting 
    yourself—knowing where to turn for immediate support is equally important.
    </p>
    """
    return insight_text

def generate_trend_chart(db, VictimsByGenderYearly):

    results = db.session.query(
        VictimsByGenderYearly.year,
        VictimsByGenderYearly.sex,
        func.sum(VictimsByGenderYearly.victims).label('total_victims')
    ).group_by(VictimsByGenderYearly.year, VictimsByGenderYearly.sex).order_by(VictimsByGenderYearly.year).all()

    df = pd.DataFrame(results, columns=['year', 'sex', 'total_victims'])

    fig = px.line(
        df,
        x='year',
        y='total_victims',
        color='sex',
        markers=True,
        title='Victim Trends Over Time by Gender',
        labels={'year': 'Year', 'total_victims': 'Number of Victims', 'sex': 'Gender'},
        color_discrete_sequence=['#5DADE2', '#F5B041']
    )

    overall_results = db.session.query(
        VictimsByGenderYearly.year,
        func.sum(VictimsByGenderYearly.victims).label('overall_victims')
    ).group_by(VictimsByGenderYearly.year).order_by(VictimsByGenderYearly.year).all()

    df_overall = pd.DataFrame(overall_results, columns=['year', 'overall_victims'])

    fig.add_scatter(
        x=df_overall['year'],
        y=df_overall['overall_victims'],
        mode='lines+markers',
        name='Overall Victims',
        line=dict(color='#2E86C1', dash='dash'),
        hovertemplate="Year: %{x}<br>Number of Victims: %{y}"
    )

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        legend=dict(
            title=dict(text='Legend (click to hide/show lines)'),
            orientation='v',    
            x=1.02,             
            xanchor='left',    
            y=1,                
            yanchor='top'
        )
    )

    # Update axes to display the axis lines explicitly
    fig.update_xaxes(
        showgrid=False,
        showline=True,
        linewidth=1,
        linecolor='black',
        mirror=True
    )
    fig.update_yaxes(
        showgrid=False,
        showline=True,
        linewidth=1,
        linecolor='black',
        mirror=True
    )

    return fig.to_html(full_html=False)

def fetch_trend_data(db, VictimsByGenderYearly):
    results = db.session.query(
        VictimsByGenderYearly.year,
        VictimsByGenderYearly.sex,
        func.sum(VictimsByGenderYearly.victims).label('total_victims')
    ).group_by(VictimsByGenderYearly.year, VictimsByGenderYearly.sex)\
     .order_by(VictimsByGenderYearly.year).all()
    
    df_gender = pd.DataFrame(results, columns=['year', 'sex', 'total_victims'])
    
    overall_results = db.session.query(
        VictimsByGenderYearly.year,
        func.sum(VictimsByGenderYearly.victims).label('overall_victims')
    ).group_by(VictimsByGenderYearly.year).order_by(VictimsByGenderYearly.year).all()
    
    df_overall = pd.DataFrame(overall_results, columns=['year', 'overall_victims'])
    
    return df_gender, df_overall

def create_summary_table(df_gender, df_overall):
    
    table_df = df_gender.pivot(index='year', columns='sex', values='total_victims').reset_index()

    table_df = pd.merge(table_df, df_overall, on='year', how='left')

    table_df.rename(columns={
        'year': 'Year',
        'females': 'Females',
        'males': 'Males',
        'overall_victims': 'Overall Victims'
    }, inplace=True)

    table_df['Female victims (%)'] = (table_df['Females'] / table_df['Overall Victims']) * 100
    table_df['Male victims (%)'] = (table_df['Males'] / table_df['Overall Victims']) * 100

    table_df['Female victims (%)'] = table_df['Female victims (%)'].round(1)
    table_df['Male victims (%)'] = table_df['Male victims (%)'].round(1)

    table_df.sort_values('Year', inplace=True)

    return table_df

def create_plotly_table(table_df):
    header_values = list(table_df.columns)
    cell_values = [table_df[col].tolist() for col in table_df.columns]
    
    table_fig = ff.create_table(
        [header_values] + list(zip(*cell_values)), 
        index=False
    )
    
    n_columns = len(header_values)
    
    # Loop through annotations
    for i, annotation in enumerate(table_fig.layout.annotations):
        if i < n_columns:
            annotation.font.color = 'white'
            annotation.font.size = 14
            annotation.text = f"<b>{annotation.text}</b>"
        else:
            annotation.font.color = 'black'
            annotation.font.size = 12

    return table_fig