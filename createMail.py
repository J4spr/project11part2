def createMail(data):
    head = '''<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Weather Forecast</title>
        <style>
            .container {
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            h2 {
                margin-bottom: 20px;
            }
            .day {
                border: 1px solid #ccc;
                padding: 10px;
                margin-bottom: 20px;
            }
        </style>
    </head>'''
    locationInfo = ""
    for place in data:
        locationInfo += f'''
        <div class="day">
            <b>Location:</b> {place.get('location').get('city')} | {place.get('location').get('country')}<br>
            <b>Datum:</b> {place.get('date')[0]} tot {place.get('date')[0]}<br>
            <b>Temperatuur:</b> {place.get('temp')} °C<br>
            <b>Neerslag:</b> {place.get('precipitation')} mm<br>
            <b>Weer:</b> {place.get('description')}<br>
            <b>Windsnelheid:</b> {place.get('wind_speed')} m/s<br>
        </div>
        '''
    mail = f'''
    <!DOCTYPE html>
        <html lang="en">
            {head}
            <body>
                <div class="container">
                    <h2>Weersvoorspelling voor de komende vijf dagen:</h2>
                    {locationInfo}
                </div>
            </body>
        </html>'''
    return mail