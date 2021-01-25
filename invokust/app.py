import invokust
import requests

url = "https://raw.githubusercontent.com/Niraj-Fonseka/invokust-tinker/master/invokust/locustfile.py"

r = requests.get(url)
with open("temp_locustfile.py", 'wb') as f:
#giving a name and saving it in any required format
#opening the file in write mode
    f.write(r.content) 

settings = invokust.create_settings(
    locustfile='temp_locustfile.py',
    host='https://938eff4b6a23.ngrok.io',
    num_users=1,
    spawn_rate=1,
    run_time='5s'
    )

loadtest = invokust.LocustLoadTest(settings)
loadtest.run()
loadtest.stats()