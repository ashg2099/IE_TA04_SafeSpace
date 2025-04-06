import folium
from folium.plugins import MiniMap
from sqlalchemy import func
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff

def get_color(value):
    if value <= 50:
        return "#00FF00"
    elif value <= 500:
        ratio = (value - 50) / 450.0
        r = int(0 + ratio * 255)  
        g = 255                   
        b = 0                    
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    elif value <= 2000:
        ratio = (value - 500) / 1500.0
        r = 255                  
        g = int(255 - ratio * 255)  
        b = 0
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    else:
        return "#FF0000"  

def generate_aggregated_map(db, CrimeStatYearly):
    aggregated = db.session.query(
        CrimeStatYearly.suburb_town_name,
        func.sum(CrimeStatYearly.offence_count).label('total_offence'),
        func.avg(CrimeStatYearly.lat).label('lat'),
        func.avg(CrimeStatYearly.lon).label('lon')
    ).group_by(CrimeStatYearly.suburb_town_name).all()

    
    m = folium.Map(location=[-37.8136, 144.9631], zoom_start=12)

    
    minimap = MiniMap(toggle_display=True)
    m.add_child(minimap)

    
    for suburb, total, lat, lon in aggregated:
        if lat is not None and lon is not None:
            color = get_color(total)
            tooltip_text = f"<strong>{suburb}</strong><br>Total Offences: {total}"
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
        bottom: 50px; left: 50px; width: 250px; height: 140px; 
        background-color: white; 
        border:2px solid grey; 
        z-index:9999; 
        font-size:14px;
        padding: 10px;
        ">
        <b>Color Scale Legend</b><br>
        <span style="color:#00FF00;">&#9679;</span> Low (<= 50)<br>
        <span style="color:#66FF00;">&#9679;</span> Moderate (50 - 500)<br>
        <span style="color:#FFCC00;">&#9679;</span> High (500 - 2000)<br>
        <span style="color:#FF0000;">&#9679;</span> Very High (> 2000)
    </div>
     '''
    m.get_root().html.add_child(folium.Element(legend_html))

    return m

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

# Summary table displaying total numbers 
# def create_summary_table(df_gender, df_overall):
    
#     table_df = df_gender.pivot(index='year', columns='sex', values='total_victims').reset_index()
    
#     table_df = pd.merge(table_df, df_overall, on='year', how='left')
    
#     table_df.rename(columns={
#         'year': 'Year',
#         'females': 'Females',
#         'males': 'Males',
#         'overall_victims': 'Overall Victims'
#     }, inplace=True)
    
#     table_df.sort_values('Year', inplace=True)
    
#     return table_df

# Summary table displaying total numbers with percentage
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

    for i, annotation in enumerate(table_fig.layout.annotations):
        if i < n_columns:
            annotation.font.color = 'white'
            annotation.font.size = 14
            annotation.text = f"<b>{annotation.text}</b>"
        else:
            annotation.font.color = 'black'
            annotation.font.size = 12

    return table_fig