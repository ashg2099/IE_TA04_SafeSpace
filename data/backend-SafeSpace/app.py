from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# First dashboard (street harassment by gender)
TABLEAU_DASHBOARD_URL_1 = (
    "https://public.tableau.com/app/profile/miranda3916/viz/AUStreetHarassmentDataAustrlianNumberofVictimbyGender/Dashboard1"
    + "?publish=yes"
    + "&:showVizHome=no"
    + "&:embed=true"
    + "&:toolbar=yes"
)

# Second dashboard (other harassment data)
TABLEAU_DASHBOARD_URL_2 = (
    "https://public.tableau.com/app/profile/miranda3916/viz/AUStreetHarassmentData/Dashboard2"
    + "?publish=yes"
    + "&:showVizHome=no"
    + "&:embed=true"
    + "&:toolbar=yes"
)

# @app.route('/api/tableau_street_harassment_gender', methods=['GET'])
# def tableau_gender_embed():
#     # """
#     # Returns the HTML snippet needed to embed the "Victim by Gender" harassment dashboard.
#     # """
#     # embed_html = f'''
#     #   <iframe
#     #     src="{TABLEAU_DASHBOARD_URL_1}"
#     #     width="100%"
#     #     height="800px"
#     #     frameborder="0"
#     #     allowfullscreen>
#     #   </iframe>
#     # '''
#     return jsonify({
#         "embedHtml": embed_html,
#         "dashboardUrl": TABLEAU_DASHBOARD_URL_1
#     })

@app.route('/api/tableau_street_harassment_gender', methods=['GET'])
def tableau_gender_embed():
    return jsonify({
      "dashboardUrl": TABLEAU_DASHBOARD_URL_1
    })

@app.route('/api/tableau_street_harassment_general', methods=['GET'])
def tableau_general_embed():
    # """
    # Returns the HTML snippet needed to embed the "General Street Harassment" dashboard.
    # """
    # embed_html = f'''
    #   <iframe
    #     src="{TABLEAU_DASHBOARD_URL_2}"
    #     width="100%"
    #     height="800px"
    #     frameborder="0"
    #     allowfullscreen>
    #   </iframe>
    # '''
    # return jsonify({
    #     "embedHtml": embed_html,
    #     "dashboardUrl": TABLEAU_DASHBOARD_URL_2
    # })
        return jsonify({
      "dashboardUrl": TABLEAU_DASHBOARD_URL_1
    })

if __name__ == '__main__':
    app.run(debug=True)