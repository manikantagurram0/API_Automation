

def test_dashboard(dashboard):
   dashboardf, res=dashboard
   response= dashboardf.dashboard_ser(res)
   assert response.json()["dashBoard"]["totalSearchAppearancesCount"] >0
   assert response.json()["dashBoard"]["totalSearchAppearancesCount"] ==78
   