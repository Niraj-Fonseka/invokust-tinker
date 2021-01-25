import invokust

settings = invokust.create_settings(
    locustfile='locustfile.py',
    host='https://3600264080a1.ngrok.io',
    num_users=1,
    spawn_rate=1,
    run_time='15s'
    )

loadtest = invokust.LocustLoadTest(settings)
loadtest.run()
loadtest.stats()