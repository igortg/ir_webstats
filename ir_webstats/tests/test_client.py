from ir_webstats.client import iRWebStats


def test_all_series(mocker):
    irw = iRWebStats()
    with open('statsseries.html') as html_test_file:
        html_test_content = html_test_file.read()

    mocker.patch.object(irw, '_req', return_value=html_test_content)
    irw.logged = True
    series = irw.all_series()
    assert len(series) == 208
    assert series[0]['name'] == '12 Hours of Sebring'
    assert series[-1]['name'] == 'World of Outlaws Sprint Car Series'


def test_all_seasons(mocker):
    irw = iRWebStats()
    irw._all_seasons_filename = 'getseasons.html'

    seasons = irw.all_seasons()
    assert len(seasons) == 66
    assert seasons[0]['seriesshortname'] == 'Advanced Mazda MX-5 Cup Series'
    assert seasons[0]['year'] == 2017
    assert seasons[-1]['seriesshortname'] == 'World of Outlaws Sprint Car Series'
