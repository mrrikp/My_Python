import datapoint

# Create connection to DataPoint with your API key
conn = datapoint.connection(api_key="4449caa3-1a0b-4351-bd68-6e1ce103ebae")

# Get the nearest site for my longitude and latitude
site = conn.get_nearest_site(-0.124626, 51.500728)

# Get a forecast for my nearest site with 3 hourly timesteps
forecast = conn.get_forecast_for_site(site.id, "3hourly")

# Get the current timestep from the forecast
current_timestep = forecast.now()

# Print out the site and current weather
print (site.name, "-", current_timestep.weather.text)